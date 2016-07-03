# PyQt API imports
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout,
 QLabel, QLineEdit, QVBoxLayout, QWizard, QWizardPage, QDialog, QProgressBar, QCheckBox, QPushButton)
from PyQt5.QtGui import QIcon, QPixmap

# Import UI from designer files
from pyqtconvert.search_dialog import Ui_SearchDialog

# Pybombs API imports
from pybombs import config_manager
import yaml, os

class SearchDialog(QDialog, Ui_SearchDialog):
    def __init__(self):
        super(SearchDialog, self).__init__()
        self.search_dialogui = Ui_SearchDialog()
        self.search_dialogui.setupUi(self)
        self.search_dialogui.pushButton_2.clicked.connect(self.search_feature)

    def search_feature(self):
        self.close()
