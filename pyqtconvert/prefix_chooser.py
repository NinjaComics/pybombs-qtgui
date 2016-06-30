# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/prefix_chooser.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PrefixChooserDialog(object):
    def setupUi(self, PrefixChooserDialog):
        PrefixChooserDialog.setObjectName("PrefixChooserDialog")
        PrefixChooserDialog.resize(320, 240)
        self.label_2 = QtWidgets.QLabel(PrefixChooserDialog)
        self.label_2.setGeometry(QtCore.QRect(100, 40, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(PrefixChooserDialog)
        self.comboBox.setGeometry(QtCore.QRect(20, 80, 281, 41))
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(PrefixChooserDialog)
        self.pushButton.setGeometry(QtCore.QRect(194, 177, 101, 41))
        self.pushButton.setDefault(True)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(PrefixChooserDialog)
        QtCore.QMetaObject.connectSlotsByName(PrefixChooserDialog)

    def retranslateUi(self, PrefixChooserDialog):
        _translate = QtCore.QCoreApplication.translate
        PrefixChooserDialog.setWindowTitle(_translate("PrefixChooserDialog", "Dialog"))
        self.label_2.setText(_translate("PrefixChooserDialog", "Choose Prefix"))
        self.pushButton.setText(_translate("PrefixChooserDialog", "Save"))

