# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/pybombs_main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(652, 526)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_5)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.tab_5)
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setContentsMargins(15, 15, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.widget)
        self.tableWidget_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_3.setAlternatingRowColors(True)
        self.tableWidget_3.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_3.setShowGrid(False)
        self.tableWidget_3.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(2)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.tableWidget_3.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_4.addWidget(self.tableWidget_3)
        self.horizontalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.tab_5)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setContentsMargins(15, 15, 15, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.widget_2)
        self.tableWidget_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_2.setLineWidth(1)
        self.tableWidget_2.setMidLineWidth(0)
        self.tableWidget_2.setDragEnabled(False)
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_2.setShowGrid(False)
        self.tableWidget_2.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_3.addWidget(self.tableWidget_2)
        self.horizontalLayout.addWidget(self.widget_2)
        self.tabWidget.addTab(self.tab_5, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 652, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuActions = QtWidgets.QMenu(self.menubar)
        self.menuActions.setObjectName("menuActions")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setEnabled(True)
        self.toolBar.setStyleSheet("")
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_About_GNU_Radio = QtWidgets.QAction(MainWindow)
        self.action_About_GNU_Radio.setObjectName("action_About_GNU_Radio")
        self.action_About_CGRAN = QtWidgets.QAction(MainWindow)
        self.action_About_CGRAN.setObjectName("action_About_CGRAN")
        self.action_Apply = QtWidgets.QAction(MainWindow)
        self.action_Apply.setEnabled(False)
        font = QtGui.QFont()
        self.action_Apply.setFont(font)
        self.action_Apply.setIconVisibleInMenu(False)
        self.action_Apply.setObjectName("action_Apply")
        self.action_Refresh = QtWidgets.QAction(MainWindow)
        self.action_Refresh.setIconVisibleInMenu(False)
        self.action_Refresh.setObjectName("action_Refresh")
        self.action_Search = QtWidgets.QAction(MainWindow)
        self.action_Search.setIconVisibleInMenu(False)
        self.action_Search.setObjectName("action_Search")
        self.action_Preferences = QtWidgets.QAction(MainWindow)
        self.action_Preferences.setIconVisibleInMenu(False)
        self.action_Preferences.setObjectName("action_Preferences")
        self.action_RunningConfig = QtWidgets.QAction(MainWindow)
        self.action_RunningConfig.setObjectName("action_RunningConfig")
        self.action_About_PyBOMBS = QtWidgets.QAction(MainWindow)
        self.action_About_PyBOMBS.setObjectName("action_About_PyBOMBS")
        self.action_Discard_Changes = QtWidgets.QAction(MainWindow)
        self.action_Discard_Changes.setObjectName("action_Discard_Changes")
        self.action_Recipe_Manager = QtWidgets.QAction(MainWindow)
        self.action_Recipe_Manager.setObjectName("action_Recipe_Manager")
        self.action_Prefix_Manager = QtWidgets.QAction(MainWindow)
        self.action_Prefix_Manager.setObjectName("action_Prefix_Manager")
        self.action_Add_Recipe = QtWidgets.QAction(MainWindow)
        self.action_Add_Recipe.setObjectName("action_Add_Recipe")
        self.action_Choose_Prefix = QtWidgets.QAction(MainWindow)
        self.action_Choose_Prefix.setObjectName("action_Choose_Prefix")
        self.menuFile.addAction(self.action_Prefix_Manager)
        self.menuFile.addAction(self.action_Recipe_Manager)
        self.menuFile.addAction(self.action_Add_Recipe)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_RunningConfig)
        self.menuActions.addSeparator()
        self.menuActions.addSeparator()
        self.menuActions.addAction(self.action_Apply)
        self.menuActions.addAction(self.action_Discard_Changes)
        self.menuActions.addAction(self.action_Refresh)
        self.menuActions.addSeparator()
        self.menuActions.addAction(self.action_Search)
        self.menuActions.addAction(self.action_Choose_Prefix)
        self.menuHelp.addAction(self.action_About_PyBOMBS)
        self.menuHelp.addAction(self.action_About_GNU_Radio)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.action_About_CGRAN)
        self.menuHelp.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuActions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.action_Apply)
        self.toolBar.addAction(self.action_Discard_Changes)
        self.toolBar.addAction(self.action_Refresh)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Choose_Prefix)
        self.toolBar.addAction(self.action_Prefix_Manager)
        self.toolBar.addAction(self.action_Recipe_Manager)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Search)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Package Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Category"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Status"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Description"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Applications"))
        self.label.setText(_translate("MainWindow", "Baseline Packages"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Package Name"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Status"))
        self.label_2.setText(_translate("MainWindow", "Prefix Specific Packages"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Package Name"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Status"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Other Packages"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuActions.setTitle(_translate("MainWindow", "Actions"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_About_GNU_Radio.setText(_translate("MainWindow", "&About GNU Radio"))
        self.action_About_CGRAN.setText(_translate("MainWindow", "&About CGRAN"))
        self.action_Apply.setText(_translate("MainWindow", "&Apply Changes"))
        self.action_Refresh.setText(_translate("MainWindow", "&Refresh List"))
        self.action_Search.setText(_translate("MainWindow", "&Search"))
        self.action_Search.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.action_Preferences.setText(_translate("MainWindow", "&Prefix Manager"))
        self.action_RunningConfig.setText(_translate("MainWindow", "&Running Config"))
        self.action_About_PyBOMBS.setText(_translate("MainWindow", "&About PyBOMBS"))
        self.action_Discard_Changes.setText(_translate("MainWindow", "&Discard Changes"))
        self.action_Recipe_Manager.setText(_translate("MainWindow", "&Recipe Manager"))
        self.action_Prefix_Manager.setText(_translate("MainWindow", "&Prefix Manager"))
        self.action_Add_Recipe.setText(_translate("MainWindow", "&Add Recipe"))
        self.action_Choose_Prefix.setText(_translate("MainWindow", "&Choose Prefix"))

import myicons_rc
