# PyQt API imports
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QDialog, QFrame)
from PyQt5.QtGui import QIcon, QPixmap

# Import UI from designer files
from pyqtconvert.running_config import Ui_RunningConfigDialog

class RunningConfig(QDialog, Ui_RunningConfigDialog):
    def __init__(self):
        super(RunningConfig, self).__init__()
        self.running_configui = Ui_RunningConfigDialog()
        self.running_configui.setupUi(self)
        self.running_configui.textEdit.setFrameStyle(QFrame.NoFrame)
        self.running_configui.textEdit_2.setFrameStyle(QFrame.NoFrame)
        self.running_configui.textEdit.setContentsMargins(0,0,0,0)
        self.running_configui.textEdit.clear()

