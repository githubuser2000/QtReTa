#!/usr/bin/env python3.10
# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide6.QtGui import QGuiApplication, QIcon
from PySide6.QtWidgets import QSystemTrayIcon
from PySide6.QtCore import QObject, Slot
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWebEngineWidgets import QWebEngineView
import zstd
import multiprocessing
import random
import string
import os
#from pathlib import Path
#home = str(Path.home())
import tempfile
tempdir = tempfile.gettempdir()
import binascii
from data import base
import ress

randstr = ""

def fkt(var):
    print("bla "+str(var))

class MyAppEng(QQmlApplicationEngine):
    @Slot()
    def entf(self):
        global randstr
        os.remove(tempdir+os.sep+randstr+".html")
    def __init__(self):
        super().__init__()
        self.rootContext().setContextProperty("MyAppEng", self)


def start():
    global randstr
    app = QGuiApplication(sys.argv)
    engine = MyAppEng()
    engine.rootContext().setContextProperty("MyAppEng", engine)
    app.setWindowIcon(QIcon("Jupiter.png"))
    # comp = b""
    #with open('/home/alex/religionen.html', "rb") as f:
    #    lines += f.read()
    #comp = zstd.compress(lines, 5, multiprocessing.cpu_count())
    #with open("/home/alex/comp.html.zstd", "wb") as f:
    #    f.write(comp)
    #
    #with open("/home/alex/comp.html.zstd", "rb") as f:
    #    comp += f.read()
    #base = binascii.b2a_base64(comp)
    #with open("/home/alex/base.txt", "wb") as f:
    #    f.write(base)
    ##comp = binascii.a2b_base64(base)
    #print(str(base))
    decomp = zstd.decompress(binascii.a2b_base64(base))
    for i in range(0, 13):
        randstr += random.choice(string.ascii_letters)
    with open(tempdir+os.sep+randstr+".html", "wb") as f:
        f.write(decomp)
    engine.load(os.fspath(Path(__file__).resolve().parent / "main.qml"))
    w = engine.rootObjects()[0].children()[1]
    w.setProperty("url", "file://"+tempdir+"/"+randstr+".html")
    if not engine.rootObjects():
        sys.exit(-1)

    #icon = QIcon("Jupiter.png")
    #tray = QSystemTrayIcon()
    #tray.setIcon(icon)
    #tray.setVisible(True)

    onexi = app.exec()
    try:
        os.remove(tempdir+os.sep+randstr+".html")
    except:
        pass
    sys.exit(onexi)

if __name__ == "__main__":
    start()
