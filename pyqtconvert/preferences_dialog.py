# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/preferences_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PreferencesDialog(object):
    def setupUi(self, PreferencesDialog):
        PreferencesDialog.setObjectName("PreferencesDialog")
        PreferencesDialog.resize(560, 480)
        self.buttonBox = QtWidgets.QDialogButtonBox(PreferencesDialog)
        self.buttonBox.setGeometry(QtCore.QRect(380, 440, 176, 28))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(PreferencesDialog)
        self.label.setGeometry(QtCore.QRect(20, 290, 381, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(PreferencesDialog)
        self.label_2.setGeometry(QtCore.QRect(30, 199, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(PreferencesDialog)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(PreferencesDialog)
        self.comboBox.setGeometry(QtCore.QRect(220, 198, 301, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(PreferencesDialog)
        self.lineEdit.setGeometry(QtCore.QRect(220, 130, 301, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.line = QtWidgets.QFrame(PreferencesDialog)
        self.line.setGeometry(QtCore.QRect(0, 270, 561, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.textBrowser = QtWidgets.QTextBrowser(PreferencesDialog)
        self.textBrowser.setGeometry(QtCore.QRect(5, 321, 551, 111))
        self.textBrowser.setReadOnly(False)
        self.textBrowser.setObjectName("textBrowser")
        self.label_4 = QtWidgets.QLabel(PreferencesDialog)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 561, 101))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/noprefix/images/preferences.png"))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(PreferencesDialog)
        self.buttonBox.accepted.connect(PreferencesDialog.accept)
        self.buttonBox.rejected.connect(PreferencesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PreferencesDialog)

    def retranslateUi(self, PreferencesDialog):
        _translate = QtCore.QCoreApplication.translate
        PreferencesDialog.setWindowTitle(_translate("PreferencesDialog", "PyBOMBS App Store - Preferences"))
        self.label.setText(_translate("PreferencesDialog", "Forcebuild following OOT Modules:"))
        self.label_2.setText(_translate("PreferencesDialog", "Choose Existing Prefix"))
        self.label_3.setText(_translate("PreferencesDialog", "Create New Prefix"))
        self.comboBox.setItemText(0, _translate("PreferencesDialog", "prefix_one"))
        self.comboBox.setItemText(1, _translate("PreferencesDialog", "prefix_two"))
        self.comboBox.setItemText(2, _translate("PreferencesDialog", "prefix_three"))

import myicons_rc
