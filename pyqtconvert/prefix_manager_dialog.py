# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/prefix_config.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PrefixConfigDialog(object):
    def setupUi(self, PrefixConfigDialog):
        PrefixConfigDialog.setObjectName("PrefixConfigDialog")
        PrefixConfigDialog.resize(560, 311)
        self.label_3 = QtWidgets.QLabel(PrefixConfigDialog)
        self.label_3.setGeometry(QtCore.QRect(40, 170, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(PrefixConfigDialog)
        self.lineEdit.setGeometry(QtCore.QRect(190, 170, 301, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(PrefixConfigDialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 90, 301, 41))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(PrefixConfigDialog)
        self.label_5.setGeometry(QtCore.QRect(40, 90, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(PrefixConfigDialog)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 561, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 105, 5);")
        self.label_4.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(PrefixConfigDialog)
        self.pushButton.setGeometry(QtCore.QRect(424, 247, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(PrefixConfigDialog)
        self.checkBox.setGeometry(QtCore.QRect(240, 260, 161, 26))
        self.checkBox.setObjectName("checkBox")
        self.pushButton_2 = QtWidgets.QPushButton(PrefixConfigDialog)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 170, 41, 41))
        self.pushButton_2.setText("")
        icon = QtGui.QIcon.fromTheme("document-open")
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(28, 28))
        self.pushButton_2.setAutoDefault(True)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(PrefixConfigDialog)
        QtCore.QMetaObject.connectSlotsByName(PrefixConfigDialog)

    def retranslateUi(self, PrefixConfigDialog):
        _translate = QtCore.QCoreApplication.translate
        PrefixConfigDialog.setWindowTitle(_translate("PrefixConfigDialog", "Prefix Manager"))
        self.label_3.setText(_translate("PrefixConfigDialog", "Prefix Directory"))
        self.label_5.setText(_translate("PrefixConfigDialog", "Prefix Alias"))
        self.label_4.setText(_translate("PrefixConfigDialog", "Pro tip - Choose a prefix directory with write access"))
        self.pushButton.setText(_translate("PrefixConfigDialog", "Create Prefix"))
        self.checkBox.setText(_translate("PrefixConfigDialog", "Make default prefix"))

import myicons_rc
