from operator import iconcat
from PyQt5.QtWidgets import (QMessageBox, 
                             QFileDialog, 
                             QWidget, 
                             QStackedWidget, 
                             QVBoxLayout,
                             QPushButton,
                             QSizePolicy
                             )
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtCore import Qt, QStandardPaths
from mainPage.page import Ui_Form as mainPageUi
from model import Model
from settingPage.SettingDialog import SettingDialog
from newsExcertPage.newsExcertPageSetup import Ui_Form as newsExcertPageUi
import os

class Controller:
    def __init__(self, model : Model, mainPage, newsExcertPage):
        self.model = model
        self.mainPage = mainPage
        self.newsExcertPage = newsExcertPage
        self.mainPageUi : mainPageUi = mainPage.mainPageUi
        self.newsExcertPageUi : newsExcertPageUi = newsExcertPage.newsExcertPageUi
        self.selectedFileList = None
        self.icon_path = os.path.join(os.getcwd(), "asset/upload.png")
        
        self.pageStack = QStackedWidget()
        self.pageStack.addWidget(self.mainPage)
        self.pageStack.addWidget(self.newsExcertPage)
        self.InitSlot()
        
    
    def OpenNewsExcert(self):
        self.model.scraper.run()
        existLayout = self.newsExcertPageUi.scrollAreaWidgetContents.layout()
        if existLayout is not None:
            QWidget().setLayout(existLayout)

        layout = QVBoxLayout(self.newsExcertPageUi.scrollAreaWidgetContents)
        for value in self.model.scraper.linkDict.values():
            button = QPushButton(f"{value[0]}")
            sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
            button.setSizePolicy(sizePolicy)
            button.setFixedHeight(64)
            button.setCursor(QCursor(Qt.PointingHandCursor))
            self.SetButtonStyle(button=button)
            layout.addWidget(button)
            button.clicked.connect(lambda _, button=button: self.ToggleButtonColor(button=button))
        
        self.newsExcertPageUi.scrollAreaWidgetContents.setLayout(layout)
        self.SetScrollBarStyle()
        self.pageStack.setCurrentWidget(self.newsExcertPage)
        
    def OpenMainPage(self):
        self.pageStack.setCurrentWidget(self.mainPage)
    
    def OpenSettingDialog(self):
        dialog = SettingDialog(self.model)
        dialog.exec_()
        
    def WarningDialog(self, warning):
        msgBox = QMessageBox(QMessageBox.Icon.Warning, "Warning", warning)
        msgBox.exec_()
        
    def GenerateExcert(self):
        self.mainPageUi.textOutMt5.clear()
        
        modelType = self.mainPageUi.modelType.currentText()
        
        if not self.judgeTextIn():
            return
        
        textIn = self.mainPageUi.textIn.toPlainText()
        text = self.model.ProcessTextIn(textIn, modelType)
        self.mainPageUi.textOutMt5.setText(text)
        
    def OpenFileDialog(self):
        fileDirList, _ = QFileDialog.getOpenFileNames(QWidget(), "多文件选择", '', "*")
        self.selectedFileList = fileDirList
        fileNameList = []
        for fileDir in fileDirList:
            fileNameList.append(self.GetFileName(fileDir) + "\n")
            
        if fileNameList:
            fileNames = "".join(fileNameList)
            self.mainPageUi.upload.setIcon(QIcon())
            self.mainPageUi.upload.setText(fileNames)
    
    def AckOpenFile(self):
        modelType = self.mainPageUi.modelType.currentText()
        if not self.judgeSelectedFileList():
            return
        self.model.ProcessUploadFile(self.selectedFileList,modelType)
        self.mainPageUi.upload.setText("")
        self.mainPageUi.upload.setIcon(QIcon(self.icon_path))
    
    def SubmitHTML(self):
        self.WarningDialog("尚未实现")
        for button in self.newsExcertPageUi.scrollAreaWidgetContents.findChildren(QPushButton):
            if self.judgeIsSelected(button):
                print(button.text())
    
    def judgeSelectedFileList(self):
        
        if self.selectedFileList is None:
            self.WarningDialog("请上传文件")
            return False
        
        return True
    
    def judgeTextIn(self):
        
        textIn = self.mainPageUi.textIn.toPlainText()
        if textIn == "":
            self.WarningDialog("请输入被摘要文本")
            self.mainPageUi.textIn.setFocus()
            return False
        
        return True
    
    def judgeIsSelected(self, button : QPushButton):
        backgroundColor = button.styleSheet().split("background-color:")[1].split(";")[0]
        if backgroundColor == "#607D8B":
            return True
        else:
            return False
    
    def GetFileName(self, fileDir):
        fileName = fileDir.split("/")[-1]
        return fileName
    
    def InitSlot(self):
        self.mainPageUi.Mt5Button_3.clicked.connect(self.GenerateExcert)
        self.mainPageUi.upload.clicked.connect(self.OpenFileDialog)
        self.mainPageUi.AckButton.clicked.connect(self.AckOpenFile)
        self.mainPageUi.setting.clicked.connect(self.OpenSettingDialog)
        self.mainPageUi.news_excert.clicked.connect(self.OpenNewsExcert)
        self.mainPageUi.main_page.clicked.connect(self.OpenMainPage)
        
        self.newsExcertPageUi.AckButton.clicked.connect(self.SubmitHTML)
        self.newsExcertPageUi.setting.clicked.connect(self.OpenSettingDialog)
        self.newsExcertPageUi.news_excert.clicked.connect(self.OpenNewsExcert)
        self.newsExcertPageUi.main_page.clicked.connect(self.OpenMainPage)
        
    def ToggleButtonColor(self, button : QPushButton):
        backgroundColor = button.styleSheet().split("background-color:")[1].split(";")[0]
        if backgroundColor == "#607D8B":
            button.setStyleSheet("""border:solid;\n
                                 border-radius:5px;
                                 background-color:#F5F5F5;
                                 border-color:#BDBDBD;
                                 border-width:2px;
                                 text-align: left;
                                 font:24px;
                                 padding-left: 20px;""")
        else:
            button.setStyleSheet("""border:solid;\n
                                 border-radius:5px;
                                 background-color:#607D8B;
                                 border-color:#BDBDBD;
                                 border-width:2px;
                                 text-align: left;
                                 font:24px;
                                 color:#F5F5F5;
                                 padding-left: 20px;""")
    
    def SetScrollBarStyle(self):
        self.newsExcertPageUi.scrollArea.setStyleSheet("""QScrollBar:vertical {
                                                            border: 1px solid #999999;
                                                            background: #f0f0f0;
                                                            width: 12px;
                                                            margin: 0px 0px 0px 0px;
                                                        }
                                                        QScrollBar::handle:vertical {
                                                            background: #757575;
                                                            min-height: 20px;
                                                            border-radius: 4px;
                                                        }
                                                        QScrollBar::sub-line:vertical, QScrollBar::add-line:vertical{
                                                            background: #757575;
                                                            height: 0px;
                                                        }
                                                        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                                                            background: none;
                                                        }""")
    def SetButtonStyle(self, button : QPushButton):
        button.setStyleSheet("""border:solid;
                                 border-radius:5px;
                                 background-color:#F5F5F5;
                                 border-color:#BDBDBD;
                                 border-width:2px;
                                 font:24px;
                                 text-align: left;
                                 padding-left: 20px;""")