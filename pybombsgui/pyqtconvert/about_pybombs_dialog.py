# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/about_pybombs.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AboutPybombsDialog(object):
    def setupUi(self, AboutPybombsDialog):
        AboutPybombsDialog.setObjectName("AboutPybombsDialog")
        AboutPybombsDialog.resize(500, 360)
        self.label = QtWidgets.QLabel(AboutPybombsDialog)
        self.label.setGeometry(QtCore.QRect(10, 0, 480, 100))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/noprefix/images/about_logo.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(AboutPybombsDialog)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 480, 90))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(AboutPybombsDialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 300, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(AboutPybombsDialog)
        self.pushButton_3.setGeometry(QtCore.QRect(370, 300, 101, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(AboutPybombsDialog)
        self.label_3.setGeometry(QtCore.QRect(120, 100, 271, 20))
        self.label_3.setStyleSheet("font:  11pt \"Ubuntu\"; font-weight: bold;\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(AboutPybombsDialog)
        self.label_4.setGeometry(QtCore.QRect(20, 235, 101, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(AboutPybombsDialog)
        self.label_5.setGeometry(QtCore.QRect(190, 235, 101, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(AboutPybombsDialog)
        self.label_6.setGeometry(QtCore.QRect(360, 235, 101, 20))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.textEdit = QtWidgets.QTextEdit(AboutPybombsDialog)
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QtCore.QRect(10, 130, 480, 150))
        self.textEdit.setUndoRedoEnabled(False)
        self.textEdit.setReadOnly(True)
        self.textEdit.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse)
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(AboutPybombsDialog)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 300, 101, 41))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(AboutPybombsDialog)
        self.pushButton.clicked['bool'].connect(self.textEdit.hide)
        QtCore.QMetaObject.connectSlotsByName(AboutPybombsDialog)

    def retranslateUi(self, AboutPybombsDialog):
        _translate = QtCore.QCoreApplication.translate
        AboutPybombsDialog.setWindowTitle(_translate("AboutPybombsDialog", "Dialog"))
        self.label_2.setText(_translate("AboutPybombsDialog", "A GUI frontend for PyBOMBS - the GNU Radio install management system for resolving dependencies and pulling in OOT Modules"))
        self.pushButton.setText(_translate("AboutPybombsDialog", "Credits"))
        self.pushButton_3.setText(_translate("AboutPybombsDialog", "Close"))
        self.label_3.setText(_translate("AboutPybombsDialog", "Pybombs-QtGUI 0.0.1.dev1"))
        self.label_4.setText(_translate("AboutPybombsDialog", "<html><head/><body><p><a href=\"https://gitlab.com/NinjaComics/pybombs-qtgui\"><span style=\" text-decoration: underline; color:#0000ff;\">Gitlab repo</span></a></p></body></html>"))
        self.label_5.setText(_translate("AboutPybombsDialog", "<html><head/><body><p><a href=\"https://www.gnuradio.org\"><span style=\" text-decoration: underline; color:#0000ff;\">GNU Radio</span></a></p></body></html>"))
        self.label_6.setText(_translate("AboutPybombsDialog", "<html><head/><body><p><a href=\"cgran.org\"><span style=\" text-decoration: underline; color:#0000ff;\">CGRAN</span></a></p></body></html>"))
        self.textEdit.setHtml(_translate("AboutPybombsDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Pybombs-QtGUI created by<span style=\" font-weight:600;\"> :</span> Ravi Sharan</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This GUI app is developed as a part of GSoC \'16,</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">with guidance and help from original creator of <a href=\"https://github.com/gnuradio/pybombs/\"><span style=\" text-decoration: underline; color:#0000ff;\">Pybombs</span></a> - </p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Martin Braun</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p></body></html>"))
        self.pushButton_2.setText(_translate("AboutPybombsDialog", "Credits"))

import myicons_rc
