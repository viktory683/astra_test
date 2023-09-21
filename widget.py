# This Python file uses the following encoding: utf-8
import sys
from typing import Optional, Union

from PySide2.QtWidgets import QApplication, QWidget, QFileSystemModel
from PySide2.QtCore import QDir

# pyside6-uic form.ui -o ui_form.py, or
# pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent:Optional[QWidget]=None):
        print(type(parent))
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        dirModel = QFileSystemModel(self)

        dirModel.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs)

        dirModel.setRootPath("/")

        self.ui.treeView.setModel(dirModel)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec_())
