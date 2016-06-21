# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/module_info.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_moduleDialog(object):
    def setupUi(self, moduleDialog):
        moduleDialog.setObjectName("moduleDialog")
        moduleDialog.resize(445, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(moduleDialog.sizePolicy().hasHeightForWidth())
        moduleDialog.setSizePolicy(sizePolicy)
        moduleDialog.setFocusPolicy(QtCore.Qt.NoFocus)
        self.verticalLayout = QtWidgets.QVBoxLayout(moduleDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(moduleDialog)
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("QTabBar::tab{\n"
"  min-width: 10ex;\n"
"  padding: 2px;\n"
"  margin-right: 20px;\n"
"  margin-left: 10px;\n"
"  padding-right: 20px;\n"
"  padding-left: 20px;\n"
"  padding-top: -4px;\n"
"  focus{border:none;}\n"
"}\n"
"QTabBar::tab:selected {\n"
"  border-bottom : 2.3px solid;\n"
"  border-bottom-color: rgb(69, 140, 214);\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"  border-bottom: 2.3px solid; /* make non-selected tabs look smaller */\n"
"  border-bottom-color: rgb(135, 135, 134);   \n"
"}\n"
"\n"
"QTabBar:tab:focus {\n"
"  outline: none;\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setFocusPolicy(QtCore.Qt.TabFocus)
        self.textEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.textEdit.setStyleSheet("")
        self.textEdit.setTabChangesFocus(True)
        self.textEdit.setReadOnly(True)
        self.textEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textEdit_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.textEdit_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.textEdit_2.setTabChangesFocus(True)
        self.textEdit_2.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout_3.addWidget(self.textEdit_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.label = QtWidgets.QLabel(moduleDialog)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/noprefix/images/protip.png"))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.buttonBox = QtWidgets.QDialogButtonBox(moduleDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(moduleDialog)
        self.tabWidget.setCurrentIndex(1)
        self.buttonBox.accepted.connect(moduleDialog.accept)
        self.buttonBox.rejected.connect(moduleDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(moduleDialog)

    def retranslateUi(self, moduleDialog):
        _translate = QtCore.QCoreApplication.translate
        moduleDialog.setWindowTitle(_translate("moduleDialog", "Module Info"))
        self.textEdit.setHtml(_translate("moduleDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">By default, the menu indicator is located at the bottom-right corner of the padding rectangle. We can change this by specifying subcontrol-position and subcontrol-origin to anchor the indicator differently. We can also use top and left to move the indicator by a few pixels. For example:</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("moduleDialog", "Documentation"))
        self.textEdit_2.setHtml(_translate("moduleDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">By default, the menu indicator is located at the bottom-right corner of the padding rectangle. We can change this by specifying subcontrol-position and subcontrol-origin to anchor the indicator differently. We can also use top and left to move the indicator by a few pixels. For example:</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("moduleDialog", "Dependencies"))

import myicons_rc
