#!/usr/bin/python

import os, sys, subprocess

# PyQt API imports
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout,
 QLabel, QLineEdit, QVBoxLayout, QWizard, QWizardPage, QDialog, QProgressBar, QCheckBox)
from PyQt5.QtGui import QIcon, QPixmap

# Import UI from designer files
from pyqtconvert.ui_convert import Ui_MainWindow
from pybombs_dialogs import ConfigWizard, ConfigDialog, SearchDial, ModuleInfo, PreferencesDialog, RunningConfig

# Pybombs API imports
from pybombs.config_manager import ConfigManager

class PybombsMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(PybombsMainWindow, self).__init__()
        
        #Setup the UI for MainWindow 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
         
        #MainWindow Properties
        self.ui.centralwidget.setContentsMargins(0, 0, 0, 0);
        self.ui.verticalLayout.setContentsMargins(0, 0, 0, 0);        
         
        #Toolbar Properties
        self.ui.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setPlaceholderText("Quick search")
        self.lineEdit.setFixedWidth(200)
        self.ui.toolBar.addWidget(self.lineEdit)

        #QTableWidget Properties
        #self.ui.tableWidget.setRowCount(44) #Replace this line with real entries
        self.ui.tableWidget.resizeRowsToContents()
        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableWidget.setShowGrid(False)
        self.ui.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget.verticalHeader().setVisible(False)
        self.ui.tableWidget.setAlternatingRowColors(True)
       
        #Prefix Config Wizard Properties
        self.wizard = ConfigWizard()
        self.wizard.setWindowTitle("PyBOMBS Prefix Configuration") 
        self.wizard.setContentsMargins(0,0,0,0)
        self.wizard.setModal(True)
        self.wizard.show()
        #self.wizard.exec_()      
    
        #It's all signals and slots !!!
        self.ui.action_About_PyBOMBS.triggered.connect(self.config_window_popup)
        self.ui.action_Preferences.triggered.connect(self.preferences_popup)
        self.ui.action_Search.triggered.connect(self.search_box_popup)
        self.ui.action_Properties.triggered.connect(self.module_info_popup)
        self.ui.action_RunningConfig.triggered.connect(self.config_info_popup)    
        
        #self.populate_tabs()

    # General Methods
    #def populate_tabs(self):
        
 
    #Methods for Dialogs and Wizard
    def config_window_popup(self):
        self.dialog = ConfigDialog()
        self.dialog.setWindowTitle("About PyBOMBS")
        self.dialog.show()
    
    def preferences_popup(self):
        self.preferences = PreferencesDialog()
        self.preferences.show()

    def search_box_popup(self):
        self.search_opt = SearchDial()
        self.search_opt.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.search_opt.show()
    
    def module_info_popup(self):
        self.module_dialog = ModuleInfo()
        #self.module_dialog.move(QtWidgets.QDesktopWidget.availableGeometry.center() - self.module_infoui.frameGeometry.center())
        self.module_dialog.show()

    def config_info_popup(self):
        self.running_config_dialog = RunningConfig()
        #self.module_dialog.move(QtWidgets.QDesktopWidget.availableGeometry.center() - self.module_infoui.frameGeometry.center())
        self.running_config_dialog.show()
        
def main():
    app = QApplication(sys.argv)
    bombs = PybombsMainWindow()
    bombs.setWindowTitle("PyBOMBS App Store")
    bombs.showMaximized()
    bombs.setWindowIcon(QIcon(":/images/box.png"))
    bombs.setGeometry(0,0, 640, 480)
    bombs.show()
    app.exec()
      
if __name__ == '__main__':
    main()

