import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy
from PyQt5 import QtGui
from model import Model
from mainPage.mainPage import MainPage
from settingPage.setting import Ui_Dialog
from newsExcertPage.newsExcertPage import NewsExcertPage
from controller import Controller



class main:
    
    def __init__(self):
        app = QApplication(sys.argv)
        self.InitResource()
        
        app.aboutToQuit.connect(self.ClearResource)
        sys.exit(app.exec_())
        
    def ClearResource(self):
        self.model.ClearResource()
        
    def InitResource(self):
        
        self.model = Model()
        self.mainPage = MainPage()
        self.newsExcertPage = NewsExcertPage()
        self.controller = Controller(self.model, self.mainPage, self.newsExcertPage)
        self.mainWindow = self.MainWindow(self.controller)
        self.mainWindow.show()
        
    class MainWindow(QMainWindow):
        def __init__(self, controller):
            super().__init__()
            self.resize(1222, 937)
            sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            self.setSizePolicy(sizePolicy)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("asset/text.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.setWindowIcon(icon)
            self.setWindowTitle("文本摘要")
            self.controller = controller
            self.setCentralWidget(self.controller.pageStack)



if __name__ == "__main__":
    main()