# PyQt API imports
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QDialog

# Import UI from designer files
from pyqtconvert.progress_bar_dialog import Ui_ProgressBarDialog

class ProgressDialog(QDialog, Ui_ProgressBarDialog):
    def __init__(self):
        super(ProgressDialog, self).__init__()
        self.progress_dialogui = Ui_ProgressBarDialog()
        self.progress_dialogui.setupUi(self)
