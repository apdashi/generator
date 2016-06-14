from PyQt5.QtWidgets import QMainWindow, QMessageBox
from job_db import nProject, editProject, selectProject
from ui.project import Ui_MainWindow

class Project(QMainWindow):
    def __init__(self, parent, edit=False):
        QMainWindow.__init__(self)
        self.py = Ui_MainWindow()
        self.py.setupUi(self)
        self.parent = parent
        self.edit = edit
        if self.edit:
            self.py.nameProject.setText(self.parent.py.nameProject.itemText(self.parent.py.nameProject.currentIndex()))

        self.py.Okey.clicked.connect(self.saveProject)

    def saveProject(self):
        if self.edit:
            status = self.parent.py.nameProject.itemData(self.parent.py.nameProject.currentIndex())
            otvet = editProject([self.py.nameProject.text(), status])
        else:
            otvet = nProject([self.py.nameProject.text()])
        if not(otvet):
            QMessageBox.question(self, 'Cообщение', 'Ошибка добавления(изменения) компании', QMessageBox.Yes)
        else:
            self.parent.py.nameProject.clear()
            for i in selectProject():
                self.parent.py.nameProject.addItem(i[1], i[0])
            self.parent.py.nameProject.setCurrentIndex(self.parent.py.nameProject.findText(self.py.nameProject.text()))
            self.close()