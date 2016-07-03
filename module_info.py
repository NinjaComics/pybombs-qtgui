# PyQt API imports
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QDialog, QFrame) 

# Import UI from designer files
from pyqtconvert.module_info_dialog import Ui_ModuleInfoDialog

class ModuleInfoDialog(QDialog, Ui_ModuleInfoDialog):
    def __init__(self, package_name):
        super(ModuleInfoDialog, self).__init__()
        self.moduleinfo_dialogui = Ui_moduleDialog()
        self.moduleinfo_dialogui.setupUi(self)
        self.moduleinfo_dialogui.textEdit.setFrameStyle(QFrame.NoFrame)
        self.moduleinfo_dialogui.textEdit.setContentsMargins(0,0,0,0)
        self.moduleinfo_dialogui.textEdit.clear()
        
