# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'comany.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(445, 72)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.nameCompany = QtWidgets.QLineEdit(self.centralwidget)
        self.nameCompany.setObjectName("nameCompany")
        self.gridLayout.addWidget(self.nameCompany, 0, 1, 1, 1)
        self.Okey = QtWidgets.QPushButton(self.centralwidget)
        self.Okey.setObjectName("Okey")
        self.gridLayout.addWidget(self.Okey, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Наименование"))
        self.Okey.setText(_translate("MainWindow", "OK"))

