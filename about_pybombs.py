# PyQt API imports
from PyQt5.QtWidgets import QDialog

# Import UI from designer files
from pyqtconvert.about_pybombs_dialog import Ui_AboutPybombsDialog


class AboutPybombsDialog(QDialog, Ui_AboutPybombsDialog):
    def __init__(self):
        super(AboutPybombsDialog, self).__init__()
        self.aboutpybombs_dialogui = Ui_AboutPybombsDialog()
        self.aboutpybombs_dialogui.setupUi(self)
