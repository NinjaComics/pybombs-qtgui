# PyQt API imports
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import (QApplication, QMainWindow, QDialog, QFrame, QTableWidgetItem)
from PyQt5.QtGui import QIcon, QPixmap

# Import UI from designer files
from pyqtconvert.recipe_config import Ui_RecipeConfigDialog

#Pybombs API imports
from pybombs import config_manager, recipe_manager

class RecipeConfigDialog(QDialog, Ui_RecipeConfigDialog):
    def __init__(self):
        super(RecipeConfigDialog, self).__init__()
        self.recipeconfig_dialogui = Ui_RecipeConfigDialog()
        self.recipeconfig_dialogui.setupUi(self) 

        self.generate_recipe_repos()
        self.set_repo_data()
                 
        self.prefix_combobox_items = sorted(list(self.cfg.prefix_aliases().keys()))
        self.recipeconfig_dialogui.comboBox.clear()

        self.recipeconfig_dialogui.comboBox.addItem('')
        if self.prefix_combobox_items:
            for item in self.prefix_combobox_items:
                self.recipeconfig_dialogui.comboBox.addItem(item)

        self.recipeconfig_dialogui.label_5.hide()

        self.recipeconfig_dialogui.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.recipeconfig_dialogui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.recipeconfig_dialogui.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.recipeconfig_dialogui.tableWidget.resizeColumnsToContents()
        self.recipeconfig_dialogui.tableWidget.resizeRowsToContents()
        self.recipeconfig_dialogui.tableWidget.verticalHeader().setVisible(False)
        self.recipeconfig_dialogui.lineEdit_2.editingFinished.connect(self.collect_recipe_info)
           
    def generate_recipe_repos(self): 
        self.cfg = config_manager.config_manager
        self.recipe_repo_data = [] 
        self.all_locations = self.cfg.get_recipe_locations()
        self.named_sources = self.cfg.get_named_recipe_sources()
        self.named_locations = self.cfg.get_named_recipe_dirs()
        self.unnamed_locations = [x for x in self.all_locations if not x in self.named_locations.values()]

        for name in self.named_locations.keys():
            self.recipe_repo_data.append([name, self.named_locations.get(name), self.named_sources.get(name)])

        for loc in self.unnamed_locations:
            self.recipe_repo_data.append(['None', loc, 'None'])
        
        self.recipeconfig_dialogui.tableWidget.setRowCount(len(self.recipe_repo_data)) 

    def set_repo_data(self):
        m = 0
        for data in self.recipe_repo_data:
            self.recipeconfig_dialogui.tableWidget.setItem(m, 0, QTableWidgetItem(data[0]))
            self.recipeconfig_dialogui.tableWidget.setItem(m, 1, QTableWidgetItem(data[1]))
            self.recipeconfig_dialogui.tableWidget.setItem(m, 2, QTableWidgetItem(data[2]))
            m +=1
                 
 
    def collect_recipe_info(self):     
        self.recipe_alias = self.recipeconfig_dialogui.lineEdit.text()
        self.recipe_location = self.recipeconfig_dialogui.lineEdit_2.text()
        self.prefix_to_install = str(self.recipeconfig_dialogui.comboBox.currentText())

        if self.recipe_alias in self.named_sources:
            self.recipeconfig_dialogui.label_5.show()
            self.recipeconfig_dialogui.pushButton_2.setEnabled(False)
        else:
            self.recipeconfig_dialogui.label_5.hide()
            self.recipeconfig_dialogui.pushButton_2.setEnabled(True)
            
        self.recipeconfig_dialogui.pushButton_2.clicked.connect(self.run_recman)

    def run_recman(self):
        print(self.recipe_alias, self.recipe_location, self.prefix_to_install)    
