# PyQt API imports
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout,
 QLabel, QLineEdit, QVBoxLayout, QWizard, QWizardPage, QDialog, QProgressBar, QCheckBox, QPushButton)
from PyQt5.QtGui import QIcon, QPixmap

# Import UI from designer files
from pyqtconvert.prefix_config import Ui_Wizard
from pyqtconvert.wizard_help import Ui_Dialog 
from pyqtconvert.search_box import Ui_SearchDialog
from pyqtconvert.module_info import Ui_moduleDialog
from pyqtconvert.preferences_dialog import Ui_PreferencesDialog
from pyqtconvert.running_config import Ui_RunningConfigDialog

# Pybombs API imports
from pybombs import config_manager

class ConfigWizard(QWizard, Ui_Wizard):
    def __init__(self):
        super(ConfigWizard, self).__init__()
        self.wizard_ui = Ui_Wizard()
        self.wizard_ui.setupUi(self)
        self.wizard_ui.lineEdit.setPlaceholderText("Enter new prefix alias")
        self.wizard_ui.lineEdit_2.setPlaceholderText("Enter new prefix path")
        self.wizard_ui.lineEdit_2.editingFinished.connect(self.save_config)

    def save_config(self):
        new_prefix_alias = self.wizard_ui.lineEdit.text()
        new_prefix_dir = self.wizard_ui.lineEdit_2.text() 
        new_data = {'prefix_aliases' : {new_prefix_alias: new_prefix_dir}}
        if(self.wizard_ui.checkBox.isChecked):
            default_prefix_data = {'config': {'default_prefix': new_prefix_alias}} 
            cfg_data = config_manager.dict_merge(new_data, default_prefix_data)
        else:
            cfg_data = new_data 
        cfg_file = config_manager.config_manager.local_cfg
        config_manager.config_manager.update_cfg_file(cfg_data, cfg_file)

class ConfigDialog(QDialog,Ui_Dialog):
    def __init__(self):
        super(ConfigDialog, self).__init__()
        self.wizard_dialogui = Ui_Dialog()
        self.wizard_dialogui.setupUi(self)






