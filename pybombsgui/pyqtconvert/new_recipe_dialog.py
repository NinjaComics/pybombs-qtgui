# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/new_recipe.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NewRecipeDialog(object):
    def setupUi(self, NewRecipeDialog):
        NewRecipeDialog.setObjectName("NewRecipeDialog")
        NewRecipeDialog.resize(500, 480)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(NewRecipeDialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 41, 500, 371))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(NewRecipeDialog)
        self.pushButton.setGeometry(QtCore.QRect(530, 410, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(NewRecipeDialog)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 502, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(52, 101, 164);")
        self.label_4.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(NewRecipeDialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 430, 361, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(NewRecipeDialog)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 430, 101, 41))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(NewRecipeDialog)
        QtCore.QMetaObject.connectSlotsByName(NewRecipeDialog)

    def retranslateUi(self, NewRecipeDialog):
        _translate = QtCore.QCoreApplication.translate
        NewRecipeDialog.setWindowTitle(_translate("NewRecipeDialog", "Add new recipe"))
        self.plainTextEdit.setPlainText(_translate("NewRecipeDialog", "# This is a template for private recipes. \n"
"# To add this recipe to the list of recipes, \n"
"# load the recipe location from the recipe manager\n"
"\n"
"depends:\n"
"category: common\n"
"satisfy:\n"
"source:\n"
"vars:\n"
"inherit: cmake\n"
"configure_static: \n"
"install: \n"
"description: "))
        self.pushButton.setText(_translate("NewRecipeDialog", "Save recipe"))
        self.label_4.setText(_translate("NewRecipeDialog", "This recipe will be added to the active prefix"))
        self.pushButton_2.setText(_translate("NewRecipeDialog", "Save Recipe"))

