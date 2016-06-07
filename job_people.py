from PyQt5.QtWidgets import QMainWindow, QMessageBox
from job_db import selectCompany, addPeople, editPeople
from PyQt5.QtCore import Qt
from ui.people import Ui_MainWindow
from job_company import Company

class People(QMainWindow):
    def __init__(self, parent, edit=False):
        QMainWindow.__init__(self)
        self.py = Ui_MainWindow()
        self.py.setupUi(self)
        self.parent = parent
        self.edit = edit
        for i in selectCompany():
            self.py.comboBox.addItem(i[1], i[0])

        if self.edit:
            model = parent.py.tableView.model()
            index = parent.py.tableView.selectedIndexes()
            self.id = model.cached[index[0].row()][3]
            self.py.fio.setText(model.cached[index[0].row()][4])
            self.py.comboBox.setCurrentIndex(self.py.comboBox.findData(model.cached[index[0].row()][7]))
            self.py.email.setText(model.cached[index[0].row()][6])

        self.py.Okey.clicked.connect(self.savePeople)
        self.py.addCompany.clicked.connect(lambda: self.upCompany(False))
        self.py.editCompany.clicked.connect(lambda: self.upCompany(True))

    def savePeople(self):
        status = self.py.comboBox.itemData(self.py.comboBox.currentIndex())
        if self.py.fio.text() == '' or self.py.email.text() == '':
            QMessageBox.question(self, 'Cообщение', "Не все параметры заполнены", QMessageBox.Yes)
        else:
            if self.edit:
                otvet = editPeople([self.py.fio.text(), status, self.py.email.text(), self.id])
            else:
                otvet = addPeople([self.py.fio.text(), status, self.py.email.text()])
            if otvet:
                QMessageBox.question(self, 'Cообщение', 'Добавление(изменение) сотрудника прошло успешно',
                                     QMessageBox.Yes)
            else:
                QMessageBox.question(self, 'Cообщение', 'Ошибка добавления(изменения) сотруника', QMessageBox.Yes)
            self.parent.tableFill()
            self.close()

    def upCompany(self, edit):
        self.company = Company(self, edit)
        self.company.setWindowModality(Qt.ApplicationModal)
        self.company.show()

