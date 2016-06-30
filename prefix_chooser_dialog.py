# PyQt API imports
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import (QApplication, QMainWindow, QDialog, QFrame, QFileDialog)
from PyQt5.QtGui import QIcon, QPixmap

# Import UI from designer files
from pyqtconvert.prefix_chooser import Ui_PrefixChooserDialog

#Pybombs API imports
from pybombs import config_manager

class PrefixChooserDialog(QDialog, Ui_PrefixChooserDialog):
    def __init__(self):
        super(PrefixChooserDialog, self).__init__()
        self.prefixchooser_dialogui = Ui_PrefixChooserDialog()
        self.prefixchooser_dialogui.setupUi(self)

        self.cfg = config_manager.config_manager

        self.prefixchooser_dialogui.comboBox.addItem(self.cfg.get('default_prefix'))    
        active_prefix = self.cfg.get_active_prefix()
        prefix_list = sorted(list(active_prefix.prefix_aliases.keys()))
        if prefix_list:
            prefix_list.remove(self.cfg.get('default_prefix'))

        for prefix in prefix_list:
            self.prefixchooser_dialogui.comboBox.addItem(prefix)  
        
        self.prefixchooser_dialogui.pushButton.clicked.connect(self.change_prefix)

    def change_prefix(self):
        current_prefix = self.prefixchooser_dialogui.comboBox.currentText()
        cfg_data = {'config': {'default_prefix': current_prefix}}
        cfg_file = self.cfg.local_cfg
        self.cfg.update_cfg_file(cfg_data, cfg_file)
        self.close()

    def current_prefix(self):
        return self.prefixchooser_dialogui.comboBox.currentText()
