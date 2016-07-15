# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/module_info.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ModuleInfoDialog(object):
    def setupUi(self, ModuleInfoDialog):
        ModuleInfoDialog.setObjectName("ModuleInfoDialog")
        ModuleInfoDialog.resize(445, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ModuleInfoDialog.sizePolicy().hasHeightForWidth())
        ModuleInfoDialog.setSizePolicy(sizePolicy)
        ModuleInfoDialog.setFocusPolicy(QtCore.Qt.NoFocus)
        ModuleInfoDialog.setWindowTitle("")
        self.tabWidget = QtWidgets.QTabWidget(ModuleInfoDialog)
        self.tabWidget.setGeometry(QtCore.QRect(9, 9, 431, 331))
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_2.addWidget(self.plainTextEdit)
        self.tabWidget.addTab(self.tab, "")
        self.label = QtWidgets.QLabel(ModuleInfoDialog)
        self.label.setGeometry(QtCore.QRect(9, 340, 427, 93))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/noprefix/images/protip.png"))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(ModuleInfoDialog)
        self.pushButton.setGeometry(QtCore.QRect(362, 440, 71, 32))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(ModuleInfoDialog)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton.clicked['bool'].connect(ModuleInfoDialog.close)
        QtCore.QMetaObject.connectSlotsByName(ModuleInfoDialog)

    def retranslateUi(self, ModuleInfoDialog):
        _translate = QtCore.QCoreApplication.translate
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("ModuleInfoDialog", "Module Info"))
        self.pushButton.setText(_translate("ModuleInfoDialog", "Ok"))

import myicons_rc
