# PyQt API imports
from PyQt5.QtWidgets import QDialog

# Import UI from designer files
from pyqtconvert.about_pybombs_dialog import Ui_AboutPybombsDialog

class AboutPybombsDialog(QDialog, Ui_AboutPybombsDialog):
    def __init__(self):
        super(AboutPybombsDialog, self).__init__()
        self.aboutpybombs_dialogui = Ui_AboutPybombsDialog()
        self.aboutpybombs_dialogui.setupUi(self)

        self.aboutpybombs_dialogui.textEdit.hide()
        self.aboutpybombs_dialogui.pushButton_2.hide()
        self.aboutpybombs_dialogui.pushButton.clicked.connect(self.credits_show)
        self.aboutpybombs_dialogui.pushButton_2.clicked.connect(self.credits_hide)
        self.aboutpybombs_dialogui.pushButton_3.clicked.connect(self.about_close)

    def credits_show(self):
        self.aboutpybombs_dialogui.textEdit.show()
        self.aboutpybombs_dialogui.pushButton_2.show()

    def credits_hide(self):
        self.aboutpybombs_dialogui.textEdit.hide()
        self.aboutpybombs_dialogui.pushButton_2.hide()

    def about_close(self):
        self.close()
