# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search_opt.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SearchDialog(object):
    def setupUi(self, SearchDialog):
        SearchDialog.setObjectName("SearchDialog")
        SearchDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        SearchDialog.resize(370, 256)
        self.label = QtWidgets.QLabel(SearchDialog)
        self.label.setGeometry(QtCore.QRect(50, 40, 66, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(SearchDialog)
        self.lineEdit.setGeometry(QtCore.QRect(140, 30, 191, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(SearchDialog)
        self.pushButton.setGeometry(QtCore.QRect(140, 197, 93, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(SearchDialog)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 197, 93, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/circle3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox = QtWidgets.QComboBox(SearchDialog)
        self.comboBox.setGeometry(QtCore.QRect(140, 120, 191, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(SearchDialog)
        self.label_2.setGeometry(QtCore.QRect(50, 130, 66, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(SearchDialog)
        QtCore.QMetaObject.connectSlotsByName(SearchDialog)

    def retranslateUi(self, SearchDialog):
        _translate = QtCore.QCoreApplication.translate
        SearchDialog.setWindowTitle(_translate("SearchDialog", "Dialog"))
        self.label.setText(_translate("SearchDialog", "Search "))
        self.pushButton.setText(_translate("SearchDialog", "Cancel"))
        self.pushButton_2.setText(_translate("SearchDialog", "Search"))
        self.comboBox.setItemText(0, _translate("SearchDialog", "Name"))
        self.comboBox.setItemText(1, _translate("SearchDialog", "Version"))
        self.comboBox.setItemText(2, _translate("SearchDialog", "Description"))
        self.comboBox.setItemText(3, _translate("SearchDialog", "Installed"))
        self.label_2.setText(_translate("SearchDialog", "Look in:"))

