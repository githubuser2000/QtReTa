#!/usr/bin/env python3.10
# This Python file uses the following encoding: utf-8
# import multiprocessing
import os
# import random
import re
# import string
import sys
# from pathlib import Path
# home = str(Path.home())
# import tempfile
from pathlib import Path

# import zstd
from PySide6.QtCore import QObject, Slot
from PySide6.QtGui import QGuiApplication, QIcon
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QSystemTrayIcon

# tempdir = tempfile.gettempdir()
# import binascii

# import ress
# from data import base

randstr = ""


def windows_to_browser_path(path):
    # Replace backslashes with forward slashes
    path = path.replace("\\", "/")
    # If the path starts with a drive letter, add "file:///" at the beginning
    if len(path) > 1 and path[1] == ":":
        path = "file://" + path
    # If the path doesn't start with a drive letter, add "file:///" before the path
    else:
        path = "file:///" + os.path.abspath(path)
    return path


def linux_to_browser_path(path):
    # Replace backslashes with forward slashes
    path = path.replace("\\", "/")
    # Add "file://" at the beginning
    path = "file://" + os.path.abspath(path)
    return path


def fkt(var):
    print("bla " + str(var))


class MyAppEng(QQmlApplicationEngine):
    @Slot()
    def entf(self):
        global randstr
        # os.remove(tempdir + os.sep + randstr + ".html")

    def __init__(self):
        super().__init__()
        self.rootContext().setContextProperty("MyAppEng", self)


def start():
    global randstr
    app = QGuiApplication(sys.argv)
    engine = MyAppEng()
    engine.rootContext().setContextProperty("MyAppEng", engine)
    app.setWindowIcon(QIcon(":/Jupiter.png"))
    #print(":"+os.fspath(Path(__file__).resolve().parent / "Jupiter.png"))
    #app.setWindowIcon(QIcon("/"+os.fspath(Path(__file__).resolve().parent / "Jupiter.png")))
    # comp = b""
    # with open('/home/alex/religionen.html', "rb") as f:
    #    lines += f.read()
    # comp = zstd.compress(lines, 5, multiprocessing.cpu_count())
    # with open("/home/alex/comp.html.zstd", "wb") as f:
    #    f.write(comp)
    #
    # with open("/home/alex/comp.html.zstd", "rb") as f:
    #    comp += f.read()
    # base = binascii.b2a_base64(comp)
    # with open("/home/alex/base.txt", "wb") as f:
    #    f.write(base)
    ##comp = binascii.a2b_base64(base)
    # print(str(base))
    # decomp = zstd.decompress(binascii.a2b_base64(base))
    # for i in range(0, 13):
    #    randstr += random.choice(string.ascii_letters)
    # with open(tempdir + os.sep + randstr + ".html", "wb") as f:
    #    f.write(decomp)
    engine.load(os.fspath(Path(__file__).resolve().parent / "main.qml"))
    w = engine.rootObjects()[0].children()[1]
    # w.setProperty("url", "file://"+tempdir+"/"+randstr+".html")
    path_regex = re.compile(
        r'^[a-zA-Z]:\\(?:[^\\/:*?"<>|\r\n]+\\)*[^\\/:*?"<>|\r\n]*$|^/([^/\0]+(/[^/\0]+)*)?$'
    )
    pfad = ""
    browser_path = "file:///home/alex/religionen.html?preselect=no_universal"
    for path in sys.argv[1:]:
        if path_regex.match(path):
            pfad = path
    if pfad != "":
        windows_path_regex = re.compile(
            r'^[a-zA-Z]:\\(?:[^\\/:*?"<>|\r\n]+\\)*[^\\/:*?"<>|\r\n]*$'
        )
        linux_path_regex = re.compile(r"^/.*$")
        if windows_path_regex.match(pfad):
            browser_path = windows_to_browser_path(pfad)
        elif linux_path_regex.match(pfad):
            browser_path = linux_to_browser_path(pfad)
    w.setProperty("url", browser_path)
    if not engine.rootObjects():
        sys.exit(-1)
    if "-tray" in sys.argv:
        engine.rootObjects()[0].setVisible(False)
    else:
        print("possible parameters: -tray")
    # icon = QIcon("Jupiter.png")
    # tray = QSystemTrayIcon()
    # tray.setIcon(icon)
    # tray.setVisible(True)

    onexi = app.exec()
    # try:
    #    os.remove(tempdir + os.sep + randstr + ".html")
    # except:
    #    pass
    sys.exit(onexi)


if __name__ == "__main__":
    start()
