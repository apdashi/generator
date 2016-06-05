#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tabModel
import configparser
from job_db import connDB, createDB, tableDB
from ui.form import Ui_MainWindow
from generate import generate, saveDoc
from PyQt5.QtCore import Qt
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialogButtonBox, QMessageBox

class startGen(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.py = Ui_MainWindow()
        self.py.setupUi(self)
        self.py.buttonBox.button(QDialogButtonBox.Open).clicked.connect(self.opened)
        self.py.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(lambda: generate(self, self.py))
        self.py.buttonBox.button(QDialogButtonBox.Close).clicked.connect(self.closeApp)
        self.py.buttonBox.button(QDialogButtonBox.Save).clicked.connect(lambda: saveDoc(self, self.py))

        self.py.saveConfig.clicked.connect(lambda: self.saveConfig())
        self.py.createDB.clicked.connect(lambda: self.create())
        self.py.checkDB.clicked.connect(lambda: self.check())

        self.conf = configparser.RawConfigParser()
        self.conf.read("config.conf")
        self.dsn = 'dbname=%s user=%s password=%s host=%s' % (self.conf.get("postgres", "dbname"),
                                                            self.conf.get("postgres", "user"),
                                                            self.conf.get("postgres", "password"),
                                                            self.conf.get("postgres", "host"))
        self.py.dbname.setText(self.conf.get("postgres", "dbname"))
        self.py.user.setText(self.conf.get("postgres", "user"))
        self.py.password.setText(self.conf.get("postgres", "password"))
        self.py.host.setText(self.conf.get("postgres", "host"))
        otvet = connDB(self, self.dsn)
        if otvet != "Связь есть":
            QMessageBox.question(self, 'Cообщение', otvet, QMessageBox.Yes)
        else:
            self.tableFill()


    def check(self):
        self.dsn = 'dbname=%s user=%s password=%s host=%s' % (self.py.dbname.text(), self.py.user.text(),
                                                              self.py.password.text(), self.py.host.text())
        QMessageBox.question(self, 'Cообщение', connDB(self, self.dsn), QMessageBox.Yes)

    def create(self):
        QMessageBox.question(self, 'Cообщение', createDB(self), QMessageBox.Yes)

    def closeApp(self):
        self.close()

    def saved(self):
        print(3)

    def opened(self):
        print(4)

    def tableFill(self):
        shapka = ['Ответственные', 'Публикация', 'Отчет', 'Код', 'Сотрудник', 'Компания', 'email']
        table =[]
        for i in tableDB():
            print(i)
            table.append([False, False, False, i[0], i[1], i[2], i[3]])
        self.model_tab = tabModel.MyTableModel( table, shapka, self.py.tableView)
        self.py.tableView.setModel(self.model_tab)

        self.py.tableView.hideColumn(3)
        self.py.tableView.setColumnWidth(0, 100)
        self.py.tableView.setColumnWidth(1, 100)
        self.py.tableView.setColumnWidth(2, 100)
        self.py.tableView.setColumnWidth(4, 200)
        self.py.tableView.setColumnWidth(5, 200)
        self.py.tableView.setColumnWidth(6, 200)


    def saveConfig(self):
        try:
            self.conf.add_section('postgres')
        except:
            pass
        self.conf.set('postgres', 'host', self.py.host.text())
        self.conf.set('postgres', 'user', self.py.user.text())
        self.conf.set('postgres', 'password', self.py.password.text())
        self.conf.set('postgres', 'dbname', self.py.dbname.text())
        self.conf.write(open('config.conf', 'w'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startGen()
    window.show()
    sys.exit(app.exec_())

