# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/about_pybombs.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AboutPybombsDialog(object):
    def setupUi(self, AboutPybombsDialog):
        AboutPybombsDialog.setObjectName("AboutPybombsDialog")
        AboutPybombsDialog.resize(640, 480)
        self.buttonBox = QtWidgets.QDialogButtonBox(AboutPybombsDialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 440, 621, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.widget = QtWidgets.QWidget(AboutPybombsDialog)
        self.widget.setGeometry(QtCore.QRect(0, 10, 640, 420))
        self.widget.setObjectName("widget")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(190, 210, 301, 201))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(AboutPybombsDialog)
        self.buttonBox.accepted.connect(AboutPybombsDialog.accept)
        self.buttonBox.rejected.connect(AboutPybombsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AboutPybombsDialog)

    def retranslateUi(self, AboutPybombsDialog):
        _translate = QtCore.QCoreApplication.translate
        AboutPybombsDialog.setWindowTitle(_translate("AboutPybombsDialog", "Dialog"))
        self.label_2.setText(_translate("AboutPybombsDialog", "Our popular package manager has had its first version number bump since the version 2 release. Version 2.0.1 contains a lot of fixes for bugs, most of which were reported by community members willing to try the early 2.0.0 release. We would like to thank everyone for trying PyBOMBS 2.0.0 and reporting back any issues.\n"
"\n"
""))

