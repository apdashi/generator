from PyQt5 import QtCore


""" Модуль отвечающий за таблицу"""
class MyTableModel(QtCore.QAbstractTableModel):
    def __init__(self, datain, headerdata, parent=None, *args):
        """ datain: a list of lists
            headerdata: a list of strings
        """
        QtCore.QAbstractTableModel.__init__(self, parent, *args)
        self.cached = datain
        self.colLabels = headerdata

    def rowCount(self, parent):
        return len(self.cached)

    def columnCount(self, parent):
        return len(self.colLabels)

    def data(self, index, role):
        if role == QtCore.Qt.CheckStateRole and index.column() in [0, 1, 2]:
            if self.cached[index.row()][index.column()] == False:
                return QtCore.QVariant(QtCore.Qt.Unchecked)
            else:
                return QtCore.QVariant(QtCore.Qt.Checked)
        if not index.isValid():
            return QtCore.QVariant()
        elif role != QtCore.Qt.DisplayRole and role != QtCore.Qt.EditRole:
            return QtCore.QVariant()
        value = ''
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            col = index.column()
            value = self.cached[row][col]
        elif role == QtCore.Qt.EditRole:
            row = index.row()
            col = index.column()
            value = self.cached[row][col]
        return QtCore.QVariant(value)

    def flags(self, index):
        if not index.isValid():
            return QtCore.Qt.ItemIsEnabled
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable

    def setData(self, index, value, role = None):
        if (index.isValid() and role == QtCore.Qt.EditRole) or (index.column() in [0,1,2]):
            self.cached[index.row()][index.column()] = value
            # self.emit(QtCore.SIGNAL("dataChanged(QModelIndex, QModelIndex)"), index, index)
            return True
        else:
            return False

    def headerData(self, section, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return QtCore.QVariant(self.colLabels[section])
        return QtCore.QVariant()

    def value_date(self, index):
        row = index.row()
        col = index.column()
        value = self.arraydata[row][col]
        return value