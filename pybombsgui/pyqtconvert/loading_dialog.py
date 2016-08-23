# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/loading.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoadingDialog(object):
    def setupUi(self, LoadingDialog):
        LoadingDialog.setObjectName("LoadingDialog")
        LoadingDialog.resize(622, 200)
        self.label = QtWidgets.QLabel(LoadingDialog)
        self.label.setGeometry(QtCore.QRect(-10, -10, 641, 230))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/noprefix/images/loading.png"))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(LoadingDialog)
        self.label_3.setGeometry(QtCore.QRect(150, 100, 481, 51))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"Ubuntu\";")
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(LoadingDialog)
        QtCore.QMetaObject.connectSlotsByName(LoadingDialog)

    def retranslateUi(self, LoadingDialog):
        _translate = QtCore.QCoreApplication.translate
        LoadingDialog.setWindowTitle(_translate("LoadingDialog", "Dialog"))

import myicons_rc
