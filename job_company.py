from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog
from job_db import addCompany, editCompany, selectCompany

class Company(QMainWindow):
    def __init__(self, parent, edit=True):
        from ui.comany import Ui_MainWindow
        QMainWindow.__init__(self)
        self.py = Ui_MainWindow()
        self.py.setupUi(self)
        self.parent = parent
        self.edit = edit

        if not(edit):
            self.py.nameCompany.setText(self.parent.py.comboBox.itemText(self.parent.py.comboBox.currentIndex()))

        self.py.Okey.clicked.connect(self.saveCompany)

    def saveCompany(self):
        status = self.parent.py.comboBox.itemData(self.parent.py.comboBox.currentIndex())
        if self.edit:
            otvet = addCompany([self.py.nameCompany.text()])
        else:
            otvet = editCompany([self.py.nameCompany.text(), status])
        QMessageBox.question(self, 'Cообщение', otvet, QMessageBox.Yes)
        self.parent.py.comboBox.clear()
        for i in selectCompany():
            self.parent.py.comboBox.addItem(i[1], i[0])
        self.close()