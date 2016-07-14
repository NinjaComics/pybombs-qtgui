# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/progress_bar.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ProgressBarDialog(object):
    def setupUi(self, ProgressBarDialog):
        ProgressBarDialog.setObjectName("ProgressBarDialog")
        ProgressBarDialog.resize(600, 181)
        self.progressBar = QtWidgets.QProgressBar(ProgressBarDialog)
        self.progressBar.setGeometry(QtCore.QRect(10, 70, 581, 28))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(ProgressBarDialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 371, 31))
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(ProgressBarDialog)
        self.pushButton.setGeometry(QtCore.QRect(376, 120, 101, 41))
        self.pushButton.setDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(ProgressBarDialog)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 120, 101, 41))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(ProgressBarDialog)
        self.pushButton.clicked['bool'].connect(ProgressBarDialog.groupBox.setVisible)
        QtCore.QMetaObject.connectSlotsByName(ProgressBarDialog)

    def retranslateUi(self, ProgressBarDialog):
        _translate = QtCore.QCoreApplication.translate
        ProgressBarDialog.setWindowTitle(_translate("ProgressBarDialog", "Dialog"))
        self.pushButton.setText(_translate("ProgressBarDialog", "Details"))
        self.pushButton_2.setText(_translate("ProgressBarDialog", "Cancel"))

