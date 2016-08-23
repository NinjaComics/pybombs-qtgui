# Generic imports
import yaml
from pybombs import config_manager

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
        self.runningconfig_dialogui.textEdit_2.clear()
        self.runningconfig_dialogui.pushButton.clicked.connect(self.close_dialog)

        cfg = config_manager.config_manager
        cfg_file_name = cfg.cfg_file_name
        active_prefix = cfg.get_active_prefix()
        global_path = cfg.local_cfg
        prefix_path = active_prefix.cfg_file

        with open(global_path, 'r') as global_cfg:
                global_config = yaml.load(global_cfg)

        with open(prefix_path, 'r') as prefix_cfg:
               prefix_config = yaml.load(prefix_cfg)

        for k, v in global_config.items():
            self.runningconfig_dialogui.textEdit.append(
                '<html><b>{}:</b></html>'.format(k))
            if isinstance(v, dict):
                for vk, vv in v.items():
                    if isinstance(vv, dict):
                        self.runningconfig_dialogui.textEdit.append(
                            '    {}:'.format(vk))
                        for vvk, vvv in vv.items():
                            self.runningconfig_dialogui.textEdit.append(
                                '    {}:'.format(vvk))
                    else:
                        self.runningconfig_dialogui.textEdit.append(
                            '    {} : {}'.format(vk, vv))
            else:
                self.runningconfig_dialogui.textEdit.append(
                    '    {} : {}'.format(k, v))

        for k, v in prefix_config.items():
            self.runningconfig_dialogui.textEdit_2.append(
                '<html><b>{}:</b></html>'.format(k))
            if isinstance(v, dict):
                for vk, vv in v.items():
                    if isinstance(vv, dict):
                        self.runningconfig_dialogui.textEdit_2.append(
                            '    {}:'.format(vk))
                        for vvk, vvv in vv.items():
                            self.runningconfig_dialogui.textEdit_2.append(
                                '        {} : {}'.format(vvk, vvv))
                    else:
                        self.runningconfig_dialogui.textEdit_2.append(
                            '    {} : {}'.format(vk, vv))
            else:
                self.runningconfig_dialogui.textEdit_2.append(
                    '    {} : {}'.format(k, v))

    def close_dialog(self):
        self.close()
