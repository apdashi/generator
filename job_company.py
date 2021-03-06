from PyQt5.QtWidgets import QMainWindow, QMessageBox
from job_db import addCompany, editCompany, selectCompany
from ui.company import Ui_MainWindow

class Company(QMainWindow):
    def __init__(self, parent, edit=False):
        QMainWindow.__init__(self)
        self.py = Ui_MainWindow()
        self.py.setupUi(self)
        self.parent = parent
        self.edit = edit
        if self.edit:
            model = self.parent.parent.py.tableView.model()
            index = self.parent.parent.py.tableView.selectedIndexes()
            self.py.nameCompany.setText(self.parent.py.comboBox.itemText(self.parent.py.comboBox.currentIndex()))
            self.py.priority.setText(str(model.cached[index[0].row()][8]))
        else:
            self.py.priority.setText(str(9))

        self.py.Okey.clicked.connect(self.saveCompany)

    def saveCompany(self):
        prio = self.py.priority.text()
        if self.edit:
            status = self.parent.py.comboBox.itemData(self.parent.py.comboBox.currentIndex())
            otvet = editCompany([self.py.nameCompany.text(), prio, status])
        else:
            otvet = addCompany([self.py.nameCompany.text(), prio])
        if otvet:
            QMessageBox.question(self, 'Cообщение', 'Добавление(изменение) компании прошло успешно', QMessageBox.Yes)
        else:
            QMessageBox.question(self, 'Cообщение', 'Ошибка добавления(изменения) компании', QMessageBox.Yes)
        self.parent.py.comboBox.clear()
        for i in selectCompany():
            self.parent.py.comboBox.addItem(i[1], i[0])
        self.parent.py.comboBox.setCurrentIndex(self.parent.py.comboBox.findText(self.py.nameCompany.text()))
        model = self.parent.parent.py.tableView.model()
        index = self.parent.parent.py.tableView.selectedIndexes()
        self.close()