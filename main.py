#!/usr/bin/env python3.10
# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide6.QtGui import QGuiApplication
from PySide6.QtCore import QObject
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWebEngineWidgets import QWebEngineView
import zstd
import multiprocessing
import random
import string
import os
from pathlib import Path
home = str(Path.home())

def fkt(var):
    print("bla "+str(var))


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    comp = b""
    #with open('/home/alex/religionen.html', "rb") as f:
    #    lines += f.read()
    #comp = zstd.compress(lines, 5, multiprocessing.cpu_count())
    #with open("/home/alex/comp.html.zstd", "wb") as f:
    #    f.write(comp)
    #
    with open("/home/alex/comp.html.zstd", "rb") as f:
        comp += f.read()
    decomp = zstd.decompress(comp)
    randstr = ""
    for i in range(0, 13):
        randstr += random.choice(string.ascii_letters)
    with open("/home/alex/"+randstr+".html", "wb") as f:
        f.write(decomp)
    engine.load(os.fspath(Path(__file__).resolve().parent / "main.qml"))
    w = engine.rootObjects()[0].children()[1]
    w.setProperty("url", "file://"+home+"/"+randstr+".html")
    if not engine.rootObjects():
        sys.exit(-1)
    onexi = app.exec()
    os.remove(home+os.sep+randstr+".html")
    sys.exit(onexi)
