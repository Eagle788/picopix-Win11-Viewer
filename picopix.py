"""Affiche l'écran Windows sur un Philips PicoPix PPX2330 en USB (remplace Picopix Fun Viewer).

Protocole repris de libam7xxx (https://git.ao2.it/libam7xxx.git).
Prérequis : pilote WinUSB (via Zadig) sur les deux modes USB du projecteur.
"""
import argparse
import io
import struct
import sys
import time

from i18n import t

VID, PID = 0x21E7, 0x0019
EP_OUT, EP_IN = 0x01, 0x81
DEVINFO, IMAGE = 0x01, 0x02
JPEG = 1
STORAGE_VID, STORAGE_PID = 0x1DE1, 0x1101
# Commande de am7xxx-modeswitch (libam7xxx) ; le PPX2330 exige un CBW de 31 octets pile (sans le NUL que libam7xxx ajoute)
SWITCH_CMD = (b"\x55\x53\x42\x43\x08\x70\x52\x89\x00\x00\x00\x00\x00\x00"
              b"\x10\xff\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
# shortcut: commandes de puissance du PicoPix 2055, non documentées pour le 2330 ; à retirer si sans effet
POWER = {"low": 0x15, "medium": 0x16, "high": 0x17}


class PicoPixError(Exception):
    pass


def header(ptype, data_len=0, *words):
    words = (list(words) + [0, 0, 0, 0])[:4]
    return struct.pack("<IBBBB4I", ptype, 0, data_len, 0x3E, 0x10, *words)


def selftest():
    h = header(IMAGE, 16, JPEG, 854, 480, 1234)
    assert len(h) == 24
    assert h[:8] == bytes([2, 0, 0, 0, 0, 16, 0x3E, 0x10])
    assert struct.unpack("<4I", h[8:]) == (1, 854, 480, 1234)
    assert len(SWITCH_CMD) == 31 and SWITCH_CMD[:4] == b"USBC" and SWITCH_CMD[15:17] == b"\xff\x02"
    assert header(DEVINFO) == bytes([1, 0, 0, 0, 0, 0, 0x3E, 0x10]) + bytes(16)
    import i18n
    for code, texts in i18n.T.items():  # chaque langue complète et formatable
        assert texts.keys() == i18n.T["fr"].keys(), code
        for v in texts.values():
            v.format(w=1, h=1, i=1, e="x", hex="00", fps=1.0, kb=1, stats="s")
    print("selftest OK")


def find(vid, pid):
    import libusb_package
    import usb.backend.libusb1

    backend = usb.backend.libusb1.get_backend(find_library=lambda _: libusb_package.get_library_path())
    return usb.core.find(idVendor=vid, idProduct=pid, backend=backend)


def switch_to_display(log=print):
    """Bascule le mode stockage (1DE1:1101, WinUSB requis) vers le mode écran, comme am7xxx-modeswitch."""
    import usb

    st = find(STORAGE_VID, STORAGE_PID)
    if st is None:
        return False
    log(t("switching"))
    try:
        st.set_configuration(1)
        st.write(EP_OUT, SWITCH_CMD, timeout=2000)
    except usb.core.USBError:
        raise PicoPixError(t("err_storage_driver"))
    for _ in range(20):  # le projecteur se reconnecte sous un autre identifiant
        time.sleep(0.5)
        if find(VID, PID) is not None:
            log(t("display_active"))
            time.sleep(8)  # le projecteur ignore puis bloque les commandes tant que le logo s'affiche
            return True
    return False


def open_device(log=print):
    import usb

    dev = find(VID, PID)
    if dev is None and switch_to_display(log):
        dev = find(VID, PID)
    if dev is None:
        raise PicoPixError(t("not_found"))
    try:
        dev.set_configuration(1)
    except usb.core.USBError:
        raise PicoPixError(t("err_display_driver"))
    # Le PicoPix exige DEVINFO comme premier paquet
    try:
        dev.write(EP_OUT, header(DEVINFO), timeout=5000)
        r = bytes(dev.read(EP_IN, 512, timeout=5000))
    except usb.core.USBTimeoutError:
        raise PicoPixError(t("no_response"))
    ptype, direction = struct.unpack_from("<IB", r)
    w, h = struct.unpack_from("<2I", r, 8)
    if ptype != DEVINFO or direction != 1 or not (0 < w <= 4096 and 0 < h <= 4096):
        raise PicoPixError(t("bad_reply", hex=r.hex()))
    log(t("connected", w=w, h=h))
    return dev, w, h


def stream(dev, w, h, settings, stop, log=print):
    """Envoie l'écran jusqu'à stop.set(). settings (dict monitor/fps/quality) est relu à chaque image."""
    import mss
    from PIL import Image

    canvas = Image.new("RGB", (w, h))
    frames, t_stat = 0, time.perf_counter()
    with mss.MSS() as sct:
        while not stop.is_set():
            t0 = time.perf_counter()
            mon = sct.monitors[min(settings["monitor"], len(sct.monitors) - 1)]
            shot = sct.grab(mon)
            img = Image.frombytes("RGB", shot.size, shot.bgra, "raw", "BGRX")
            img.thumbnail((w, h), Image.BILINEAR, reducing_gap=2.0)  # garde le ratio
            canvas.paste((0, 0, 0), (0, 0, w, h))
            canvas.paste(img, ((w - img.width) // 2, (h - img.height) // 2))
            buf = io.BytesIO()
            canvas.save(buf, "JPEG", quality=settings["quality"])
            jpg = buf.getvalue()
            dev.write(EP_OUT, header(IMAGE, 16, JPEG, w, h, len(jpg)), timeout=2000)
            dev.write(EP_OUT, jpg, timeout=2000)

            frames += 1
            now = time.perf_counter()
            if now - t_stat >= 2:
                log(t("stats", fps=frames / (now - t_stat), kb=len(jpg) // 1024))
                frames, t_stat = 0, now
            time.sleep(max(0, 1 / settings["fps"] - (time.perf_counter() - t0)))


def main():
    import threading

    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--monitor", type=int, default=1, help="écran à projeter (1 = principal)")
    p.add_argument("--fps", type=float, default=30)
    p.add_argument("--quality", type=int, default=80, help="qualité JPEG 1-95")
    p.add_argument("--power", choices=POWER, help="EXPÉRIMENTAL : luminosité")
    p.add_argument("--selftest", action="store_true")
    a = p.parse_args()
    if a.selftest:
        return selftest()

    try:
        dev, w, h = open_device()
        if a.power:
            dev.write(EP_OUT, header(POWER[a.power]), timeout=2000)
            print(f"Commande puissance '{a.power}' envoyée")
        print("Projection en cours — Ctrl+C pour arrêter")
        stream(dev, w, h, vars(a), threading.Event())
    except PicoPixError as e:
        sys.exit(str(e))
    except KeyboardInterrupt:
        print("Arrêt.")


if __name__ == "__main__":
    main()
