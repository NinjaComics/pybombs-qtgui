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
        NewRecipeDialog.resize(640, 480)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(NewRecipeDialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 641, 371))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(NewRecipeDialog)
        self.pushButton.setGeometry(QtCore.QRect(530, 410, 101, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(NewRecipeDialog)
        QtCore.QMetaObject.connectSlotsByName(NewRecipeDialog)

    def retranslateUi(self, NewRecipeDialog):
        _translate = QtCore.QCoreApplication.translate
        NewRecipeDialog.setWindowTitle(_translate("NewRecipeDialog", "Dialog"))
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

