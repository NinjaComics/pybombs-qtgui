#!/usr/bin/python

import sys

# PyQt API imports
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QTableWidgetItem
from PyQt5.QtCore import Qt, QThread
from PyQt5.QtGui import QCursor

# Pybombs API imports
from pybombs import config_manager, package_manager, recipe_manager, recipe, \
     install_manager, dep_manager
from pybombs.recipe import Recipe

# Import UI from designer generated python files
from pyqtconvert.pybombs_main_window import Ui_MainWindow
from about_pybombs import AboutPybombsDialog
from search_box import SearchDialog
from module_info import ModuleInfoDialog
from prefix_config import PrefixConfigDialog
from recipe_config import RecipeConfigDialog
from new_recipe import NewRecipeDialog
from prefix_chooser import PrefixChooserDialog
from running_config import RunningConfigDialog
from progress_bar import ProgressDialog

class GenericThread(QThread):
    def __init__(self, function, *args, **kwargs):
        QThread.__init__(self)
        self.function = function
        self.args = args
        self.kwargs = kwargs

    def __del__(self):
        self.wait()

    def run(self):
        self.function(*self.args, **self.kwargs)
        return

class WorkerThread(QtCore.QThread):
    progress_tick = QtCore.pyqtSignal(int, name="package")

    def __init__(self, package_list):
        QtCore.QThread.__init__(self)
        self.package_list = package_list

    def run(self):
        instaman = install_manager.InstallManager()

        if 'install' in self.package_list:
            install_list = self.package_list.get('install')
            print(install_list)
            try:
                for package in install_list:
                    install = []
                    install.append(package)
                    instaman.install(install, 'install')
                    install.remove(package)
                    progress = (install_list.index(package)+1)/len(
                        install_list)*100.0
                    print(progress)
                    self.progress_tick.emit(progress, package)
            except:
                pass

        if 'update' in self.package_list:
            update_list = self.package_list.get('update')
            try:
                for package in update_list:
                    update = []
                    update.append(package)
                    instaman.install(self.package_list.get('update'),
                                     'update', update_if_exists=True)
                    update.remove(package)
                    progress = (update_list.index(package)+1)/len(
                        update_list)*100.0
                    self.progress_tick.emit(progress, package)
            except:
                pass

        if 'remove' in self.package_list:
            try:
                remove_list = self.package_list.get('remove')
                pm = package_manager.PackageManager()
                dep_tree = dep_manager.DepManager().make_dep_tree(
                    self.package_list.get('remove'),
                    lambda x: bool(x in self.package_list.get('remove')))
                remove = reversed(dep_tree.serialize())
                ### Remove packages
                for pkg in remove:
                    print(pkg)
                    #Uninstall:
                    pm.uninstall(pkg)
                    progress = (remove_list.index(pkg)+1)/len(remove_list)*100.0
                    print(progress)
                    #Remove entry from inventory:
                    self.inventory.remove(pkg)
                    self.inventory.save()
            except:
                pass
        return

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

        #self.ui.tableWidget_2.setVisible(False)
        #creating an empty dictionary and few lists which later goes into
        #install_manager.py with full list of packages to install/update/remove
        self.final_packages = {}
        self.install_material = []
        self.update_material = []
        self.remove_material = []

        #Init lists used for generating data for tableWidgets
        self.app_package_data = []
        self.sdk_package_data = []
        self.base_package_data = []
        self.app_package_list = []
        self.sdk_package_list = []

        #List that holds our threads
        self.threadPool = []

        #Searchbox in Toolbar
        self.ui.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.tb_line_edit = QtWidgets.QLineEdit(self)
        self.tb_line_edit.setPlaceholderText("Quick search")
        self.tb_line_edit.setFixedWidth(250)
        self.ui.toolBar.addWidget(self.tb_line_edit)

        #TableWidget's Properties (Application Packages)
        self.ui.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeToContents)
        self.ui.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.tableWidget.horizontalHeader().setStyleSheet(
            "QHeaderView {font: bold; color:gray; border: 0px; padding: 0px;}")
        self.ui.tableWidget.setAlternatingRowColors(True)
        self.ui.tableWidget.setStyleSheet(
            "QTableWidget {alternate-background-color: rgb(211, 215, 207);" \
            "background-color: white;}")
        self.ui.tableWidget.setStyleSheet(
            "QTableWidget::item {border: 0px; padding-left: 10px;" \
            "padding-right: 40px;}")

        #TableWidget's ContextMenu
        self.ui.tableWidget.customContextMenuRequested.connect(self.context_menu)

        #TableWidget_2's Properties (Baseline Packages)
        self.ui.tableWidget_2.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeToContents)
        self.ui.tableWidget_2.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.tableWidget_2.horizontalHeader().setStyleSheet(
            "QHeaderView {font: bold; color:gray; border: 0px; padding: 0px;}")
        self.ui.tableWidget_2.setAlternatingRowColors(True)
        self.ui.tableWidget_2.setStyleSheet(
            "QTableWidget {alternate-background-color: rgb(211, 215, 207);" \
            "background-color: white;}")
        self.ui.tableWidget_2.setStyleSheet(
            "QTableWidget::item {border: 0px; padding-left: 10px;" \
            "padding-right: 40px;}")

        #TableWidget_3's Properties (SDK and Prefix specific Packages)
        self.ui.tableWidget_3.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeToContents)
        self.ui.tableWidget_3.setContextMenuPolicy(Qt.CustomContextMenu) #Custom context menu
        self.ui.tableWidget_3.horizontalHeader().setStyleSheet(
            "QHeaderView {font: bold; color:gray; border: 0px; padding: 0px;}")
        self.ui.tableWidget_3.setAlternatingRowColors(True)
        self.ui.tableWidget_3.setStyleSheet(
            "QTableWidget {alternate-background-color: rgb(211, 215, 207);" \
            "background-color: white;}")
        self.ui.tableWidget_3.setStyleSheet(
            "QTableWidget::item {border: 0px; padding-left: 10px;" \
            "padding-right: 40px;}")

        #tableWidget_3's ContextMenu
        #self.ui.tableWidget_3.customContextMenuRequested.connect(self.context_menu)


        #Our GenericThread performing the data collection and setting it to TableWidgets
        # generic thread using signal
        #self.ui.tableWidget.clear()
        #self.ui.tableWidget_2.clear()
        #self.ui.tableWidget_3.clear()
        self.threadPool.append(GenericThread(self.generate_table_data))
        self.threadPool[len(self.threadPool)-1].start()

        #It's all signals and slots !!!
        self.ui.action_About_PyBOMBS.triggered.connect(self.about_pybombs_popup)
        self.ui.action_Prefix_Manager.triggered.connect(self.prefix_config_popup)

        self.ui.action_Search.triggered.connect(self.search_box_popup)
        self.ui.action_RunningConfig.triggered.connect(self.running_config_popup)
        self.ui.action_Recipe_Manager.triggered.connect(self.recipe_manager_popup)
        self.ui.action_Apply.triggered.connect(self.apply_changes)
        self.ui.action_Add_Recipe.triggered.connect(self.add_recipes_popup)
        self.ui.action_Choose_Prefix.triggered.connect(self.prefix_chooser_popup)
        self.tb_line_edit.returnPressed.connect(self.quick_search_highlight)

    #Here's where we generate the source data for tableWidget
    def generate_table_data(self):
        """Generate data from Pybombs backend to feed to the Model
        """
        self.pm = package_manager.PackageManager()

        list_recipes = sorted(list(recipe_manager.recipe_manager.list_all()))

        for pkg_name in list_recipes:
            module = Recipe(recipe_manager.recipe_manager.
                            get_recipe_filename(pkg_name))
            if module.target == 'prefix':
                self.sdk_package_list.append(pkg_name)
            elif module.target == 'sdk':
                self.sdk_package_list.append(pkg_name)
            elif module.target == 'package':
                self.app_package_list.append(pkg_name)

        for pkg in self.sdk_package_list:
            rec = Recipe(recipe_manager.recipe_manager.get_recipe_filename(pkg))
            if rec.target == 'prefix':
                self.sdk_package_data.append([pkg, 'Prefix Specific Packages'])
            elif rec.target == 'sdk':
                self.sdk_package_data.append([pkg, 'SDK Packages'])

        for oot_module in self.app_package_list:
            rec = recipe.get_recipe(oot_module, target='package', fail_easy=True)
            if rec.category == 'baseline':
                if self.pm.installed(oot_module):
                    self.base_package_data.append([oot_module, 'Installed'])
                else:
                    self.base_package_data.append([oot_module, 'Not Installed'])
            else:
                if 'description' in rec.get_dict():
                    if self.pm.installed(oot_module):
                        self.app_package_data.append([oot_module,
                                               rec.get_dict()['category'],
                                               'Installed',
                                               rec.get_dict()['description']])
                    else:
                        self.app_package_data.append([oot_module,
                                               rec.get_dict()['category'],
                                               'Not Installed',
                                               rec.get_dict()['description']])
                else:
                    if self.pm.installed(oot_module):
                        self.app_package_data.append([oot_module,
                                               rec.get_dict()['category'],
                                               'Installed',
                                               'No description available'])
                    else:
                        self.app_package_data.append([oot_module,
                                               rec.get_dict()['category'],
                                               'Not Installed',
                                               'No description available'])

        #set generated data to tableWidget
        self.ui.tableWidget.setRowCount(len(self.app_package_data))

        row = 0
        for data in self.app_package_data:
            for column in range(self.ui.tableWidget.columnCount()):
                self.ui.tableWidget.setItem(row, column,
                                            QTableWidgetItem(str(data[column])))
            row += 1

        #set generated data to tableWidget
        self.ui.tableWidget_2.setRowCount(len(self.sdk_package_data))

        row = 0
        for data in self.sdk_package_data:
            for column in range(self.ui.tableWidget_2.columnCount()):
                self.ui.tableWidget_2.setItem(row, column,
                                            QTableWidgetItem(str(data[column])))
            row += 1

        #set generated data to tableWidget
        self.ui.tableWidget_3.setRowCount(len(self.base_package_data))

        row = 0
        for data in self.base_package_data:
            for column in range(self.ui.tableWidget_3.columnCount()):
                self.ui.tableWidget_3.setItem(row, column,
                                            QTableWidgetItem(str(data[column])))
            row += 1

        self.cfg = config_manager.config_manager
        if len(self.cfg.get('default_prefix')) == 0:
            self.prefix_config_popup() #Pybombs preferences dialog

        if not self.app_package_data:
            self.recipe_manager_popup() #Pybombs recipe manager


    #Methods for Dialogs and Wizard
    def about_pybombs_popup(self):
        self.about_pybombs = AboutPybombsDialog()
        self.about_pybombs.setWindowTitle("About Pybombs")
        self.about_pybombs.show()

    def add_recipes_popup(self):
        self.new_recipe = NewRecipeDialog()
        self.new_recipe.setWindowTitle("Add New Recipe")
        self.new_recipe.show()

    def prefix_config_popup(self):
        self.prefix_conf = PrefixConfigDialog()
        self.prefix_conf.setWindowTitle("Pybombs Prefix Manager")
        self.prefix_conf.setFixedSize(self.prefix_conf.size())
        self.prefix_conf.setModal(True)
        self.prefix_conf.show()

    def recipe_manager_popup(self):
        self.recipe_conf = RecipeConfigDialog()
        self.recipe_conf.setWindowTitle("Pybombs Recipe Manager")
        self.recipe_conf.show()

    def search_box_popup(self):
        self.search_box = SearchDialog()
        self.search_box.setWindowFlags(QtCore.Qt.FramelessWindowHint | Qt.Popup)
        self.search_box.show()

    def progress_popup(self):
        self.progress = ProgressDialog()
        self.progress.setWindowFlags(QtCore.Qt.FramelessWindowHint | Qt.Popup)
        self.progress.show()

    def prefix_chooser_popup(self):
        self.choose_prefix = PrefixChooserDialog()
        self.choose_prefix.setWindowFlags(QtCore.Qt.FramelessWindowHint | Qt.Popup)
        self.choose_prefix.show()

    def module_info_popup(self, package_name):
        self.module_info = ModuleInfoDialog(package_name)
        self.module_info.setFixedSize(self.module_info.size())
        self.module_info.show()

    def running_config_popup(self):
        self.running_config = RunningConfigDialog()
        self.running_config.show()

    def quick_search_highlight(self):
        search_items = self.ui.tableWidget.findItems(self.tb_line_edit.text(),
                                                     QtCore.Qt.MatchContains)
        for item in search_items:
            self.ui.tableWidget.selectRow(item.row())
            self.ui.tableWidget.setStyleSheet(
                "QTableWidget::item:selected {background-color: gray;}")
            self.ui.tableWidget.setStyleSheet(
                "QTableWidget::item {border: 0px; padding-left: 10px;" \
                "padding-right: 40px;}")
            self.tb_line_edit.clear()

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
        discard = menu.addAction("&Discard Changes")
        menu.addSeparator()
        module_info = menu.addAction("&Module Info")

        discard.setEnabled(False)

        if self.pm.installed(package_name):
            install.setEnabled(False)
        else:
            update.setEnabled(False)
            remove.setEnabled(False)

        if package_name in self.install_material:
            install.setEnabled(False)
            discard.setEnabled(True)

        if package_name in self.update_material:
            update.setEnabled(False)
            discard.setEnabled(True)

        if package_name in self.remove_material:
            remove.setEnabled(False)
            discard.setEnabled(True)

        action = menu.exec_(QCursor.pos())

        #Here's where our context menu gets some work to do
        if action == install:
            self.install_material.append(package_name)

        if action == update:
            self.update_material.append(package_name)

        if action == remove:
            self.remove_material.append(package_name)

        if action == discard:
            if package_name in self.install_material:
                self.install_material.remove(package_name)

            if package_name in self.update_material:
                self.update_material.remove(package_name)

            if package_name in self.remove_material:
                self.remove_material.remove(package_name)

        if (self.install_material or self.update_material or self.remove_material):
            self.ui.action_Apply.setEnabled(True)
        else:
            self.ui.action_Apply.setEnabled(False)

        if action == module_info:
            self.module_info_popup(package_name)

    def apply_changes(self):
        self.final_packages = {'install': self.install_material,
                               'update': self.update_material,
                               'remove': self.remove_material}
        print(self.final_packages.values(), self.final_packages.keys())
        self.worker_thread = WorkerThread(self.final_packages)
        self.threadPool.append(self.worker_thread)
        self.threadPool[len(self.threadPool)-1].start()

        self.worker_thread.progress_tick.connect(self.progress_popup.progress.progressBar.setValue)

        self.threadPool.append(GenericThread(self.generate_table_data))
        self.threadPool[len(self.threadPool)-1].start()


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
