# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/loading.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoadingDialog(object):
    def setupUi(self, LoadingDialog):
        LoadingDialog.setObjectName("LoadingDialog")
        LoadingDialog.resize(320, 220)
        self.label = QtWidgets.QLabel(LoadingDialog)
        self.label.setGeometry(QtCore.QRect(0, -20, 321, 251))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/noprefix/images/loading.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(LoadingDialog)
        self.label_2.setGeometry(QtCore.QRect(0, 160, 321, 41))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 11pt \"Ubuntu\";")
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(LoadingDialog)
        QtCore.QMetaObject.connectSlotsByName(LoadingDialog)

    def retranslateUi(self, LoadingDialog):
        _translate = QtCore.QCoreApplication.translate
        LoadingDialog.setWindowTitle(_translate("LoadingDialog", "Dialog"))

import myicons_rc
