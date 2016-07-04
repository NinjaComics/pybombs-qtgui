#Python imports
import os.path as op

# PyQt API imports
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QFrame, QFileDialog
from PyQt5.QtCore import Qt

#Pybombs imports
from pybombs import config_manager, recipe
from pybombs.utils import sysutils, subproc

# Import UI from designer files
from pyqtconvert.prefix_manager_dialog import Ui_PrefixConfigDialog


class PrefixConfigDialog(QDialog, Ui_PrefixConfigDialog):
    def __init__(self):
        super(PrefixConfigDialog, self).__init__()
        self.prefixconfig_dialogui = Ui_PrefixConfigDialog()
        self.prefixconfig_dialogui.setupUi(self)
        self.prefixconfig_dialogui.label_4.setAlignment(Qt.AlignCenter
                                                        | Qt.AlignVCenter)
        self.prefix_alias = self.prefixconfig_dialogui.lineEdit.text()
        self.prefix_path = self.prefixconfig_dialogui.lineEdit_2.text()
        self.prefixconfig_dialogui.pushButton_2.clicked.connect(self.get_fname)

    def get_fname(self):
        dirname = str(QFileDialog.getExistingDirectory(self, 'Choose target recipe' \
                                                     'directory'))
        if dirname:
            self.prefixconfig_dialogui.lineEdit_2.setText(dirname)

    def prefix_init(self):
        """
        pybombs prefix init
        """
        # Go, go, go!
        prefix_recipe = recipe.get_recipe('default_prefix', target='prefix',
                                              fail_easy=True)

        # Make sure the directory is writable
        path = op.abspath(op.normpath(self.prefix_path))
        if not sysutils.mkdir_writable(path):
            dir_msg = "Choose a prefix directory with write access"
            self.color_strips(dir_msg, 'red')

        # Make sure that a pybombs directory doesn't already exist
        from pybombs import config_manager
        if op.exists(op.join(path, config_manager.PrefixInfo.prefix_conf_dir)):
            dir_exists = "Prefix directory already exists. Choose a new one"
            self.color_strips(dir_exists, 'red')

        # Add subdirs
        sysutils.require_subdirs(path,
                                 [k for k, v in prefix_recipe.dirs.items() if v])
        self.cfg.load(select_prefix=path)
        self.prefix = self.cfg.get_active_prefix()

        # Create files
        for fname, content in prefix_recipe.files.items():
            sysutils.write_file_in_subdir(path, fname,
                                          prefix_recipe.var_replace_all(content))

        # Register alias
        if self.prefix_alias is not None:
            self.register_alias()

        # If there is no default prefix, make this the default
        if len(self.cfg.get('default_prefix')) == 0:
            if self.prefix_alias is not None:
                new_default_prefix = self.prefix_alias
            else:
                new_default_prefix = prefix_path
            self.cfg.update_cfg_file({'config':
                                      {'default_prefix': new_default_prefix}})

        # Create virtualenv if so desired
        if self.prefix_manager_dialog.checkBox.isChecked():
            #self.log.info("Creating Python virtualenv in prefix...")
            venv_args = ['virtualenv']
            venv_args.append(path)
            subproc.monitor_process(args=venv_args)

        # Update config section
        if len(prefix_recipe.config):
            self.cfg.update_cfg_file(prefix_recipe.config, self.prefix.cfg_file)
            self.cfg.load(select_prefix=path)
            self.prefix = self.cfg.get_active_prefix()

    def register_alias(self):
            if self.prefix_alias is not None:
                if self.prefix is not None and \
                        self.prefix.prefix_aliases.get(self.prefix_alias) is not None:
                    confirm_msg = "Alias `{0}' already exists, overwrite?".format(self.prefix_alias)
                    self.color_strips(confirm_msg, 'red')
                    self.prefixconfig_dialogui.pushButton.setText("Overwrite")
                self.cfg.update_cfg_file({'prefix_aliases': {self.prefix_alias: path}})

    def default_strip(self):
        new_msg = "Pro tip - Choose a prefix directory with write access"
        self.color_strips(new_msg, 'orange')

    def color_strips(self, msg, color):
        if color == 'red':
            self.prefixconfig_dialogui.label_4.setText(msg)
            self.prefixconfig_dialogui.label_4.setStyleSheet(
                "QLabel{background-color:rgb(239, 41, 41); color:rgb(255, 255, 255);}")
        elif color == 'blue':
            self.prefixconfig_dialogui.label_4.setText(msg)
            self.prefixconfig_dialogui.label_4.setStyleSheet(
                "QLabel{background-color:rgb(52, 101, 164); color:rgb(255, 255, 255);}")
        elif color == 'orange':
            self.prefixconfig_dialogui.label_4.setText(msg)
            self.prefixconfig_dialogui.label_4.setStyleSheet(
                "QLabel{background-color:rgb(255, 105, 5); color:rgb(255, 255, 255);}")
