# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/config_wizard.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Wizard(object):
    def setupUi(self, Wizard):
        Wizard.setObjectName("Wizard")
        Wizard.resize(640, 480)
        font = QtGui.QFont()
        font.setPointSize(12)
        Wizard.setFont(font)
        Wizard.setOptions(QtWidgets.QWizard.HelpButtonOnRight|QtWidgets.QWizard.NoBackButtonOnStartPage|QtWidgets.QWizard.NoCancelButton)
        self.wizardPage1 = QtWidgets.QWizardPage()
        self.wizardPage1.setObjectName("wizardPage1")
        self.label = QtWidgets.QLabel(self.wizardPage1)
        self.label.setGeometry(QtCore.QRect(50, 210, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.wizardPage1)
        self.lineEdit.setGeometry(QtCore.QRect(240, 210, 341, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.wizardPage1)
        self.label_3.setGeometry(QtCore.QRect(-10, -20, 661, 191))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/noprefix/images/pybombs_logo.png"))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.wizardPage1)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 300, 341, 41))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.wizardPage1)
        self.label_2.setGeometry(QtCore.QRect(50, 300, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.checkBox = QtWidgets.QCheckBox(self.wizardPage1)
        self.checkBox.setGeometry(QtCore.QRect(460, 350, 131, 25))
        self.checkBox.setObjectName("checkBox")
        Wizard.addPage(self.wizardPage1)

        self.retranslateUi(Wizard)
        QtCore.QMetaObject.connectSlotsByName(Wizard)

    def retranslateUi(self, Wizard):
        _translate = QtCore.QCoreApplication.translate
        Wizard.setWindowTitle(_translate("Wizard", "Wizard"))
        self.label.setText(_translate("Wizard", "New Prefix Alias"))
        self.label_2.setText(_translate("Wizard", "New Prefix Location"))
        self.checkBox.setText(_translate("Wizard", "Make Default"))

import myicons_rc
