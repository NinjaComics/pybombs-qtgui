# PyQt API imports
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QDialog, QFrame) 

# Import UI from designer files
from pyqtconvert.module_info import Ui_moduleDialog

class ModuleInfo(QDialog, Ui_moduleDialog):
    def __init__(self):
        super(ModuleInfo, self).__init__()
        self.module_infoui = Ui_moduleDialog()
        self.module_infoui.setupUi(self)
        self.module_infoui.textEdit.setFrameStyle(QFrame.NoFrame)
        self.module_infoui.textEdit_2.setFrameStyle(QFrame.NoFrame)
        self.module_infoui.textEdit.setContentsMargins(0,0,0,0)
        self.module_infoui.textEdit.clear()
