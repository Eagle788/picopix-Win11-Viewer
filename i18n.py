"""Traductions de PPX Win11 Viewer. t(clé, **valeurs) renvoie le texte dans la langue courante."""
import os

NAMES = {"fr": "Français", "en": "English", "es": "Español", "de": "Deutsch", "it": "Italiano",
         "pt": "Português", "ru": "Русский", "zh": "中文", "ja": "日本語"}
# langue principale Windows (LANGID & 0x3FF) -> code
_WIN = {0x0C: "fr", 0x09: "en", 0x0A: "es", 0x07: "de", 0x10: "it", 0x16: "pt", 0x19: "ru", 0x04: "zh", 0x11: "ja"}
_PREF = os.path.join(os.environ.get("APPDATA", "."), "PPXWin11Viewer", "langue.txt")

T = {
    "fr": {
        "subtitle": "Projetez votre écran sur le Philips PicoPix PPX2330 par USB",
        "ready": "Prêt. Branchez et allumez le projecteur, puis cliquez sur Démarrer.",
        "start": "▶  Démarrer", "stop": "■  Arrêter", "stopping": "Arrêt...",
        "screen": "Écran à projeter", "screen_item": "Écran {i} ({w}x{h})",
        "quality": "Netteté", "quality_hint": "Plus net = moins fluide",
        "fps": "Images par seconde", "fps_hint": "Moins = soulage le PC",
        "language": "Langue", "help_btn": "Aide / installation", "zadig_btn": "Télécharger Zadig",
        "credits": "Protocole USB : projet libre libam7xxx (Antonio Ospite)",
        "connecting": "Connexion au projecteur...", "running": "Projection en cours ({w}x{h}).",
        "running_stats": "Projection en cours : {stats}", "stopped": "Projection arrêtée.",
        "lost": "Connexion perdue ({e}).\nÉteignez le projecteur 10 secondes, rallumez-le, puis Démarrer.",
        "stats": "{fps:.1f} images/s, {kb} Ko/image",
        "switching": "Projecteur en mode stockage : bascule en mode écran...",
        "display_active": "Mode écran actif, attente de la fin du logo Philips...",
        "connected": "PicoPix connecté, résolution native {w}x{h}",
        "err_storage_driver": "Le projecteur est branché mais Windows le garde en mode clé USB.\n"
                              "Installez le pilote WinUSB sur « PicoPix2330 » avec Zadig (voir Aide).",
        "not_found": "Projecteur introuvable.\nAllumez-le avec le câble USB branché et attendez l'écran « Connexion au PC ».",
        "err_display_driver": "Le projecteur est en mode écran mais sans le bon pilote.\n"
                              "Installez WinUSB sur « actions-subdisplay » avec Zadig (voir Aide).",
        "no_response": "Le projecteur ne répond pas. Éteignez-le 10 secondes (interrupteur sur le côté),\n"
                       "rallumez-le avec le câble USB branché, puis réessayez.",
        "bad_reply": "Réponse inattendue du projecteur : {hex}",
        "help": """Installation (une seule fois par PC)

Le projecteur a deux identités USB. Chacune a besoin du pilote WinUSB.

1. Téléchargez Zadig (bouton ci-dessous) et lancez-le.
2. Branchez le projecteur, allumez-le, attendez « Connexion au PC ».
3. Dans Zadig : menu Options > List All Devices.
4. Choisissez « PicoPix2330 » (USB ID 1DE1 1101),
   pilote « WinUSB », puis « Replace Driver ».
5. Revenez ici et cliquez sur Démarrer : le projecteur passe
   en mode écran (puis une erreur de pilote s'affiche, c'est normal).
6. Dans Zadig, choisissez « actions-subdisplay » (USB ID 21E7 0019),
   pilote « WinUSB », puis « Replace Driver ».
7. Cliquez à nouveau sur Démarrer. C'est fini !

Si le projecteur ne répond plus : éteignez-le 10 secondes
avec l'interrupteur sur le côté, rallumez-le, puis Démarrer.

Note : avec WinUSB, l'explorateur Windows n'affiche plus
les fichiers du projecteur.""",
    },
    "en": {
        "subtitle": "Project your screen on the Philips PicoPix PPX2330 over USB",
        "ready": "Ready. Plug in and switch on the projector, then click Start.",
        "start": "▶  Start", "stop": "■  Stop", "stopping": "Stopping...",
        "screen": "Screen to project", "screen_item": "Screen {i} ({w}x{h})",
        "quality": "Sharpness", "quality_hint": "Sharper = less smooth",
        "fps": "Frames per second", "fps_hint": "Lower = lighter on the PC",
        "language": "Language", "help_btn": "Help / setup", "zadig_btn": "Download Zadig",
        "credits": "USB protocol: libam7xxx open-source project (Antonio Ospite)",
        "connecting": "Connecting to the projector...", "running": "Projecting ({w}x{h}).",
        "running_stats": "Projecting: {stats}", "stopped": "Projection stopped.",
        "lost": "Connection lost ({e}).\nSwitch the projector off for 10 seconds, switch it back on, then Start.",
        "stats": "{fps:.1f} fps, {kb} KB/frame",
        "switching": "Projector in storage mode: switching to display mode...",
        "display_active": "Display mode on, waiting for the Philips logo to finish...",
        "connected": "PicoPix connected, native resolution {w}x{h}",
        "err_storage_driver": "The projector is connected but Windows keeps it in USB drive mode.\n"
                              "Install the WinUSB driver on \"PicoPix2330\" with Zadig (see Help).",
        "not_found": "Projector not found.\nSwitch it on with the USB cable plugged in and wait for the \"PC connection\" screen.",
        "err_display_driver": "The projector is in display mode but has the wrong driver.\n"
                              "Install WinUSB on \"actions-subdisplay\" with Zadig (see Help).",
        "no_response": "The projector does not respond. Switch it off for 10 seconds (switch on the side),\n"
                       "switch it back on with the USB cable plugged in, then try again.",
        "bad_reply": "Unexpected reply from the projector: {hex}",
        "help": """Setup (once per PC)

The projector has two USB identities. Each one needs the WinUSB driver.

1. Download Zadig (button below) and run it.
2. Plug in the projector, switch it on, wait for "PC connection".
3. In Zadig: Options menu > List All Devices.
4. Choose "PicoPix2330" (USB ID 1DE1 1101),
   driver "WinUSB", then "Replace Driver".
5. Come back here and click Start: the projector switches
   to display mode (then a driver error appears, that's normal).
6. In Zadig, choose "actions-subdisplay" (USB ID 21E7 0019),
   driver "WinUSB", then "Replace Driver".
7. Click Start again. Done!

If the projector stops responding: switch it off for 10 seconds
with the switch on the side, switch it on again, then Start.

Note: with WinUSB, Windows Explorer no longer shows
the projector's files.""",
    },
    "es": {
        "subtitle": "Proyecta tu pantalla en el Philips PicoPix PPX2330 por USB",
        "ready": "Listo. Conecta y enciende el proyector y pulsa Iniciar.",
        "start": "▶  Iniciar", "stop": "■  Detener", "stopping": "Deteniendo...",
        "screen": "Pantalla a proyectar", "screen_item": "Pantalla {i} ({w}x{h})",
        "quality": "Nitidez", "quality_hint": "Más nítido = menos fluido",
        "fps": "Imágenes por segundo", "fps_hint": "Menos = alivia el PC",
        "language": "Idioma", "help_btn": "Ayuda / instalación", "zadig_btn": "Descargar Zadig",
        "credits": "Protocolo USB: proyecto libre libam7xxx (Antonio Ospite)",
        "connecting": "Conectando con el proyector...", "running": "Proyectando ({w}x{h}).",
        "running_stats": "Proyectando: {stats}", "stopped": "Proyección detenida.",
        "lost": "Conexión perdida ({e}).\nApaga el proyector 10 segundos, vuelve a encenderlo y pulsa Iniciar.",
        "stats": "{fps:.1f} imágenes/s, {kb} KB/imagen",
        "switching": "Proyector en modo almacenamiento: cambiando a modo pantalla...",
        "display_active": "Modo pantalla activo, esperando a que termine el logo de Philips...",
        "connected": "PicoPix conectado, resolución nativa {w}x{h}",
        "err_storage_driver": "El proyector está conectado pero Windows lo mantiene en modo memoria USB.\n"
                              "Instala el controlador WinUSB en «PicoPix2330» con Zadig (ver Ayuda).",
        "not_found": "Proyector no encontrado.\nEnciéndelo con el cable USB conectado y espera la pantalla «Conexión al PC».",
        "err_display_driver": "El proyector está en modo pantalla pero sin el controlador correcto.\n"
                              "Instala WinUSB en «actions-subdisplay» con Zadig (ver Ayuda).",
        "no_response": "El proyector no responde. Apágalo 10 segundos (interruptor lateral),\n"
                       "enciéndelo con el cable USB conectado y vuelve a intentarlo.",
        "bad_reply": "Respuesta inesperada del proyector: {hex}",
        "help": """Instalación (una sola vez por PC)

El proyector tiene dos identidades USB. Cada una necesita el controlador WinUSB.

1. Descarga Zadig (botón de abajo) y ejecútalo.
2. Conecta el proyector, enciéndelo y espera «Conexión al PC».
3. En Zadig: menú Options > List All Devices.
4. Elige «PicoPix2330» (USB ID 1DE1 1101),
   controlador «WinUSB» y luego «Replace Driver».
5. Vuelve aquí y pulsa Iniciar: el proyector pasa a modo
   pantalla (luego aparece un error de controlador, es normal).
6. En Zadig, elige «actions-subdisplay» (USB ID 21E7 0019),
   controlador «WinUSB» y luego «Replace Driver».
7. Pulsa Iniciar de nuevo. ¡Listo!

Si el proyector deja de responder: apágalo 10 segundos
con el interruptor lateral, vuelve a encenderlo y pulsa Iniciar.

Nota: con WinUSB, el Explorador de Windows ya no muestra
los archivos del proyector.""",
    },
    "de": {
        "subtitle": "Bildschirm per USB auf den Philips PicoPix PPX2330 projizieren",
        "ready": "Bereit. Projektor anschließen und einschalten, dann auf Start klicken.",
        "start": "▶  Start", "stop": "■  Stopp", "stopping": "Wird beendet...",
        "screen": "Zu projizierender Bildschirm", "screen_item": "Bildschirm {i} ({w}x{h})",
        "quality": "Schärfe", "quality_hint": "Schärfer = weniger flüssig",
        "fps": "Bilder pro Sekunde", "fps_hint": "Weniger = entlastet den PC",
        "language": "Sprache", "help_btn": "Hilfe / Einrichtung", "zadig_btn": "Zadig herunterladen",
        "credits": "USB-Protokoll: freies Projekt libam7xxx (Antonio Ospite)",
        "connecting": "Verbindung zum Projektor...", "running": "Projektion läuft ({w}x{h}).",
        "running_stats": "Projektion läuft: {stats}", "stopped": "Projektion beendet.",
        "lost": "Verbindung verloren ({e}).\nProjektor 10 Sekunden ausschalten, wieder einschalten, dann Start.",
        "stats": "{fps:.1f} Bilder/s, {kb} KB/Bild",
        "switching": "Projektor im Speichermodus: Wechsel in den Anzeigemodus...",
        "display_active": "Anzeigemodus aktiv, warte auf das Ende des Philips-Logos...",
        "connected": "PicoPix verbunden, native Auflösung {w}x{h}",
        "err_storage_driver": "Der Projektor ist angeschlossen, aber Windows behandelt ihn als USB-Laufwerk.\n"
                              "Installieren Sie den WinUSB-Treiber für „PicoPix2330“ mit Zadig (siehe Hilfe).",
        "not_found": "Projektor nicht gefunden.\nMit angeschlossenem USB-Kabel einschalten und auf den Bildschirm „PC-Verbindung“ warten.",
        "err_display_driver": "Der Projektor ist im Anzeigemodus, hat aber den falschen Treiber.\n"
                              "Installieren Sie WinUSB für „actions-subdisplay“ mit Zadig (siehe Hilfe).",
        "no_response": "Der Projektor antwortet nicht. 10 Sekunden ausschalten (Schalter an der Seite),\n"
                       "mit angeschlossenem USB-Kabel wieder einschalten und erneut versuchen.",
        "bad_reply": "Unerwartete Antwort des Projektors: {hex}",
        "help": """Einrichtung (einmal pro PC)

Der Projektor hat zwei USB-Identitäten. Jede braucht den WinUSB-Treiber.

1. Zadig herunterladen (Schaltfläche unten) und starten.
2. Projektor anschließen, einschalten, auf „PC-Verbindung“ warten.
3. In Zadig: Menü Options > List All Devices.
4. „PicoPix2330“ wählen (USB ID 1DE1 1101),
   Treiber „WinUSB“, dann „Replace Driver“.
5. Hierher zurückkehren und auf Start klicken: Der Projektor
   wechselt in den Anzeigemodus (dann erscheint ein Treiberfehler, das ist normal).
6. In Zadig „actions-subdisplay“ wählen (USB ID 21E7 0019),
   Treiber „WinUSB“, dann „Replace Driver“.
7. Erneut auf Start klicken. Fertig!

Wenn der Projektor nicht mehr reagiert: 10 Sekunden mit dem
Schalter an der Seite ausschalten, wieder einschalten, dann Start.

Hinweis: Mit WinUSB zeigt der Windows-Explorer die Dateien
des Projektors nicht mehr an.""",
    },
    "it": {
        "subtitle": "Proietta lo schermo sul Philips PicoPix PPX2330 via USB",
        "ready": "Pronto. Collega e accendi il proiettore, poi clicca su Avvia.",
        "start": "▶  Avvia", "stop": "■  Ferma", "stopping": "Arresto...",
        "screen": "Schermo da proiettare", "screen_item": "Schermo {i} ({w}x{h})",
        "quality": "Nitidezza", "quality_hint": "Più nitido = meno fluido",
        "fps": "Immagini al secondo", "fps_hint": "Meno = alleggerisce il PC",
        "language": "Lingua", "help_btn": "Aiuto / installazione", "zadig_btn": "Scarica Zadig",
        "credits": "Protocollo USB: progetto libero libam7xxx (Antonio Ospite)",
        "connecting": "Connessione al proiettore...", "running": "Proiezione in corso ({w}x{h}).",
        "running_stats": "Proiezione in corso: {stats}", "stopped": "Proiezione fermata.",
        "lost": "Connessione persa ({e}).\nSpegni il proiettore per 10 secondi, riaccendilo, poi Avvia.",
        "stats": "{fps:.1f} immagini/s, {kb} KB/immagine",
        "switching": "Proiettore in modalità archiviazione: passaggio alla modalità schermo...",
        "display_active": "Modalità schermo attiva, attesa della fine del logo Philips...",
        "connected": "PicoPix connesso, risoluzione nativa {w}x{h}",
        "err_storage_driver": "Il proiettore è collegato ma Windows lo tiene in modalità chiavetta USB.\n"
                              "Installa il driver WinUSB su «PicoPix2330» con Zadig (vedi Aiuto).",
        "not_found": "Proiettore non trovato.\nAccendilo con il cavo USB collegato e attendi la schermata «Connessione al PC».",
        "err_display_driver": "Il proiettore è in modalità schermo ma senza il driver giusto.\n"
                              "Installa WinUSB su «actions-subdisplay» con Zadig (vedi Aiuto).",
        "no_response": "Il proiettore non risponde. Spegnilo per 10 secondi (interruttore laterale),\n"
                       "riaccendilo con il cavo USB collegato, poi riprova.",
        "bad_reply": "Risposta inattesa dal proiettore: {hex}",
        "help": """Installazione (una sola volta per PC)

Il proiettore ha due identità USB. Ognuna richiede il driver WinUSB.

1. Scarica Zadig (pulsante qui sotto) e avvialo.
2. Collega il proiettore, accendilo, attendi «Connessione al PC».
3. In Zadig: menu Options > List All Devices.
4. Scegli «PicoPix2330» (USB ID 1DE1 1101),
   driver «WinUSB», poi «Replace Driver».
5. Torna qui e clicca su Avvia: il proiettore passa in
   modalità schermo (poi compare un errore di driver, è normale).
6. In Zadig, scegli «actions-subdisplay» (USB ID 21E7 0019),
   driver «WinUSB», poi «Replace Driver».
7. Clicca di nuovo su Avvia. Fatto!

Se il proiettore non risponde più: spegnilo per 10 secondi
con l'interruttore laterale, riaccendilo, poi Avvia.

Nota: con WinUSB, Esplora risorse non mostra più
i file del proiettore.""",
    },
    "pt": {
        "subtitle": "Projete a sua tela no Philips PicoPix PPX2330 via USB",
        "ready": "Pronto. Conecte e ligue o projetor e clique em Iniciar.",
        "start": "▶  Iniciar", "stop": "■  Parar", "stopping": "Parando...",
        "screen": "Tela a projetar", "screen_item": "Tela {i} ({w}x{h})",
        "quality": "Nitidez", "quality_hint": "Mais nítido = menos fluido",
        "fps": "Imagens por segundo", "fps_hint": "Menos = alivia o PC",
        "language": "Idioma", "help_btn": "Ajuda / instalação", "zadig_btn": "Baixar o Zadig",
        "credits": "Protocolo USB: projeto livre libam7xxx (Antonio Ospite)",
        "connecting": "Conectando ao projetor...", "running": "Projetando ({w}x{h}).",
        "running_stats": "Projetando: {stats}", "stopped": "Projeção parada.",
        "lost": "Conexão perdida ({e}).\nDesligue o projetor por 10 segundos, ligue-o novamente e clique em Iniciar.",
        "stats": "{fps:.1f} imagens/s, {kb} KB/imagem",
        "switching": "Projetor em modo armazenamento: mudando para modo tela...",
        "display_active": "Modo tela ativo, aguardando o fim do logotipo Philips...",
        "connected": "PicoPix conectado, resolução nativa {w}x{h}",
        "err_storage_driver": "O projetor está conectado, mas o Windows o mantém como pen drive.\n"
                              "Instale o driver WinUSB em \"PicoPix2330\" com o Zadig (ver Ajuda).",
        "not_found": "Projetor não encontrado.\nLigue-o com o cabo USB conectado e aguarde a tela \"Conexão ao PC\".",
        "err_display_driver": "O projetor está em modo tela, mas sem o driver correto.\n"
                              "Instale o WinUSB em \"actions-subdisplay\" com o Zadig (ver Ajuda).",
        "no_response": "O projetor não responde. Desligue-o por 10 segundos (interruptor lateral),\n"
                       "ligue-o novamente com o cabo USB conectado e tente de novo.",
        "bad_reply": "Resposta inesperada do projetor: {hex}",
        "help": """Instalação (uma única vez por PC)

O projetor tem duas identidades USB. Cada uma precisa do driver WinUSB.

1. Baixe o Zadig (botão abaixo) e execute-o.
2. Conecte o projetor, ligue-o e aguarde "Conexão ao PC".
3. No Zadig: menu Options > List All Devices.
4. Escolha "PicoPix2330" (USB ID 1DE1 1101),
   driver "WinUSB" e depois "Replace Driver".
5. Volte aqui e clique em Iniciar: o projetor muda para
   modo tela (depois aparece um erro de driver, é normal).
6. No Zadig, escolha "actions-subdisplay" (USB ID 21E7 0019),
   driver "WinUSB" e depois "Replace Driver".
7. Clique em Iniciar novamente. Pronto!

Se o projetor parar de responder: desligue-o por 10 segundos
com o interruptor lateral, ligue-o de novo e clique em Iniciar.

Observação: com o WinUSB, o Explorador do Windows deixa de
mostrar os arquivos do projetor.""",
    },
    "ru": {
        "subtitle": "Вывод экрана на Philips PicoPix PPX2330 через USB",
        "ready": "Готово. Подключите и включите проектор, затем нажмите «Старт».",
        "start": "▶  Старт", "stop": "■  Стоп", "stopping": "Остановка...",
        "screen": "Экран для показа", "screen_item": "Экран {i} ({w}x{h})",
        "quality": "Чёткость", "quality_hint": "Чётче = менее плавно",
        "fps": "Кадров в секунду", "fps_hint": "Меньше = меньше нагрузка на ПК",
        "language": "Язык", "help_btn": "Справка / установка", "zadig_btn": "Скачать Zadig",
        "credits": "USB-протокол: свободный проект libam7xxx (Antonio Ospite)",
        "connecting": "Подключение к проектору...", "running": "Идёт показ ({w}x{h}).",
        "running_stats": "Идёт показ: {stats}", "stopped": "Показ остановлен.",
        "lost": "Соединение потеряно ({e}).\nВыключите проектор на 10 секунд, включите снова и нажмите «Старт».",
        "stats": "{fps:.1f} кадр/с, {kb} КБ/кадр",
        "switching": "Проектор в режиме накопителя: переключение в режим экрана...",
        "display_active": "Режим экрана включён, ожидание окончания логотипа Philips...",
        "connected": "PicoPix подключён, разрешение {w}x{h}",
        "err_storage_driver": "Проектор подключён, но Windows видит его как USB-накопитель.\n"
                              "Установите драйвер WinUSB для «PicoPix2330» через Zadig (см. Справку).",
        "not_found": "Проектор не найден.\nВключите его с подключённым USB-кабелем и дождитесь экрана «Подключение к ПК».",
        "err_display_driver": "Проектор в режиме экрана, но драйвер неверный.\n"
                              "Установите WinUSB для «actions-subdisplay» через Zadig (см. Справку).",
        "no_response": "Проектор не отвечает. Выключите его на 10 секунд (выключатель сбоку),\n"
                       "включите снова с подключённым USB-кабелем и повторите попытку.",
        "bad_reply": "Неожиданный ответ проектора: {hex}",
        "help": """Установка (один раз на каждом ПК)

У проектора два USB-режима. Каждому нужен драйвер WinUSB.

1. Скачайте Zadig (кнопка ниже) и запустите его.
2. Подключите проектор, включите, дождитесь «Подключение к ПК».
3. В Zadig: меню Options > List All Devices.
4. Выберите «PicoPix2330» (USB ID 1DE1 1101),
   драйвер «WinUSB», затем «Replace Driver».
5. Вернитесь сюда и нажмите «Старт»: проектор перейдёт
   в режим экрана (затем появится ошибка драйвера, это нормально).
6. В Zadig выберите «actions-subdisplay» (USB ID 21E7 0019),
   драйвер «WinUSB», затем «Replace Driver».
7. Снова нажмите «Старт». Готово!

Если проектор перестал отвечать: выключите его на 10 секунд
выключателем сбоку, включите снова и нажмите «Старт».

Примечание: с WinUSB Проводник Windows больше не показывает
файлы проектора.""",
    },
    "zh": {
        "subtitle": "通过 USB 将电脑屏幕投影到飞利浦 PicoPix PPX2330",
        "ready": "就绪。请连接并打开投影仪，然后点击“开始”。",
        "start": "▶  开始", "stop": "■  停止", "stopping": "正在停止...",
        "screen": "要投影的屏幕", "screen_item": "屏幕 {i}（{w}x{h}）",
        "quality": "清晰度", "quality_hint": "越清晰越不流畅",
        "fps": "每秒帧数", "fps_hint": "越低电脑负担越小",
        "language": "语言", "help_btn": "帮助 / 安装", "zadig_btn": "下载 Zadig",
        "credits": "USB 协议：开源项目 libam7xxx（Antonio Ospite）",
        "connecting": "正在连接投影仪...", "running": "正在投影（{w}x{h}）。",
        "running_stats": "正在投影：{stats}", "stopped": "投影已停止。",
        "lost": "连接中断（{e}）。\n请关闭投影仪 10 秒，重新打开，然后点击“开始”。",
        "stats": "{fps:.1f} 帧/秒，{kb} KB/帧",
        "switching": "投影仪处于存储模式：正在切换到显示模式...",
        "display_active": "显示模式已开启，正在等待飞利浦标志结束...",
        "connected": "PicoPix 已连接，原生分辨率 {w}x{h}",
        "err_storage_driver": "投影仪已连接，但 Windows 将其识别为 U 盘。\n"
                              "请用 Zadig 为“PicoPix2330”安装 WinUSB 驱动（见帮助）。",
        "not_found": "未找到投影仪。\n请在连接 USB 线的情况下打开投影仪，并等待“连接电脑”画面。",
        "err_display_driver": "投影仪处于显示模式，但驱动不正确。\n"
                              "请用 Zadig 为“actions-subdisplay”安装 WinUSB（见帮助）。",
        "no_response": "投影仪无响应。请关闭 10 秒（侧面的开关），\n"
                       "在连接 USB 线的情况下重新打开，然后重试。",
        "bad_reply": "投影仪返回了意外的响应：{hex}",
        "help": """安装（每台电脑只需一次）

投影仪有两个 USB 身份，每个都需要 WinUSB 驱动。

1. 下载 Zadig（下方按钮）并运行。
2. 连接投影仪并打开，等待“连接电脑”画面。
3. 在 Zadig 中：菜单 Options > List All Devices。
4. 选择“PicoPix2330”（USB ID 1DE1 1101），
   驱动选“WinUSB”，然后点“Replace Driver”。
5. 回到这里点击“开始”：投影仪会切换到显示模式
   （随后会出现驱动错误，这是正常的）。
6. 在 Zadig 中选择“actions-subdisplay”（USB ID 21E7 0019），
   驱动选“WinUSB”，然后点“Replace Driver”。
7. 再次点击“开始”。完成！

如果投影仪无响应：用侧面的开关关闭 10 秒，
重新打开，然后点击“开始”。

注意：安装 WinUSB 后，Windows 资源管理器将不再显示
投影仪中的文件。""",
    },
    "ja": {
        "subtitle": "USB で画面を Philips PicoPix PPX2330 に投影します",
        "ready": "準備完了。プロジェクターを接続して電源を入れ、「開始」をクリックしてください。",
        "start": "▶  開始", "stop": "■  停止", "stopping": "停止中...",
        "screen": "投影する画面", "screen_item": "画面 {i}（{w}x{h}）",
        "quality": "画質", "quality_hint": "高画質ほど動きが重くなります",
        "fps": "フレームレート", "fps_hint": "低いほど PC の負荷が軽くなります",
        "language": "言語", "help_btn": "ヘルプ / セットアップ", "zadig_btn": "Zadig をダウンロード",
        "credits": "USB プロトコル：オープンソースプロジェクト libam7xxx（Antonio Ospite）",
        "connecting": "プロジェクターに接続中...", "running": "投影中（{w}x{h}）。",
        "running_stats": "投影中：{stats}", "stopped": "投影を停止しました。",
        "lost": "接続が切れました（{e}）。\nプロジェクターの電源を 10 秒切ってから入れ直し、「開始」をクリックしてください。",
        "stats": "{fps:.1f} fps、{kb} KB/フレーム",
        "switching": "プロジェクターはストレージモードです。表示モードに切り替え中...",
        "display_active": "表示モードになりました。Philips のロゴが消えるのを待っています...",
        "connected": "PicoPix に接続しました。ネイティブ解像度 {w}x{h}",
        "err_storage_driver": "プロジェクターは接続されていますが、Windows が USB ドライブとして扱っています。\n"
                              "Zadig で「PicoPix2330」に WinUSB ドライバーをインストールしてください（ヘルプ参照）。",
        "not_found": "プロジェクターが見つかりません。\nUSB ケーブルを接続したまま電源を入れ、「PC 接続」画面になるまで待ってください。",
        "err_display_driver": "プロジェクターは表示モードですが、ドライバーが正しくありません。\n"
                              "Zadig で「actions-subdisplay」に WinUSB をインストールしてください（ヘルプ参照）。",
        "no_response": "プロジェクターが応答しません。側面のスイッチで 10 秒電源を切り、\n"
                       "USB ケーブルを接続したまま電源を入れ直して、もう一度お試しください。",
        "bad_reply": "プロジェクターから予期しない応答がありました：{hex}",
        "help": """セットアップ（PC ごとに 1 回）

プロジェクターには 2 つの USB モードがあり、それぞれに WinUSB ドライバーが必要です。

1. Zadig をダウンロード（下のボタン）して起動します。
2. プロジェクターを接続して電源を入れ、「PC 接続」画面を待ちます。
3. Zadig で：メニュー Options > List All Devices。
4. 「PicoPix2330」（USB ID 1DE1 1101）を選び、
   ドライバー「WinUSB」で「Replace Driver」をクリック。
5. ここに戻って「開始」をクリック：プロジェクターが表示モードに
   切り替わります（その後ドライバーエラーが出ますが正常です）。
6. Zadig で「actions-subdisplay」（USB ID 21E7 0019）を選び、
   ドライバー「WinUSB」で「Replace Driver」をクリック。
7. もう一度「開始」をクリック。完了です！

プロジェクターが応答しなくなったら：側面のスイッチで 10 秒
電源を切り、入れ直してから「開始」をクリックしてください。

注意：WinUSB を入れると、エクスプローラーにプロジェクターの
ファイルが表示されなくなります。""",
    },
}


def _detect():
    try:
        with open(_PREF, encoding="utf-8") as f:
            code = f.read().strip()
            if code in T:
                return code
    except OSError:
        pass
    try:
        import ctypes
        return _WIN.get(ctypes.windll.kernel32.GetUserDefaultUILanguage() & 0x3FF, "en")
    except (AttributeError, OSError):
        return "en"


lang = _detect()


def set_lang(code):
    global lang
    lang = code
    try:
        os.makedirs(os.path.dirname(_PREF), exist_ok=True)
        with open(_PREF, "w", encoding="utf-8") as f:
            f.write(code)
    except OSError:
        pass  # préférence non sauvegardée : pas grave, la langue change quand même


def t(key, **kw):
    return T[lang].get(key, T["en"][key]).format(**kw)
