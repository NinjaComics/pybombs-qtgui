#!/usr/bin/python

import os
import sys
import subprocess

# PyQt API imports
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu, QTableWidgetItem
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

# Import UI from designer generated python files
from pyqtconvert.ui_convert import Ui_MainWindow
from wizard_dialog import ConfigWizard, ConfigDialog, RunConfigDialog
from search_dialog import SearchDialog
from module_info_dialog import ModuleInfo
from preferences_dialog import PreferencesDialog
from recipe_manager_dialog import RecipeConfigDialog
from add_recipe_dialog import NewRecipeDialog
from prefix_chooser_dialog import PrefixChooserDialog

# Pybombs API imports
from pybombs import config_manager, package_manager, recipe_manager, recipe, install_manager

class PybombsMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        """Pybombs GUI MainWindow
        """
        super(PybombsMainWindow, self).__init__()

        #Setup the UI for MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #MainWindow Properties
        self.ui.centralwidget.setContentsMargins(0, 0, 0, 0)
        self.ui.verticalLayout.setContentsMargins(0, 0, 0, 0)

        #creating an empty dictionary and few lists which later goes into install_manager.py
        #with full list of packages to install/update/remove
        self.final_packages = {}
        self.install_material = []
        self.update_material = []
        self.remove_material = []

        self.cfg = config_manager.config_manager
        if len(self.cfg.get('default_prefix')) == 0:
            self.prefix_config_wizard() #Pybombs preferences dialog

        #Searchbox in Toolbar
        self.ui.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.tb_lineEdit = QtWidgets.QLineEdit(self)
        self.tb_lineEdit.setPlaceholderText("Quick search")
        self.tb_lineEdit.setFixedWidth(250)
        self.ui.toolBar.addWidget(self.tb_lineEdit)

        #Our tableWidget and it's data. Yay !
        self.generate_table_data()
        self.create_table()
        #self.ui.tableWidget.setModel(self.table_model) #Apply our model to the tableWidget

        #It's all signals and slots !!!
        #self.ui.action_About_PyBOMBS.triggered.connect(self.config_window_popup)
        self.ui.action_Prefix_Manager.triggered.connect(self.preferences_popup)
        self.ui.action_Search.triggered.connect(self.search_box_popup)
        #self.ui.action_RunningConfig.triggered.connect(self.config_info_popup)
        self.ui.action_Recipe_Manager.triggered.connect(self.recipe_manager_popup)
        self.ui.action_Apply.triggered.connect(self.apply_changes)
        self.ui.action_Add_Recipe.triggered.connect(self.add_recipes_popup)
        self.ui.action_Choose_Prefix.triggered.connect(self.prefix_chooser_popup)
        self.tb_lineEdit.returnPressed.connect(self.search_highlight)

    #Here's where we decorate the tableWidget and generate the source data for table
    def generate_table_data(self):
        """Generate data from Pybombs backend to feed to the Model
        """
        self.tabledata = []
        self.pm = package_manager.PackageManager()

        list_recipes = sorted(list(recipe_manager.recipe_manager.list_all()))

        #The following three lines are hard-coded. Do something to fix that. Do it already !
        #http://lists.gnu.org/archive/html/discuss-gnuradio/2016-05/msg00242.html As explained in
        #this thread, the CLI can initialize and install GNU Radio along with bunch of other packages
        #with a single command, but that doesn't hold true for the GUI. The user is first presented
        #with a single command, but that doesn't hold true for the GUI. The user is first presented
        #with a list of packages available and then the user gets to choose which version of gnuradio
        #he/she wants to install.
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
        """tableWidget's stuff in here !
        """
        #QtableWidget Propertiesself.ui.tableWidget.setShowGrid(False)
        self.ui.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget.verticalHeader().setVisible(False)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.
                                                                    ResizeToContents)
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.ui.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu) #For custom context menu
        self.ui.tableWidget.horizontalHeader().setStyleSheet("QHeaderView {font: bold; color:gray; border: 0px; padding: 0px;}")
        self.ui.tableWidget.setAlternatingRowColors(True)
        self.ui.tableWidget.setStyleSheet("QTableWidget {alternate-background-color: rgb(211, 215, 207); background-color: white;}")
        self.ui.tableWidget.setStyleSheet("QTableWidget::item {border: 0px; padding-left: 10px; padding-right: 40px;}")

        #tableWidget's ContextMenu that displays (Install/Update/Remove/Module Info) menu
        self.ui.tableWidget.customContextMenuRequested.connect(self.context_menu)

        #set generated data to tableWidget
        self.ui.tableWidget.setRowCount(len(self.tabledata))

        row = 0
        for data in self.tabledata:
            for column in range(self.ui.tableWidget.columnCount()):
                self.ui.tableWidget.setItem(row, column, QTableWidgetItem(str(data[column])))
            row += 1

    #Methods for Dialogs and Wizard
    def prefix_config_wizard(self):
        #Prefix Config Wizard Properties
        self.wizard = ConfigWizard()
        self.wizard.setWindowTitle("PyBOMBS Prefix Configuration")
        self.wizard.setContentsMargins(0, 0, 0, 0)
        self.wizard.setModal(True)
        self.wizard.show()
        self.wizard.exec_()

    def add_recipes_popup(self):
        self.new_rec = NewRecipeDialog()
        self.new_rec.setWindowTitle("Add New Recipe")
        self.new_rec.show()

        self.dialog = ConfigDialog()
        self.dialog.setWindowTitle("About PyBOMBS")
        self.dialog.show()

    def recipe_manager_popup(self):
        self.recman = RecipeConfigDialog()
        self.recman.setWindowTitle("Pybombs Recipe Manager")
        self.recman.show()

    def preferences_popup(self):
        self.preferences = PreferencesDialog()
        self.preferences.setWindowTitle("Prefix Manager")
        self.preferences.show()

    def search_box_popup(self):
        self.search_opt = SearchDialog()
        self.search_opt.setWindowFlags(QtCore.Qt.FramelessWindowHint | Qt.Popup)
        self.search_opt.show()

    def search_highlight(self):
        search_items = self.ui.tableWidget.findItems(self.tb_lineEdit.text(), QtCore.Qt.MatchExactly)
        for item in search_items:
            self.ui.tableWidget.selectRow(item.row())
            self.ui.tableWidget.setStyleSheet("QTableWidget::item:selected {background-color: gray;}")
            self.ui.tableWidget.setStyleSheet("QTableWidget::item {border: 0px; padding-left: 10px; padding-right: 40px;}")
            self.tb_lineEdit.clear()

    def prefix_chooser_popup(self):
        self.choose_prefix = PrefixChooserDialog()
        self.choose_prefix.setWindowFlags(QtCore.Qt.FramelessWindowHint | Qt.Popup)
        self.choose_prefix.show()
        current_prefix = self.choose_prefix.current_prefix()
        self.prefix_msg = 'Active Prefix - {}'.format(current_prefix)

    def module_info_popup(self, package_name):
        self.module_dialog = ModuleInfo(package_name)
        self.module_dialog.setFixedSize(self.module_dialog.size())
        self.module_dialog.show()

    def config_info_popup(self):
        self.running_config_dialog = RunningConfig()
        self.running_config_dialog.show()

    def context_menu(self):
        """Custom ContextMenu that helps us install/update/remove OOT Modules
           from the list displayed on tableWidget
        """
        #Following three lines will return the package name irrespective of where
        #mouse click event happens on the row associated with the package
        indexes = self.ui.tableWidget.selectionModel().selectedRows()
        for index in indexes:
            package_name = self.ui.tableWidget.model().index(index.row(), 0).data()

        #Our custom context menu
        menu = QMenu(self)
        install = menu.addAction("&Mark Install")
        update = menu.addAction("&Mark Update")
        remove = menu.addAction("&Mark Remove")
        menu.addSeparator()
        discard = menu.addAction("&Discard Changes")
        module_info = menu.addAction("&Module Info")
        if self.pm.installed(package_name):
            install.setEnabled(False)
        else:
            update.setEnabled(False)
            remove.setEnabled(False)

        if package_name in self.install_material:
            discard.setEnabled(True)
        elif package_name in self.update_material:
            discard.setEnabled(True)
        elif package_name in self.remove_material:
            discard.setEnabled(True)
        else:
            discard.setEnabled(False)

        action = menu.exec_(QCursor.pos())

        #Here's where our context menu gets some work to do
        if (action == install):
            self.install_material.append(package_name)
            print('{} = self.install_material'.format(self.install_material))

        if (action == update):
            self.update_material.append(package_name)
            print('{} = self.update_material'.format(self.update_material))

        if (action == remove):
            self.remove_material.append(package_name)
            print('{} = self.remove_material'.format(self.remove_material))

        if (action == discard):
            if package_name in self.install_material:
                self.install_material.remove(package_name)

            if package_name in self.update_material:
                self.update_material.remove(package_name)

            if package_name in self.remove_material:
                self.remove_material.remove(package_name)

        if (self.install_material and self.update_material and self.remove_material) == []:
            self.ui.action_Apply.setEnabled(True)
        else:
            self.ui.action_Apply.setEnabled(False)

    def apply_changes(self):
        self.final_packages = {'install': self.install_material,
                               'update': self.update_material,
                               'remove': self.remove_material}
        print(self.final_packages.values(), self.final_packages.keys())
        instaman = install_manager.InstallManager()

        if 'install' in self.final_packages:
            instaman.install(self.final_packages.get('install'), 'install')

        if 'update' in self.final_packages:
            instaman.install(self.final_packages.get('update'),
                             'update', update_if_exists=True)

        if 'remove' in self.final_packages:
            pass

def main():
    app = QApplication(sys.argv)
    bombs = PybombsMainWindow()
    bombs.setWindowTitle("PyBOMBS App Store")
    bombs.showMaximized()
    #bombs.setWindowIcon(QIcon(":/images/box.png"))
    bombs.show()
    app.exec_()

if __name__ == '__main__':
    main()
