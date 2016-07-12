# PyQt API imports
from PyQt5.QtWidgets import QDialog, QFrame

#Pybombs imports
from pybombs import recipe

# Import UI from designer files
from pyqtconvert.module_info_dialog import Ui_ModuleInfoDialog

class ModuleInfoDialog(QDialog, Ui_ModuleInfoDialog):
    def __init__(self, package_name):
        super(ModuleInfoDialog, self).__init__()
        self.moduleinfo_dialogui = Ui_ModuleInfoDialog()
        self.moduleinfo_dialogui.setupUi(self)
        self.moduleinfo_dialogui.plainTextEdit.setFrameStyle(QFrame.NoFrame)
        self.moduleinfo_dialogui.plainTextEdit.setContentsMargins(0, 0, 0, 0)
        self.moduleinfo_dialogui.plainTextEdit.readOnly = True
        self.moduleinfo_dialogui.plainTextEdit.clear()

        rec = recipe.get_recipe(package_name, target='package')

        pkg = 'Package Name: {}'.format(package_name)
        self.moduleinfo_dialogui.plainTextEdit.appendPlainText(pkg)
        self.moduleinfo_dialogui.plainTextEdit.appendPlainText('Dependencies:')
        for item in rec.depends:
            depends = '-{}'.format(item)
            self.moduleinfo_dialogui.plainTextEdit.appendPlainText(depends)
        self.moduleinfo_dialogui.plainTextEdit.appendPlainText('Source')
        source = '{}'.format(rec.get_dict()['source'])
        self.moduleinfo_dialogui.plainTextEdit.appendPlainText(source)
        self.moduleinfo_dialogui.plainTextEdit.appendPlainText('Category')
        self.moduleinfo_dialogui.plainTextEdit.appendPlainText(rec.category)
        if 'description' in rec.get_dict():
            self.moduleinfo_dialogui.plainTextEdit.appendPlainText('Module Description')
            self.moduleinfo_dialogui.plainTextEdit.appendPlainText(rec.description)

        if 'forcebuild' in rec.get_dict():
            self.moduleinfo_dialogui.plainTextEdit.appendPlainText('Forcebuild')
            self.moduleinfo_dialogui.plainTextEdit.appendPlainText('True')




