#!/usr/bin/env python3.10
# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide6.QtGui import QGuiApplication
from PySide6.QtCore import QObject
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWebEngineWidgets import QWebEngineView

def fkt(var):
    print("bla "+str(var))

class myApp(QGuiApplication):
    pass
    #def __init__():
    #    self.runJavaScript("document.documentElement.innerHTML=\"<html><head></head><body><h1>testx</h1></body></html>\";alert(\"2\"+document.documentElement.innerHTML)", fkt)
    #def exec(self):
    #    #super().exec()

if __name__ == "__main__":
    app =myApp(sys.argv)
    engine = QQmlApplicationEngine()
    engine.load(os.fspath(Path(__file__).resolve().parent / "main.qml"))
    w = engine.rootObjects()[0].children()[1]
    print(str((w.__str__())))
    print(str(dir(w)))
    #w.show()
    # w.runJavaScript("document.documentElement.innerHTML=\"<html><head></head><body><h1>testx</h1></body></html>\";alert(\"2\"+document.documentElement.innerHTML)", fkt)
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
