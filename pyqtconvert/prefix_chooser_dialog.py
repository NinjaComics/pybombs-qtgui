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
        self.label_2.setGeometry(QtCore.QRect(20, 70, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(PrefixChooserDialog)
        self.comboBox.setGeometry(QtCore.QRect(20, 100, 281, 41))
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(PrefixChooserDialog)
        self.pushButton.setGeometry(QtCore.QRect(194, 177, 101, 41))
        self.pushButton.setDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(PrefixChooserDialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(PrefixChooserDialog)
        self.label_3.setGeometry(QtCore.QRect(140, 20, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.checkBox = QtWidgets.QCheckBox(PrefixChooserDialog)
        self.checkBox.setGeometry(QtCore.QRect(20, 190, 151, 26))
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(PrefixChooserDialog)
        QtCore.QMetaObject.connectSlotsByName(PrefixChooserDialog)

    def retranslateUi(self, PrefixChooserDialog):
        _translate = QtCore.QCoreApplication.translate
        PrefixChooserDialog.setWindowTitle(_translate("PrefixChooserDialog", "Dialog"))
        self.label_2.setText(_translate("PrefixChooserDialog", "Choose Prefix"))
        self.pushButton.setText(_translate("PrefixChooserDialog", "Save"))
        self.label.setText(_translate("PrefixChooserDialog", "Current Prefix :"))
        self.checkBox.setText(_translate("PrefixChooserDialog", "Write env to prefix"))

