# PyQt API imports
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import (QApplication, QMainWindow, QDialog, QFrame)
from PyQt5.QtGui import QIcon, QPixmap

# Import UI from designer files
from pyqtconvert.prefix_manager_dialog import Ui_PrefixConfigDialog


class PrefixConfigDialog(QDialog, Ui_PrefixConfigDialog):
    def __init__(self):
        super(PrefixConfigDialog, self).__init__()
        self.prefixconfig_dialogui = Ui_PrefixConfigDialog()
        self.prefixconfig_dialogui.setupUi(self)
        self.prefixconfig_dialogui.textBrowser.setFrameStyle(QFrame.NoFrame) 
        self.prefixconfig_dialogui.label_4.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)

    def prefix_init(self):
        """
        pybombs prefix init
        """
        def register_alias(alias):
            if alias is not None:
                if self.prefix is not None and \
                        self.prefix.prefix_aliases.get(alias) is not None \
                        and not confirm("Alias `{0}' already exists, overwrite?".format(alias)):
                    self.log.warn('Aborting.')
                    raise PBException("Could not create alias.")
                self.cfg.update_cfg_file({'prefix_aliases': {self.args.alias: path}})
        # Go, go, go!
        try:
            prefix_recipe = get_prefix_recipe(self.args.recipe)
        except PBException as ex:
            self.log.error(str(ex))
            return -1
        if prefix_recipe is None:
            self.log.error("Could not find recipe for `{0}'".format(self.args.recipe))
            return -1
        # Make sure the directory is writable
        path = op.abspath(op.normpath(self.args.path))
        if not sysutils.mkdir_writable(path, self.log):
            self.log.error("Cannot write to prefix path `{0}'.".format(path))
            return -1
        # Make sure that a pybombs directory doesn't already exist
        from pybombs import config_manager
        if op.exists(op.join(path, config_manager.PrefixInfo.prefix_conf_dir)):
            self.log.error("Ignoring. A prefix already exists in `{0}'".format(path))
            return -1
        # Add subdirs
        sysutils.require_subdirs(path, [k for k, v in prefix_recipe.dirs.items() if v])
        self.cfg.load(select_prefix=path)
        self.prefix = self.cfg.get_active_prefix()
        # Create files
        for fname, content in prefix_recipe.files.items():
            sysutils.write_file_in_subdir(path, fname, prefix_recipe.var_replace_all(content))
        # Register alias
        if self.args.alias is not None:
            register_alias(self.args.alias)
        # If there is no default prefix, make this the default
        if len(self.cfg.get('default_prefix')) == 0:
            if self.args.alias is not None:
                new_default_prefix = self.args.alias
            else:
                new_default_prefix = path
            self.cfg.update_cfg_file({'config': {'default_prefix': new_default_prefix}})
        # Create virtualenv if so desired
        if self.args.virtualenv:
            self.log.info("Creating Python virtualenv in prefix...")
            venv_args = ['virtualenv']
            venv_args.append(path)
            subproc.monitor_process(args=venv_args)
        # Install SDK if so desired
        sdk = self.args.sdkname or prefix_recipe.sdk
        if sdk is not None:
            self.log.info("Installing SDK recipe {0}.".format(sdk))
            self.log.info("Reloading configuration...")
            self.cfg.load(select_prefix=path)
            self.prefix = self.cfg.get_active_prefix()
            self.inventory = self.prefix.inventory
            self._install_sdk_to_prefix(sdk)
        # Update config section
        if len(prefix_recipe.config):
            self.cfg.update_cfg_file(prefix_recipe.config, self.prefix.cfg_file)
            self.cfg.load(select_prefix=path)
            self.prefix = self.cfg.get_active_prefix()
        # Install dependencies
        if len(prefix_recipe.depends):
            self.log.info("Installing default packages for prefix...")
            self.log.info("".join(["\n  - {0}".format(x) for x in prefix_recipe.depends]))
            from pybombs import install_manager
            install_manager.InstallManager().install(
                    prefix_recipe.depends,
                    'install', # install / update
                    fail_if_not_exists=False,
                    update_if_exists=False,
                    print_tree=True,
            )
