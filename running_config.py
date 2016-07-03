# PyQt API imports
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QDialog, QFrame)
from PyQt5.QtGui import QIcon, QPixmap

# Import UI from designer files
from pyqtconvert.running_config_dialog import Ui_RunningConfigDialog

class RunningConfigDialog(QDialog, Ui_RunningConfigDialog):
    def __init__(self):
        super(RunningConfigDialog, self).__init__()
        self.runningconfig_dialogui = Ui_RunningConfigDialog()
        self.runningconfig_dialogui.setupUi(self)
        self.runningconfig_dialogui.textEdit.setFrameStyle(QFrame.NoFrame)
        self.runningconfig_dialogui.textEdit_2.setFrameStyle(QFrame.NoFrame)
        self.runningconfig_dialogui.textEdit.setContentsMargins(0,0,0,0)
        self.runningconfig_dialogui.textEdit.clear()

