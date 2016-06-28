#Python Libraries
import os

# PyQt API imports
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import (QApplication, QMainWindow, QDialog, QFrame, QTableWidgetItem, QMenu)
from PyQt5.QtGui import QIcon, QPixmap, QCursor
from PyQt5.QtCore import Qt

# Import UI from designer files
from pyqtconvert.recipe_config import Ui_RecipeConfigDialog

#Pybombs API imports
from pybombs import commands, config_manager, recipe_manager
from pybombs.pb_exception import PBException
from pybombs.fetcher import Fetcher

class RecipeConfigDialog(QDialog, Ui_RecipeConfigDialog):
    def __init__(self):
        super(RecipeConfigDialog, self).__init__()
        self.recipeconfig_dialogui = Ui_RecipeConfigDialog()
        self.recipeconfig_dialogui.setupUi(self) 

        self.generate_recipe_data()
        self.set_table_widget()

        self.recipeconfig_dialogui.progressBar.hide()
        self.recipeconfig_dialogui.label_4.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.recipeconfig_dialogui.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.recipeconfig_dialogui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.recipeconfig_dialogui.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.recipeconfig_dialogui.tableWidget.resizeColumnsToContents()
        self.recipeconfig_dialogui.tableWidget.verticalHeader().setVisible(False)
        self.recipeconfig_dialogui.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.recipeconfig_dialogui.lineEdit_2.editingFinished.connect(self.collect_recipe_info) 
        self.recipeconfig_dialogui.pushButton_2.clicked.connect(self.add_recipe_repo)
        self.recipeconfig_dialogui.tableWidget.customContextMenuRequested.connect(self.context_menu)
        self.recipeconfig_dialogui.lineEdit.cursorPositionChanged.connect(self.default_strip)
   
    def generate_recipe_data(self): 
        self.cfg = config_manager.config_manager
        self.recipe_repo_data = [] 
        self.all_locations = self.cfg.get_recipe_locations()
        self.named_sources = self.cfg.get_named_recipe_sources()
        self.named_locations = self.cfg.get_named_recipe_dirs()
        self.unnamed_locations = [x for x in self.all_locations if not x in self.named_locations.values()] 

        for name in self.named_locations.keys():
            if os.path.isdir(self.named_sources.get(name)):
                self.recipe_repo_data.append([name, self.named_locations.get(name), os.path.expanduser(self.named_sources.get(name))])
            else:
                self.recipe_repo_data.append([name, self.named_locations.get(name), self.named_sources.get(name)])

        for loc in self.unnamed_locations:
            self.recipe_repo_data.append(['None', loc, 'None'])
        
        self.recipeconfig_dialogui.tableWidget.setRowCount(len(self.recipe_repo_data)) 

    def set_table_widget(self):
        m = 0
        for data in self.recipe_repo_data:
            for n in range(self.recipeconfig_dialogui.tableWidget.columnCount()):
                self.recipeconfig_dialogui.tableWidget.setItem(m, n, QTableWidgetItem(data[n]))
            m +=1
 
    def collect_recipe_info(self):     
        self.recipe_alias = self.recipeconfig_dialogui.lineEdit.text()
        self.recipe_uri = self.recipeconfig_dialogui.lineEdit_2.text()    

        if self.recipe_alias in self.named_sources:
            alias_msg = 'Ruh oh ! This recipe alias already exists. Overwrite ?'
            self.color_strips(alias_msg, 'red')
        else:
            self.recipeconfig_dialogui.pushButton_2.setEnabled(True)
            
    def add_recipe_repo(self):
        """
        Add recipe location:
        - If a prefix was explicitly selected, install it there
        - Otherwise, use local config file
        - Check alias is not already used

        Works similar to the pybombs.commands.Recipes.add_recipe_dir()
        """
        prefix = self.cfg.get_active_prefix()
        cfg_file = None
        recipe_cache = None
        if self.recipeconfig_dialogui.checkBox.isChecked():
            cfg_file = prefix.cfg_file
            recipe_cache_top_level = os.path.join(prefix.prefix_cfg_dir, self.cfg.recipe_cache_dir)
        else:
            cfg_file = self.cfg.local_cfg
            recipe_cache_top_level = os.path.join(self.cfg.local_cfg_dir, self.cfg.recipe_cache_dir)
        if not os.path.isdir(recipe_cache_top_level):
            #self.log.debug("Recipe cache dir does not exist, creating {0}".format(recipe_cache_top_level))
            os.mkdir(recipe_cache_top_level)
        recipe_cache = os.path.join(recipe_cache_top_level, self.recipe_alias)
        #self.log.debug("Storing new recipe location to {cfg_file}".format(cfg_file=cfg_file))
        assert cfg_file is not None
        assert os.path.isdir(recipe_cache_top_level)
        assert recipe_cache is not None
        assert self.recipe_alias
        # Now make sure we don't already have a cache dir
        if os.path.isdir(recipe_cache):
            #self.log.warn("Cache dir {cdir} for remote recipe location {alias} already exists! Deleting.".format(
            #    cdir=recipe_cache, alias=self.recipe_alias
            #))
            shutil.rmtree(recipe_cache)
        if not os.path.isdir(os.path.normpath(os.path.expanduser(self.recipe_uri))):
            # Let the fetcher download the location
            #self.log.debug("Fetching into directory: {0}/{1}".format(recipe_cache_top_level, self.recipe_alias))
            try:
                Fetcher().fetch_url(self.recipe_uri, recipe_cache_top_level, self.recipe_alias, {}) # No args
            except PBException as ex:
                #self.log.error("Could not fetch recipes: {s}".format(str(ex)))
                fetch_err_msg = 'Oops ! Could not fetch the recipes'
                self.color_strips(fetch_err_msg, 'red')
                return False
        # Write this to config file
        self.cfg.update_cfg_file({'recipes': {self.recipe_alias: self.recipe_uri}}, cfg_file=cfg_file)
        self.generate_recipe_data()
        self.set_table_widget()
        success_msg = 'Recipe added successfully ! '
        self.color_strips(success_msg, 'blue')
        return True
       
    def context_menu(self):
        """Custom ContextMenu that helps us install/update/remove OOT Modules
           from the list displayed on tableView 
        """
        #Following three lines will return the package name irrespective of where
        #mouse click event happens on the row associated with the package
        indexes = self.recipeconfig_dialogui.tableWidget.selectionModel().selectedRows()
        for index in indexes:
            alias = self.recipeconfig_dialogui.tableWidget.model().index(index.row(), 0).data()
        
        #Our custom context menu
        menu = QMenu(self)
        update = menu.addAction("&Update Recipes")
        remove = menu.addAction("&Remove Recipes")

        try:
            if os.path.isdir(self.cfg.get_named_recipe_sources().get(alias)):
                update.setEnabled(False)
            else:
                update.setEnabled(True)
        except:
            update.setEnabled(False)
            
        action = menu.exec_(QCursor.pos()) 

        if (action == update):
            self.update_recipe_repo(alias)

    def update_recipe_repo(self, alias):
        """
        Update a remote recipe location by its alias name.
        """
        uri = self.cfg.get_named_recipe_sources()[alias]
        recipes_dir = self.cfg.get_named_recipe_dirs()[alias]

        cache_dir_top_level, cache_dir = os.path.split(os.path.normpath(recipes_dir))
        # Do actual update
        if not Fetcher().update_src(uri, cache_dir_top_level, cache_dir, {}):
            failure_msg = 'Failed to update {}'.format(alias)
            self.color_strips(failure_msg, 'red')
        else:
            update_msg = 'Successfully updated {}'.format(alias)
            self.color_strips(update_msg, 'blue')
        return True

    def color_strips(self, msg, color):
        if (color == 'red'):
            self.recipeconfig_dialogui.label_4.setText(msg)
            self.recipeconfig_dialogui.label_4.setStyleSheet("QLabel{background-color:rgb(239, 41, 41); color:rgb(255, 255, 255);}")
        elif (color == 'blue'):
            self.recipeconfig_dialogui.label_4.setText(msg)
            self.recipeconfig_dialogui.label_4.setStyleSheet("QLabel{background-color:rgb(52, 101, 164); color:rgb(255, 255, 255);}")
        elif (color == 'orange'):
            self.recipeconfig_dialogui.label_4.setText(msg)
            self.recipeconfig_dialogui.label_4.setStyleSheet("QLabel{background-color:rgb(255, 105, 5); color:rgb(255, 255, 255);}")

    def default_strip(self):
        new_msg = "Add new recipe locations and aliases"
        self.color_strips(new_msg, 'orange')
     
