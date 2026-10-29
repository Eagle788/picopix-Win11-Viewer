"""PPX Win11 Viewer : fenêtre simple pour projeter l'écran sur un Philips PicoPix PPX2330 en USB."""
import queue
import threading
import tkinter as tk
import webbrowser
from tkinter import ttk

import mss

import i18n
import picopix
from i18n import t


class App:
    def __init__(self, root):
        self.root = root
        self.msgs = queue.Queue()
        self.stop = threading.Event()
        self.worker = None
        with mss.MSS() as sct:
            self.monitors = [(m["width"], m["height"]) for m in sct.monitors[1:]]
        self.settings = {"monitor": 1, "fps": 30, "quality": 80}
        self.frame = None
        self.res = (0, 0)

        root.title("PPX Win11 Viewer")
        root.resizable(False, False)
        root.protocol("WM_DELETE_WINDOW", self.quit)
        self.build()
        self.poll()

    def running(self):
        return self.worker is not None and self.worker.is_alive()

    def build(self):
        """(Re)construit l'interface dans la langue courante."""
        if self.frame:
            self.frame.destroy()
        f = self.frame = ttk.Frame(self.root, padding=16)
        f.grid()
        f.columnconfigure(1, weight=1)

        ttk.Label(f, text="PPX Win11 Viewer", font=("Segoe UI", 16, "bold")).grid(row=0, column=0, sticky="w")
        langs = list(i18n.NAMES)
        lang = ttk.Combobox(f, values=list(i18n.NAMES.values()), state="readonly", width=10)
        lang.current(langs.index(i18n.lang))
        lang.bind("<<ComboboxSelected>>", lambda _: self.change_lang(langs[lang.current()]))
        lang.grid(row=0, column=1, sticky="e")
        ttk.Label(f, text=t("subtitle")).grid(row=1, columnspan=2, sticky="w", pady=(0, 12))

        self.status = tk.StringVar(value=t("running", w=self.res[0], h=self.res[1]) if self.running() else t("ready"))
        ttk.Label(f, textvariable=self.status, wraplength=400, justify="left").grid(
            row=2, columnspan=2, sticky="w", pady=(0, 12))

        self.btn = ttk.Button(f, text=t("stop") if self.running() else t("start"), command=self.toggle)
        self.btn.grid(row=3, columnspan=2, sticky="ew", ipady=8, pady=(0, 16))

        ttk.Label(f, text=t("screen")).grid(row=4, column=0, sticky="w", padx=(0, 12))
        screen = ttk.Combobox(f, state="readonly", width=28,
                              values=[t("screen_item", i=i, w=w, h=h) for i, (w, h) in enumerate(self.monitors, 1)])
        screen.current(self.settings["monitor"] - 1)
        screen.bind("<<ComboboxSelected>>", lambda _: self.settings.update(monitor=screen.current() + 1))
        screen.grid(row=4, column=1, sticky="ew", pady=4)

        self.slider(f, 5, t("quality"), "quality", 30, 95, t("quality_hint"))
        self.slider(f, 7, t("fps"), "fps", 5, 30, t("fps_hint"))

        ttk.Button(f, text=t("help_btn"), command=self.help).grid(row=9, columnspan=2, sticky="ew", pady=(12, 0))

    def change_lang(self, code):
        i18n.set_lang(code)
        self.build()

    def slider(self, f, row, label, key, lo, hi, hint):
        val = tk.IntVar(value=self.settings[key])
        txt = ttk.Label(f, text=f"{label} : {val.get()}")
        txt.grid(row=row, column=0, sticky="w", padx=(0, 12))

        def changed(v):
            val.set(round(float(v)))
            self.settings[key] = val.get()
            txt.config(text=f"{label} : {val.get()}")
        ttk.Scale(f, from_=lo, to=hi, variable=val, command=changed).grid(row=row, column=1, sticky="ew", pady=4)
        ttk.Label(f, text=hint, foreground="gray").grid(row=row + 1, column=1, sticky="w")

    def toggle(self):
        if self.running():
            self.stop.set()
            self.btn.config(state="disabled")
            self.status.set(t("stopping"))
            return
        self.stop.clear()
        self.btn.config(text=t("stop"))
        self.worker = threading.Thread(target=self.run, daemon=True)
        self.worker.start()

    def run(self):
        log = self.msgs.put
        try:
            log(t("connecting"))
            dev, w, h = picopix.open_device(log)
            self.res = (w, h)
            log(t("running", w=w, h=h))
            picopix.stream(dev, w, h, self.settings, self.stop, lambda m: log(t("running_stats", stats=m)))
            log(t("stopped"))
        except picopix.PicoPixError as e:
            log(str(e))
        except Exception as e:  # câble débranché, projecteur éteint...
            log(t("lost", e=e))
        log(None)

    def poll(self):
        try:
            while True:
                m = self.msgs.get_nowait()
                if m is None:
                    self.btn.config(text=t("start"), state="normal")
                else:
                    self.status.set(m)
        except queue.Empty:
            pass
        self.root.after(200, self.poll)

    def help(self):
        w = tk.Toplevel(self.root)
        w.title(t("help_btn"))
        w.resizable(False, False)
        ttk.Label(w, text=t("help"), justify="left", padding=16).pack()
        ttk.Button(w, text=t("zadig_btn"), command=lambda: webbrowser.open("https://zadig.akeo.ie")).pack(
            fill="x", padx=16)
        ttk.Label(w, text=t("credits"), foreground="gray", padding=(16, 8, 16, 16)).pack()

    def quit(self):
        self.stop.set()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
