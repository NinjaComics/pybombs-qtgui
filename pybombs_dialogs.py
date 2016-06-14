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
import pyqtconvert.myicons_rc

# Pybombs API imports
from pybombs import config_manager
import yaml, os

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

class SearchDial(QDialog, Ui_SearchDialog):
    def __init__(self):
        super(SearchDial, self).__init__()
        self.search_dialogui = Ui_SearchDialog()
        self.search_dialogui.setupUi(self)

class ModuleInfo(QDialog, Ui_moduleDialog):
    def __init__(self):
        super(ModuleInfo, self).__init__()
        self.module_infoui = Ui_moduleDialog()
        self.module_infoui.setupUi(self)
        self.module_infoui.textEdit.setFrameStyle(QtWidgets.QFrame.NoFrame)
        self.module_infoui.textEdit_2.setFrameStyle(QtWidgets.QFrame.NoFrame)
        self.module_infoui.textEdit.setContentsMargins(0,0,0,0)
        self.module_infoui.textEdit.clear()
        prefix_dir = '/home/ravi/.pybombs/config.yml'
        f = open(prefix_dir)
        getData = yaml.safe_load(f)
        prettyData = yaml.dump(getData, default_flow_style=False)
        self.module_infoui.textEdit.append(str(prettyData))

class PreferencesDialog(QDialog, Ui_PreferencesDialog):
    def __init__(self):
        super(PreferencesDialog, self).__init__()
        self.preferences_dialogui = Ui_PreferencesDialog()
        self.preferences_dialogui.setupUi(self)
        self.preferences_dialogui.textBrowser.setFrameStyle(QtWidgets.QFrame.NoFrame) 

class RunningConfig(QDialog, Ui_RunningConfigDialog):
    def __init__(self):
        super(RunningConfig, self).__init__()
        self.running_configui = Ui_RunningConfigDialog()
        self.running_configui.setupUi(self)
        self.running_configui.textEdit.setFrameStyle(QtWidgets.QFrame.NoFrame)
        self.running_configui.textEdit_2.setFrameStyle(QtWidgets.QFrame.NoFrame)
        self.running_configui.textEdit.setContentsMargins(0,0,0,0)
        self.running_configui.textEdit.clear()
        prefix_dir = '/home/ravi/.pybombs/config.yml'
        f = open(prefix_dir)
        getData = yaml.safe_load(f)
        prettyData = yaml.dump(getData, default_flow_style=False)
        self.running_configui.textEdit.append(str(prettyData))

