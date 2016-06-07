# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'people.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(390, 162)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Okey = QtWidgets.QPushButton(self.centralwidget)
        self.Okey.setObjectName("Okey")
        self.gridLayout.addWidget(self.Okey, 3, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.editCompany = QtWidgets.QPushButton(self.centralwidget)
        self.editCompany.setObjectName("editCompany")
        self.gridLayout.addWidget(self.editCompany, 3, 2, 1, 1)
        self.addCompany = QtWidgets.QPushButton(self.centralwidget)
        self.addCompany.setObjectName("addCompany")
        self.gridLayout.addWidget(self.addCompany, 3, 0, 1, 2)
        self.fio = QtWidgets.QLineEdit(self.centralwidget)
        self.fio.setObjectName("fio")
        self.gridLayout.addWidget(self.fio, 0, 1, 1, 3)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 3)
        self.email = QtWidgets.QLineEdit(self.centralwidget)
        self.email.setObjectName("email")
        self.gridLayout.addWidget(self.email, 2, 1, 1, 3)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Okey.setText(_translate("MainWindow", "ОК"))
        self.label_3.setText(_translate("MainWindow", "Email"))
        self.label_2.setText(_translate("MainWindow", "Компания"))
        self.label.setText(_translate("MainWindow", "ФИО"))
        self.editCompany.setText(_translate("MainWindow", "Изменить компанию"))
        self.addCompany.setText(_translate("MainWindow", "Добавить компанию"))

