#!/usr/bin/python

import os, sys, subprocess

# PyQt API imports
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QCursor
from PyQt5.QtCore import QAbstractTableModel, Qt, QVariant

# Import UI from designer generated python files
from pyqtconvert.ui_convert import Ui_MainWindow
from wizard_dialog import ConfigWizard, ConfigDialog 
from search_dialog import SearchDialog
from module_info_dialog import ModuleInfo
from preferences_dialog import PreferencesDialog
from running_config_dialog import RunningConfig

# Pybombs API imports
from pybombs import config_manager, package_manager, recipe_manager, recipe 

class PybombsMainWindow(QMainWindow, Ui_MainWindow): 
    def __init__(self):
        """Pybombs GUI MainWindow
        """
        super(PybombsMainWindow, self).__init__()
        
        #Setup the UI for MainWindow 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
         
        #MainWindow Properties
        self.ui.centralwidget.setContentsMargins(0, 0, 0, 0);
        self.ui.verticalLayout.setContentsMargins(0, 0, 0, 0);        
        
        #creating an empty list which later goes into install_manager.py 
        #with full list of packages to install/update/remove
        self.install_material = []

        #Our tableview and it's data. Yay ! 
        self.generate_table_data()    
        self.create_table()
        
        #Searchbox in Toolbar
        self.ui.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setPlaceholderText("Quick search")
        self.lineEdit.setFixedWidth(250)
        self.ui.toolBar.addWidget(self.lineEdit)

        #Prefix Config Wizard Properties
        self.wizard = ConfigWizard()
        self.wizard.setWindowTitle("PyBOMBS Prefix Configuration") 
        self.wizard.setContentsMargins(0,0,0,0)
        self.wizard.setModal(True)
        self.wizard.show()      
    
        #It's all signals and slots !!!
        self.ui.action_About_PyBOMBS.triggered.connect(self.config_window_popup) #About Pybombs dialog
        self.ui.action_Preferences.triggered.connect(self.preferences_popup) #Pybombs preferences dialog   
        self.ui.action_Search.triggered.connect(self.search_box_popup) #Search Dialog box
        self.ui.action_RunningConfig.triggered.connect(self.config_info_popup) #Displays running config
        self.ui.action_Apply.triggered.connect(self.apply_changes) #Install Manager stuff
        
    #Here's where we decorate the tableView and generate the source data for table
    def generate_table_data(self):
        """Generate data from Pybombs backend to feed to the Model
        """ 
        self.tabledata = []
        self.pm = package_manager.PackageManager()
        
        list_recipes = sorted(list(recipe_manager.recipe_manager.list_all()))
        
        #if list_recipes:
        #    reply = QMessageBox.question(self, 'Ruh Oh !', "Looks like there are no recipes Would you like to add some ?", 
        #    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        #    
        #    if reply == QMessageBox.Yes:
        #        pass
        #    else:
        #        pass
        
        #The following three lines are hard-coded. Do something to fix that. Do it already !    
        list_recipes.remove('gnuradio-stable')  #Pybombs CLI specific recipe
        list_recipes.remove('default_prefix')   #Pybombs CLI specific recipe
        list_recipes.remove('gnuradio-default') #Pybombs CLI specific recipe        

        for oot_module in list_recipes:
            rec = recipe.get_recipe(oot_module)
            if rec.get_dict()['category'] == 'baseline':
                pass
            else:
                if 'description' in rec.get_dict():    
                    if(self.pm.installed(oot_module) == True):
                        self.tabledata.append([oot_module, rec.get_dict()['category'], 
                        'Installed', rec.get_dict()['description']])
                    else:
                        self.tabledata.append([oot_module, rec.get_dict()['category'], 
                        'Not Installed', rec.get_dict()['description']])
                else:
                    if(self.pm.installed(oot_module) == True):
                        self.tabledata.append([oot_module, rec.get_dict()['category'], 
                        'Installed', 'No description available'])
                    else:
                        self.tabledata.append([oot_module, rec.get_dict()['category'], 
                        'Not Installed', 'No description available'])

    def create_table(self):
        """TableView's stuff in here !
        """
        header = ['Name', 'Category', 'Status', 'Description']
        table_model = PybombsTableModel(self.tabledata, header, self)
        #QTableView Properties
        self.ui.tableView.setShowGrid(False)
        self.ui.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tableView.verticalHeader().setVisible(False)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents) 
        self.ui.tableView.horizontalHeader().setStretchLastSection(True)
        self.ui.tableView.setContextMenuPolicy(Qt.CustomContextMenu) #For custom context menu
        self.ui.tableView.setModel(table_model) #Apply our model to the tableview
        self.ui.tableView.horizontalHeader().setStyleSheet("QHeaderView {font: bold; color:gray; border: 0px; padding: 0px;}")
        self.ui.tableView.setStyleSheet("QTableView::item {border: 0px; padding-left: 10px; padding-right: 40px;}")      
        
        #TableView's ContextMenu that displays (Install/Update/Remove/Module Info) menu
        self.ui.tableView.customContextMenuRequested.connect(self.context_menu)
    
    #Methods for Dialogs and Wizard
    def apply_changes(self):
        install_manager.Install
    def config_window_popup(self):
        self.dialog = ConfigDialog()
        self.dialog.setWindowTitle("About PyBOMBS")
        self.dialog.show()
    
    def preferences_popup(self):
        self.preferences = PreferencesDialog()
        self.preferences.show()

    def search_box_popup(self):
        self.search_opt = SearchDialog()
        self.search_opt.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.search_opt.show()
    
    def module_info_popup(self):
        self.module_dialog = ModuleInfo()
        self.module_dialog.setFixedSize(self.module_dialog.size())
        self.module_dialog.show()

    def config_info_popup(self):
        self.running_config_dialog = RunningConfig()
        self.running_config_dialog.show()

    def context_menu(self):
        """Custom ContextMenu that helps us install/update/remove OOT Modules
           from the list displayed on tableView 
        """
        #Following three lines will return the package name irrespective of where
        #mouse click event happens on the row associated with the package
        indexes = self.ui.tableView.selectionModel().selectedRows()
        for index in indexes:
            package_name = self.ui.tableView.model().index(index.row(), 0).data()
        
        menu = QMenu(self)
        install = menu.addAction("Install")
        update = menu.addAction("Update")
        remove = menu.addAction("Remove")
        menu.addSeparator()
        module_info = menu.addAction("Module Info")
        if self.pm.installed(package_name):
            install.setEnabled(False)
        else:
            update.setEnabled(False)
            remove.setEnabled(False)
        action = menu.exec_(QCursor.pos())
        if (action == install):
            self.install_material.append(package_name)    
        elif (action == module_info):
            self.module_info_popup()
           
class PybombsTableModel(QAbstractTableModel): 
    def __init__(self, datain, headerdata, parent=None, *args): 
        """ datain: a list of lists
            headerdata: a list of strings
        """
        QAbstractTableModel.__init__(self, parent, *args) 
        self.arraydata = datain
        self.headerdata = headerdata
 
    def rowCount(self, parent): 
        return len(self.arraydata) 
 
    def columnCount(self, parent): 
        return len(self.arraydata[0])
 
    def data(self, index, role): 
        if not index.isValid(): 
            return QVariant() 
        elif role != Qt.DisplayRole: 
            return QVariant() 
        return QVariant(self.arraydata[index.row()][index.column()]) 

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.headerdata[col])
        return QVariant()
        
def main():
    app = QApplication(sys.argv)
    bombs = PybombsMainWindow()
    bombs.setWindowTitle("PyBOMBS App Store")
    bombs.showMaximized()
    #bombs.setWindowIcon(QIcon(":/images/box.png"))
    bombs.show()
    app.exec()
      
if __name__ == '__main__':
    main()
