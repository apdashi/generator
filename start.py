#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tabModel
from job_db import connDB, tableDB, delDB
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
        self.py.buttonBox.button(QDialogButtonBox.Close).clicked.connect(lambda: self.close())
        self.py.buttonBox.button(QDialogButtonBox.Save).clicked.connect(self.docSave)

        """ клик на таблицу"""
        self.py.tableView.doubleClicked.connect(self.twoClick)

        """ кнопки действия с таблицей"""
        self.py.addPeople.clicked.connect(lambda: self.addPeople(False))
        self.py.editPeople.clicked.connect(lambda: self.addPeople(True))
        self.py.delPeople.clicked.connect(self.delPeople)
        self.py.upTable.clicked.connect(self.tableFill)

        """ проверка связи при запуске"""
        connDB()
        self.tableFill()

    """ добавление и изменение сотрудника"""
    def addPeople(self, edit):
        from job_people import People
        if edit:
            try:
                model = self.py.tableView.model()
                index = self.py.tableView.selectedIndexes()
                index[0]
                self.people = People(self, edit)
                self.people.setWindowModality(Qt.ApplicationModal)
                self.people.show()
            except:
                QMessageBox.question(self, 'Cообщение', "Не выбран сотрудник", QMessageBox.Yes)
        else:
            self.people = People(self)
            self.people.setWindowModality(Qt.ApplicationModal)
            self.people.show()

    """" удаление сотрудников"""
    def delPeople(self):
        try:
            model = self.py.tableView.model()
            index = self.py.tableView.selectedIndexes()
            id = model.cached[index[0].row()][3]
            if delDB(id):
                otvet = "Запись удалена"
            else:
                otvet = "Что то пошло не так(запись не удалена)"
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
        doc = saveDoc(self, self.py)
        doc.save(saveFileDialog[0]+".docx")

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startGen()
    window.show()
    sys.exit(app.exec_())

