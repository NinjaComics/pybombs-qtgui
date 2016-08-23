#PyQt imports
from PyQt5.QtWidgets import QDialog

#Pybombs API imports
from pybombs import config_manager, recipe
from pybombs.utils import sysutils

# Import UI from designer files
from pyqtconvert.prefix_chooser_dialog import Ui_PrefixChooserDialog

class PrefixChooserDialog(QDialog, Ui_PrefixChooserDialog):
    def __init__(self, parent=None):
        super(PrefixChooserDialog, self).__init__()
        self.prefixchooser_dialogui = Ui_PrefixChooserDialog()
        self.prefixchooser_dialogui.setupUi(self)

        self.cfg = config_manager.config_manager
        self.prefix_info()

        self.prefixchooser_dialogui.pushButton.clicked.connect(self.change_prefix)

    def change_prefix(self):
        current_prefix = self.prefixchooser_dialogui.comboBox.currentText()
        cfg_data = {'config': {'default_prefix': current_prefix}}
        cfg_file = self.cfg.local_cfg
        self.cfg.update_cfg_file(cfg_data, cfg_file)
        self.prefix_info()
        if self.prefixchooser_dialogui.checkBox.isChecked():
            self._write_env_file(prefix_path)
        self.close()

    def prefix_info(self):
        default_prefix = self.cfg.get('default_prefix')
        self.prefixchooser_dialogui.label_3.setText(default_prefix)
        self.prefixchooser_dialogui.comboBox.addItem(default_prefix)

        active_prefix = self.cfg.get_active_prefix()
        prefix_list = sorted(list(active_prefix.prefix_aliases.keys()))
        if prefix_list:
            prefix_list.remove(default_prefix)

        for prefix in prefix_list:
            self.prefixchooser_dialogui.comboBox.addItem(prefix)

    def _write_env_file(self, path):
        prefix_recipe = recipe.get_recipe('default_prefix', target='prefix',
                                          fail_easy=True)
        #if prefix_recipe is None:
            #self.log.error("Could not find recipe for `{0}'".format(self.args.recipe))
            #return False
        if not sysutils.dir_is_writable(path):
            pass
        try:
            for fname, content in prefix_recipe.files.items():
                sysutils.write_file_in_subdir(path, fname,
                                              prefix_recipe.var_replace_all(content))
        except:
            pass
        return True

