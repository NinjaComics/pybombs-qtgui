# PyQt API imports
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import (QApplication, QMainWindow, QDialog, QFrame, QFileDialog)
from PyQt5.QtGui import QIcon, QPixmap

# Import UI from designer files
from pyqtconvert.new_recipe_dialog import Ui_NewRecipeDialog

class NewRecipeDialog(QDialog, Ui_NewRecipeDialog):
    def __init__(self):
        super(NewRecipeDialog, self).__init__()
        self.newrecipe_dialogui = Ui_NewRecipeDialog()
        self.newrecipe_dialogui.setupUi(self)
        self.newrecipe_dialogui.pushButton.clicked.connect(self.open_filedlg)

    def open_filedlg(self):
        fdlg = QFileDialog()
        fdlg.setFileMode(QFileDialog.AnyFile)
        fdlg.setFilter("Text files (*.txt)")
