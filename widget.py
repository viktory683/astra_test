import sys
import pathlib

from PySide2.QtWidgets import QApplication, QWidget, QFileSystemModel
from PySide2.QtCore import QDir, QSortFilterProxyModel, QRegExp, Qt

# pyside6-uic form.ui -o ui_form.py, or
# pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class FilterProxyModel(QSortFilterProxyModel):
    def lessThan(self, left_index, right_index):
        left_data = left_index.data(Qt.DisplayRole)
        right_data = right_index.data(Qt.DisplayRole)

        left_is_dir = self.sourceModel().isDir(left_index)
        right_is_dir = self.sourceModel().isDir(right_index)

        if left_is_dir and not right_is_dir:
            return True
        elif not left_is_dir and right_is_dir:
            return False
        return left_data < right_data


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.__filter_states = {
            "default": QDir.NoDotAndDotDot | QDir.AllEntries,
            "hidden": QDir.NoDotAndDotDot | QDir.AllEntries | QDir.Hidden
        }

        dirModel = QFileSystemModel(self)

        dirModel.setFilter(self.__filter_states["default"])

        dirModel.setRootPath("/")
        self.dirModel = dirModel

        self.proxy_model = FilterProxyModel(self)
        self.proxy_model.setSourceModel(self.dirModel)
        self.proxy_model.setRecursiveFilteringEnabled(True)  # Enable recursive filtering
        self.ui.treeView.setModel(self.proxy_model)
        self.ui.treeView.setRootIndex(self.proxy_model.mapFromSource(dirModel.index(str(pathlib.Path.home()))))
        self.ui.treeView.setSortingEnabled(True)

        self.ui.checkBox.stateChanged.connect(self.toggle_hidden)

        self.ui.lineEdit.textChanged.connect(self.filter_tree)

    def toggle_hidden(self, state):
        self.dirModel.setFilter(self.__filter_states[{0: "default", 2: "hidden"}[state]])

    def filter_tree(self, text):
        self.proxy_model.setFilterRegExp(QRegExp(text, Qt.CaseInsensitive))

        source_index = self.proxy_model.mapToSource(self.ui.treeView.rootIndex())
        index_item = self.dirModel.index(source_index.row(), 0, source_index.parent())
        file_path = self.dirModel.filePath(index_item)
        
        # TODO костыль! - убрать
        self.__new_root = file_path
        if not self.__new_root:
            self.ui.treeView.setRootIndex(self.proxy_model.mapFromSource(self.dirModel.index(self.__current_root)))
        else:
            self.__current_root = self.__new_root


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec_())
