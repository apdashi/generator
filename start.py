#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tabModel
import configparser
from job_db import connDB, createDB, tableDB, delDB
from ui.form import Ui_MainWindow
from generate import saveDoc
from PyQt5.QtCore import Qt
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialogButtonBox, QMessageBox, QFileDialog

"""" формирование окна"""
class startGen(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.py = Ui_MainWindow()
        self.py.setupUi(self)

        """ combobox"""
        self.py.buttonBox.button(QDialogButtonBox.Open).clicked.connect(self.opened)
        # self.py.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(lambda: generate(self, self.py))
        self.py.buttonBox.button(QDialogButtonBox.Close).clicked.connect(lambda: self.close())
        self.py.buttonBox.button(QDialogButtonBox.Save).clicked.connect(self.docSave)

        """ кнопки конфигов"""
        self.py.saveConfig.clicked.connect(lambda: self.saveConfig())
        self.py.createDB.clicked.connect(lambda: self.create())
        self.py.checkDB.clicked.connect(lambda: self.check())

        """ клик на таблицу"""
        self.py.tableView.doubleClicked.connect(self.twoClick)

        """ кнопки действия с таблицей"""
        self.py.addPeople.clicked.connect(lambda: self.addPeople(True))
        self.py.editPeople.clicked.connect(lambda: self.addPeople(False))
        self.py.delPeople.clicked.connect(self.delPeople)
        self.py.upTable.clicked.connect(self.tableFill)

        self.conf = configparser.RawConfigParser()
        self.conf.read("config.conf")
        self.dsn = 'dbname=%s user=%s password=%s host=%s' % (self.conf.get("postgres", "dbname"),
                                                            self.conf.get("postgres", "user"),
                                                            self.conf.get("postgres", "password"),
                                                            self.conf.get("postgres", "host"))

        """ востановление настроек"""
        self.py.dbname.setText(self.conf.get("postgres", "dbname"))
        self.py.user.setText(self.conf.get("postgres", "user"))
        self.py.password.setText(self.conf.get("postgres", "password"))
        self.py.host.setText(self.conf.get("postgres", "host"))

        """ проверка связи при запуске"""
        otvet = connDB(self, self.dsn)
        if otvet != "Связь есть":
            QMessageBox.question(self, 'Cообщение', otvet, QMessageBox.Yes)
        else:
            self.tableFill()

    """ добавление и изменение сотрудника"""
    def addPeople(self, edit):
        from job_people import People
        if edit:
            self.people = People(self)
            self.people.setWindowModality(Qt.ApplicationModal)
            self.people.show()
        else:
            try:
                model = self.py.tableView.model()
                index = self.py.tableView.selectedIndexes()
                index[0]
                self.people = People(self, edit)
                self.people.setWindowModality(Qt.ApplicationModal)
                self.people.show()
            except:
                QMessageBox.question(self, 'Cообщение', "Не выбран сотрудник", QMessageBox.Yes)

    """" удаление сотрудников"""
    def delPeople(self):
        model = self.py.tableView.model()
        index = self.py.tableView.selectedIndexes()
        try:
            id = model.cached[index[0].row()][3]
            otvet = delDB(id)
        except:
            otvet = "Не выбран сотрудник"
        QMessageBox.question(self, 'Cообщение', otvet, QMessageBox.Yes)
        self.tableFill()



    """" смена checkbox  при двойном клике"""
    def twoClick(self, index):
        model = index.model()
        model.setData(index, not(model.cached[index.row()][index.column()]))

    """ сохранение документа """
    def docSave(self):
        saveFileDialog = QFileDialog.getSaveFileName(filter = "*.docx")
        print(saveFileDialog)
        doc = saveDoc(self, self.py)
        doc.save(saveFileDialog[0]+".docx")

    """ проверка связи с БД"""
    def check(self):
        self.dsn = 'dbname=%s user=%s password=%s host=%s' % (self.py.dbname.text(), self.py.user.text(),
                                                              self.py.password.text(), self.py.host.text())
        QMessageBox.question(self, 'Cообщение', connDB(self, self.dsn), QMessageBox.Yes)

    """ создание БД"""
    def create(self):
        QMessageBox.question(self, 'Cообщение', createDB(self), QMessageBox.Yes)

    """" Загрузка настроек пока не реализовано"""
    def opened(self):
        print(4)

    """" Создание таблицы с людьми"""
    def tableFill(self):
        shapka = ['Ответственные', 'Публикация', 'Отчет', 'Код', 'Сотрудник', 'Компания', 'email', 'Код компании']
        table =[]
        for i in tableDB():
            table.append([False, False, False, i[0], i[1], i[2], i[3], i[4]])
        self.model_tab = tabModel.MyTableModel(table, shapka, self.py.tableView)
        self.py.tableView.setModel(self.model_tab)

        self.py.tableView.hideColumn(3)
        self.py.tableView.hideColumn(7)
        self.py.tableView.setColumnWidth(0, 100)
        self.py.tableView.setColumnWidth(1, 100)
        self.py.tableView.setColumnWidth(2, 100)
        self.py.tableView.setColumnWidth(4, 200)
        self.py.tableView.setColumnWidth(5, 200)
        self.py.tableView.setColumnWidth(6, 200)

    """" сохранение настроек """
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

