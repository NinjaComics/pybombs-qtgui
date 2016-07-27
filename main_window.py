#!/usr/bin/python

import sys

# PyQt API imports
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QTableWidgetItem,\
     QDialog
from PyQt5.QtCore import Qt, QThread
from PyQt5.QtGui import QCursor

# Pybombs API imports
from pybombs import config_manager, package_manager, recipe_manager, recipe, \
     install_manager, dep_manager, pb_logging
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
from info_box import InfoDialog
from load_msg import LoadingDialog

#Import thread classes
from pb_threadpool import AWorkerThread, GenericThread, DataGenerator

class PybombsMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        """Pybombs GUI MainWindow
        """
        super(PybombsMainWindow, self).__init__()

        #Setup the UI for MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.log = pb_logging.logger.getChild("PybombsMainWindow")
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

        #List that holds our threads
        self.threadPool = []

        #Searchbox in Toolbar
        self.ui.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.tb_line_edit = QtWidgets.QLineEdit(self)
        self.tb_line_edit.setPlaceholderText("Quick search")
        self.tb_line_edit.setFixedWidth(250)
        self.ui.toolBar.addWidget(self.tb_line_edit)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(
                        QtWidgets.QHeaderView.ResizeToContents)
        self.ui.tableWidget_2.horizontalHeader().setSectionResizeMode(
                        QtWidgets.QHeaderView.ResizeToContents)
        self.ui.tableWidget_3.horizontalHeader().setSectionResizeMode(
                        QtWidgets.QHeaderView.ResizeToContents)
        self.ui.widget_3.hide()

        #Our GenericThread performing the data collection and setting it to TableWidgets
        self.populate_table()

        #It's all signals and slots !!!
        self.ui.action_About_PyBOMBS.triggered.connect(self.about_pybombs_popup)
        self.ui.action_Prefix_Manager.triggered.connect(self.prefix_config_popup)

        self.ui.action_Search.triggered.connect(self.search_box_popup)
        self.ui.action_RunningConfig.triggered.connect(self.running_config_popup)
        self.ui.action_Recipe_Manager.triggered.connect(self.recipe_manager_popup)
        self.ui.action_Apply.triggered.connect(self.apply_changes)
        self.ui.action_Add_Recipe.triggered.connect(self.add_recipes_popup)
        self.ui.action_Choose_Prefix.triggered.connect(self.prefix_chooser_popup)
        self.ui.action_Refresh.triggered.connect(self.populate_table)
        self.tb_line_edit.returnPressed.connect(self.quick_search_highlight)

        #tableWidget's ContextMenu
        self.ui.tableWidget.customContextMenuRequested.connect(
            self.context_menu_apps)

        #tableWidget_2's ContextMenu
        #self.ui.tableWidget_2.customContextMenuRequested.connect(
        #    self.context_menu_baseline)

        #tableWidget_3's ContextMenu
        #self.ui.tableWidget_3.customContextMenuRequested.connect(
        #    self.context_menu_sdk)

    def populate_table(self):
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget_2.setRowCount(0)
        self.ui.tableWidget_3.setRowCount(0)
        self.generate_data = DataGenerator()
        self.threadPool.append(self.generate_data)
        #self.generate_data.indicator.connect(self.loading)
        self.generate_data.indicator.connect(self.loading_popup)
        self.generate_data.data_generator.connect(self.create_table_widget)
        self.threadPool[len(self.threadPool)-1].start()

    def create_table_widget(self, app_packages, baseline_packages, sdk_packages):
        """Creates table with the available packages
        """
        #set generated data to tableWidget
        self.ui.tableWidget.setRowCount(len(app_packages))

        row = 0
        for data in app_packages:
            for column in range(self.ui.tableWidget.columnCount()):
                self.ui.tableWidget.setItem(row, column,
                                            QTableWidgetItem(str(data[column])))
            row += 1

        #set generated data to tableWidget_2
        self.ui.tableWidget_2.setRowCount(len(sdk_packages))

        row = 0
        for data in sdk_packages:
            for column in range(self.ui.tableWidget_2.columnCount()):
                self.ui.tableWidget_2.setItem(row, column,
                                            QTableWidgetItem(str(data[column])))
            row += 1

        #set generated data to tableWidget_3
        self.ui.tableWidget_3.setRowCount(len(baseline_packages))

        row = 0
        for data in baseline_packages:
            for column in range(self.ui.tableWidget_3.columnCount()):
                self.ui.tableWidget_3.setItem(row, column,
                                            QTableWidgetItem(str(data[column])))
            row += 1

    #Methods for Dialogs and Wizard
    def about_pybombs_popup(self):
        self.about_pybombs = AboutPybombsDialog()
        self.about_pybombs.setWindowTitle("About Pybombs")
        self.about_pybombs.show()

    def add_recipes_popup(self):
        self.new_recipe = NewRecipeDialog()
        self.new_recipe.setWindowTitle("Add New Recipe")
        self.new_recipe.show()

    def loading_popup(self, loading_msg):
        self.load_popup = LoadingDialog()
        self.load_popup.loading_dialogui.label_2.setText(loading_msg)
        self.load_popup.setWindowFlags(QtCore.Qt.FramelessWindowHint | Qt.Popup)
        self.load_popup.show()
        self.generate_data.data_done.connect(self.load_popup.close)

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

    def prefix_chooser_popup(self):
        self.ui.statusbar.clearMessage()
        self.choose_prefix = PrefixChooserDialog()
        self.choose_prefix.setWindowFlags(QtCore.Qt.FramelessWindowHint | Qt.Popup)
        self.choose_prefix.show()
        if self.choose_prefix.exec_() == QDialog.Accepted:
            current_prefix = self.cfg.get('default_prefix')
            self.ui.statusbar.showMessage("Active prefix: {}".format(current_prefix), 2000)

    def module_info_popup(self, package_name):
        self.module_info = ModuleInfoDialog(package_name)
        self.module_info.setFixedSize(self.module_info.size())
        self.module_info.setWindowTitle(package_name)
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

    def context_menu_apps(self):
        """Custom ContextMenu that helps us install/update/remove OOT Modules
           from the list displayed on tableWidget
        """
        pm = package_manager.PackageManager()
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

        if pm.installed(package_name):
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
        self.ui.label_3.setText('Preparing packages')
        self.ui.widget_3.show()
        self.final_packages = {'install': self.install_material,
                               'update': self.update_material,
                               'remove': self.remove_material}
        self.log.info('Final packages - {} {}'.format(self.final_packages.values(), self.final_packages.keys()))
        self.worker_thread = AWorkerThread(self.final_packages)
        self.threadPool.append(self.worker_thread)
        self.worker_thread.info_tick.connect(self.init_progress)
        self.worker_thread.progress_tick.connect(self.update_progress)
        self.worker_thread.info_tick.connect(self.info_dialog)
        self.threadPool[len(self.threadPool)-1].start()
        self.final_packages = {}
        self.install_material = []
        self.update_material = []
        self.remove_material = []

    def info_dialog(self, err_msg):
        self.ui.widget_3.hide()
        self.info_box = InfoDialog()
        self.info_box.info_dialogui.label.setText(err_msg)
        self.info_box.setFixedSize(self.info_box.size())
        self.info_box.setWindowFlags(QtCore.Qt.FramelessWindowHint | Qt.Popup)
        self.info_box.info_dialogui.pushButton_2.clicked.connect(self.refresf_finish)
        self.info_box.show()

    def refresf_finish(self):
        self.info_box.close()
        self.populate_table()

    def init_progress(self, init_msg):
        self.ui.label_3.setText(init_msg)
        self.ui.progressBar.setValue(3)

    def update_progress(self, pkg_idx, progress, total, action):
        if action == 'install':
            self.ui.label_3.setText('Installaing {} of {} completed'.format(pkg_idx, total))
        elif action == 'update':
            self.ui.label_3.setText('Updating {} of {} completed'.format(pkg_idx, total))
        elif action == 'remove':
            self.ui.label_3.setText('Removing {} of {} completed'.format(pkg_idx, total))
        self.ui.progressBar.setValue(progress)

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
