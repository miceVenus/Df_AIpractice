from PyQt5.QtWidgets import QWidget
from newsExcertPage.newsExcertPageSetup import Ui_Form

class NewsExcertPage(QWidget):
    def __init__(self):
        super().__init__()
        self.newsExcertPageUi = Ui_Form()
        self.newsExcertPageUi.setupUi(self)