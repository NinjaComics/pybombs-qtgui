# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/initial_config.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_InitialConfigDialog(object):
    def setupUi(self, InitialConfigDialog):
        InitialConfigDialog.setObjectName("InitialConfigDialog")
        InitialConfigDialog.resize(600, 158)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        InitialConfigDialog.setFont(font)
        InitialConfigDialog.setAcceptDrops(False)
        self.buttonBox = QtWidgets.QDialogButtonBox(InitialConfigDialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 440, 621, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(InitialConfigDialog)
        self.label.setGeometry(QtCore.QRect(60, 10, 471, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(InitialConfigDialog)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 100, 131, 41))
        self.pushButton_2.setAutoFillBackground(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/circle3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(InitialConfigDialog)
        self.buttonBox.accepted.connect(InitialConfigDialog.accept)
        self.buttonBox.rejected.connect(InitialConfigDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(InitialConfigDialog)

    def retranslateUi(self, InitialConfigDialog):
        _translate = QtCore.QCoreApplication.translate
        InitialConfigDialog.setWindowTitle(_translate("InitialConfigDialog", "Run Config"))
        self.label.setText(_translate("InitialConfigDialog", "Pybombs could not find any recipes. Click \"Run Config\" to add recipes and setup a prefix"))
        self.pushButton_2.setText(_translate("InitialConfigDialog", "Run Config"))

