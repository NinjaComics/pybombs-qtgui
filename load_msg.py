# PyQt API imports
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog

# Import UI from designer files
from pyqtconvert.loading_dialog import Ui_LoadingDialog

class LoadingDialog(QDialog, Ui_LoadingDialog):
    def __init__(self):
        super(LoadingDialog, self).__init__()
        self.loading_dialogui = Ui_LoadingDialog()
        self.loading_dialogui.setupUi(self)
