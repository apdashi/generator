#!/usr/bin/python3
# -*- coding: utf-8 -*-

from ui.form import Ui_MainWindow
from PyQt5 import QtGui, QtCore
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class startGen(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.py = Ui_MainWindow()
        self.py.setupUi(self)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = startGen()
    window.show()
    sys.exit(app.exec_())
