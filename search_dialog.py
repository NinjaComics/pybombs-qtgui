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
import yaml, os

class SearchDialog(QDialog, Ui_SearchDialog):
    def __init__(self):
        super(SearchDialog, self).__init__()
        self.search_dialogui = Ui_SearchDialog()
        self.search_dialogui.setupUi(self)
