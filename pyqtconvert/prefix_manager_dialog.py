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
        PrefixConfigDialog.resize(560, 480)
        self.buttonBox = QtWidgets.QDialogButtonBox(PrefixConfigDialog)
        self.buttonBox.setGeometry(QtCore.QRect(380, 440, 176, 28))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(PrefixConfigDialog)
        self.label.setGeometry(QtCore.QRect(20, 250, 421, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(PrefixConfigDialog)
        self.label_3.setGeometry(QtCore.QRect(30, 170, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(PrefixConfigDialog)
        self.lineEdit.setGeometry(QtCore.QRect(220, 170, 301, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.line = QtWidgets.QFrame(PrefixConfigDialog)
        self.line.setGeometry(QtCore.QRect(0, 230, 561, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.textBrowser = QtWidgets.QTextBrowser(PrefixConfigDialog)
        self.textBrowser.setGeometry(QtCore.QRect(5, 281, 551, 111))
        self.textBrowser.setReadOnly(False)
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit_2 = QtWidgets.QLineEdit(PrefixConfigDialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 90, 301, 41))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(PrefixConfigDialog)
        self.label_5.setGeometry(QtCore.QRect(30, 90, 141, 41))
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

        self.retranslateUi(PrefixConfigDialog)
        self.buttonBox.accepted.connect(PrefixConfigDialog.accept)
        self.buttonBox.rejected.connect(PrefixConfigDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PrefixConfigDialog)

    def retranslateUi(self, PrefixConfigDialog):
        _translate = QtCore.QCoreApplication.translate
        PrefixConfigDialog.setWindowTitle(_translate("PrefixConfigDialog", "Prefix Manager"))
        self.label.setText(_translate("PrefixConfigDialog", "Forcebuild following OOT Modules: (specific to this prefix)"))
        self.label_3.setText(_translate("PrefixConfigDialog", "Prefix Directory"))
        self.label_5.setText(_translate("PrefixConfigDialog", "Prefix Alias"))
        self.label_4.setText(_translate("PrefixConfigDialog", "Pro tip - Choose a prefix directory with write access"))

import myicons_rc
