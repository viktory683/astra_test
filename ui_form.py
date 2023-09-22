# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.treeView = QTreeView(Widget)
        self.treeView.setObjectName(u"treeView")

        self.gridLayout.addWidget(self.treeView, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(Widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.checkBox = QCheckBox(Widget)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout.addWidget(self.checkBox)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"\u0424\u0430\u0439\u043b\u044b", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Widget", u"\u0424\u0438\u043b\u044c\u0442\u0440", None))
        self.checkBox.setText(QCoreApplication.translate("Widget", u"\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u0441\u043a\u0440\u044b\u0442\u044b\u0435", None))
    # retranslateUi

