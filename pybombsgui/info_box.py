# PyQt API imports
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout,
 QLabel, QLineEdit, QVBoxLayout, QWizard, QWizardPage, QDialog, QProgressBar, QCheckBox, QPushButton)
from PyQt5.QtGui import QIcon, QPixmap

# Import UI from designer files
from pyqtconvert.info_dialog import Ui_InfoDialog

class InfoDialog(QDialog, Ui_InfoDialog):
    def __init__(self):
        super(InfoDialog, self).__init__()
        self.info_dialogui = Ui_InfoDialog()
        self.info_dialogui.setupUi(self)
        self.info_dialogui.pushButton.clicked.connect(self.infobox_event)

    def infobox_event(self):
        self.close()
