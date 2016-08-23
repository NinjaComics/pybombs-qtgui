# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/info_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_InfoDialog(object):
    def setupUi(self, InfoDialog):
        InfoDialog.setObjectName("InfoDialog")
        InfoDialog.resize(320, 240)
        self.pushButton = QtWidgets.QPushButton(InfoDialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 180, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(InfoDialog)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 180, 101, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(InfoDialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 281, 131))
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        self.retranslateUi(InfoDialog)
        QtCore.QMetaObject.connectSlotsByName(InfoDialog)

    def retranslateUi(self, InfoDialog):
        _translate = QtCore.QCoreApplication.translate
        InfoDialog.setWindowTitle(_translate("InfoDialog", "Dialog"))
        self.pushButton.setText(_translate("InfoDialog", "Check Logs"))
        self.pushButton_2.setText(_translate("InfoDialog", "Ok"))

