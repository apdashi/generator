#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tabModel
from job_db import connDB, tableDB, delDB, lProject, sProject, dProject, selectProject
from ui.form import Ui_MainWindow
from generate import saveDoc
from PyQt5.QtCore import Qt
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialogButtonBox, QMessageBox, QFileDialog


class startGen(QMainWindow):
    """" формирование окна """
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.py = Ui_MainWindow()
        self.py.setupUi(self)

        """ combobox"""
        self.py.buttonBox.button(QDialogButtonBox.Close).clicked.connect(lambda: self.close())
        self.py.buttonBox.button(QDialogButtonBox.Save).clicked.connect(self.docSave)

        """ клик на таблицу"""
        self.py.tableView.doubleClicked.connect(self.twoClick)

        """ кнопки действия с таблицей"""
        self.py.addPeople.clicked.connect(lambda: self.addPeople(False))
        self.py.editPeople.clicked.connect(lambda: self.addPeople(True))
        self.py.delPeople.clicked.connect(self.delPeople)
        self.py.upTable.clicked.connect(lambda: self.tableFill())

        """ работа с проектом"""
        self.py.newProject.clicked.connect(lambda: self.newProject(False))
        self.py.editProject.clicked.connect(lambda: self.newProject(True))
        self.py.saveProject.clicked.connect(self.saveProject)
        self.py.loadProject.clicked.connect(self.loadProject)
        self.py.deleteProject.clicked.connect(self.deleteProject)

        """ проверка связи при запуске"""
        if not(connDB()):
            QMessageBox.question(self, 'Cообщение', 'Проблемы с БД', QMessageBox.Yes)
        table = selectProject()
        if table is not None:
            for i in table:
                self.py.nameProject.addItem(i[1], i[0])
        self.tableFill()

    def addPeople(self, edit):
        """ добавление и изменение сотрудника"""
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

    def delPeople(self):
        """" удаление сотрудников"""
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

    def twoClick(self, index):
        """" смена checkbox  при двойном клике"""
        model = index.model()
        model.setData(index, not(model.cached[index.row()][index.column()]))

    def docSave(self):
        """ сохранение документа """
        saveFileDialog = QFileDialog.getSaveFileName(filter = "*.docx")
        doc = saveDoc(self, self.py)
        saveStr = saveFileDialog[0]
        if saveStr[-5:] == ".docx":
            doc.save(saveStr)
        else:
            doc.save(saveStr+".docx")

    def tableFill(self, inTable=None):
        """" Создание таблицы с людьми"""
        shapka = ['Ответственные', 'Публикация', 'Отчет', 'Код', 'Сотрудник', 'Компания', 'email', 'Код компании']
        table =[]
        for i in tableDB():
            if inTable is not None:
                saveCon = inTable.get(i[0])
                if saveCon is not None:
                    table.append([saveCon[0], saveCon[1], saveCon[2], i[0], i[1], i[2], i[3], i[4], i[5]])
                else:
                    table.append([False, False, False, i[0], i[1], i[2], i[3], i[4], i[5]])
            else:
                table.append([False, False, False, i[0], i[1], i[2], i[3], i[4], i[5]])
        self.model_tab = tabModel.MyTableModel(table, shapka, self.py.tableView)
        self.py.tableView.setModel(self.model_tab)

        self.py.tableView.hideColumn(3)
        self.py.tableView.hideColumn(7)
        self.py.tableView.hideColumn(8)
        self.py.tableView.setColumnWidth(0, 100)
        self.py.tableView.setColumnWidth(1, 100)
        self.py.tableView.setColumnWidth(2, 100)
        self.py.tableView.setColumnWidth(4, 200)
        self.py.tableView.setColumnWidth(5, 200)
        self.py.tableView.setColumnWidth(6, 200)



    def newProject(self, edit):
        from job_project import Project
        self.project = Project(self, edit)
        self.project.setWindowModality(Qt.ApplicationModal)
        self.project.show()

    def saveProject(self):
        saveSet = {}
        model = self.py.tableView.model()
        for i in model.cached:
            if True in i[0:3]:
                saveSet[i[3]] = i[0:3]
        self.id = self.py.nameProject.itemData(self.py.nameProject.currentIndex())
        listSave = (self.py.app1.text(), self.py.app2.text(), self.py.app3.text(), self.py.app4.text(),
                    self.py.ipAddress1.text(), self.py.ipAddress2.text(), self.py.ipAddress3.text(),
                    self.py.ipAddress4.text(), self.py.vamish1.text(), self.py.vamish2.text(),
                    self.py.vamish3.text(), self.py.vamish4.text(), self.py.portApp.text(), self.py.svn.text(),
                    self.py.test1.text(), self.py.test2.text(), self.py.test3.text(), self.py.test4.text(),
                    self.py.cache.checkState(), self.py.comandCache.text(), str(saveSet), self.id)
        if sProject(listSave):
            QMessageBox.question(self, 'Cообщение', 'Проект сохранен', QMessageBox.Yes)
        else:
            QMessageBox.question(self, 'Cообщение', 'ошибка сохранения проекта', QMessageBox.Yes)



    def loadProject(self):
        self.id = self.py.nameProject.itemData(self.py.nameProject.currentIndex())
        table = lProject(self.id)
        if table is not None and table != []:
            tb = table[0]
            self.py.app1.setText(tb[2])
            self.py.app2.setText(tb[3])
            self.py.app3.setText(tb[4])
            self.py.app4.setText(tb[5])
            self.py.ipAddress1.setText(tb[6])
            self.py.ipAddress2.setText(tb[7])
            self.py.ipAddress3.setText(tb[8])
            self.py.ipAddress4.setText(tb[9])
            self.py.vamish1.setText(tb[10])
            self.py.vamish2.setText(tb[11])
            self.py.vamish3.setText(tb[12])
            self.py.vamish4.setText(tb[13])
            self.py.portApp.setText(tb[14])
            self.py.svn.setText(tb[15])
            self.py.test1.setText(tb[16])
            self.py.test2.setText(tb[17])
            self.py.test3.setText(tb[18])
            self.py.test4.setText(tb[19])
            self.py.cache.setCheckState(tb[20])
            self.py.comandCache.setText(tb[21])
            self.tableFill(eval(tb[22]))



    def deleteProject(self):
        self.id = self.py.nameProject.itemData(self.py.nameProject.currentIndex())
        if dProject(self.id):
            QMessageBox.question(self, 'Cообщение', 'Проект удален', QMessageBox.Yes)
            table = selectProject()
            self.py.nameProject.clear()
            if table is not None:
                for i in table:
                    self.py.nameProject.addItem(i[1], i[0])
        else:
            QMessageBox.question(self, 'Cообщение', 'Ошибка удаления проекта', QMessageBox.Yes)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startGen()
    window.show()
    sys.exit(app.exec_())

