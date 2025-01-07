from mainPage.page import Ui_Form
from PyQt5.QtWidgets import QWidget

class MainPage(QWidget):
    def __init__(self):
        super().__init__()
        self.mainPageUi = Ui_Form()
        self.mainPageUi.setupUi(self)
