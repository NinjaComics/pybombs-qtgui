# PyQt API imports
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import (QApplication, QMainWindow, QDialog, QFrame)
from PyQt5.QtGui import QIcon, QPixmap

# Import UI from designer files
from pyqtconvert.preferences_dialog import Ui_PreferencesDialog

class PreferencesDialog(QDialog, Ui_PreferencesDialog):
    def __init__(self):
        super(PreferencesDialog, self).__init__()
        self.preferences_dialogui = Ui_PreferencesDialog()
        self.preferences_dialogui.setupUi(self)
        self.preferences_dialogui.textBrowser.setFrameStyle(QFrame.NoFrame) 
