#!/usr/bin/python3
# -*- coding: utf-8 -*-

from ui.form import Ui_MainWindow
from generate import generate
from PyQt5 import QtGui, QtCore
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialogButtonBox

class startGen(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.py = Ui_MainWindow()
        self.py.setupUi(self)
        self.py.buttonBox.button(QDialogButtonBox.Open).clicked.connect(self.opened)
        self.py.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(lambda: generate(self, self.py))
        self.py.buttonBox.button(QDialogButtonBox.Close).clicked.connect(self.closeApp)
        self.py.buttonBox.button(QDialogButtonBox.Save).clicked.connect(self.saved)

    def closeApp(self):
        self.close()

    def saved(self):
        print(3)

    def opened(self):
        print(4)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startGen()
    window.show()
    sys.exit(app.exec_())
