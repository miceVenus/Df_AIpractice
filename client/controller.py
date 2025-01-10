from PyQt5.QtWidgets import (QMessageBox, 
                             QFileDialog, 
                             QWidget, 
                             QStackedWidget, 
                             QVBoxLayout,
                             QPushButton,
                             QSizePolicy,
                             )
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QSize
from mainPage.page import Ui_Form as mainPageUi
from model import Model
from settingPage.SettingDialog import SettingDialog
from newsExcertPage.newsExcertPageSetup import Ui_Form as newsExcertPageUi
import os
from typing import Callable

class Controller:
    def __init__(self, model : Model, mainPage, newsExcertPage):
        self.model = model
        self.mainPage = mainPage
        self.newsExcertPage = newsExcertPage
        self.mainPageUi : mainPageUi = mainPage.mainPageUi
        self.newsExcertPageUi : newsExcertPageUi = newsExcertPage.newsExcertPageUi
        self.FileTitleList = []
        self.HtmlTitleList = []
        self.icon_path = os.path.join(os.getcwd(), "asset/")
        self.currentModelType = self.mainPageUi.modelType.currentText()
        
        self.pageStack = QStackedWidget()
        self.pageStack.addWidget(self.mainPage)
        self.pageStack.addWidget(self.newsExcertPage)
        self.InitSlot()
        
    
    def OpenNewsExcert(self):
        self.model.scraper.run()
        self.RenderNewsPage()
        self.pageStack.setCurrentWidget(self.newsExcertPage)
        
    def RenderNewsPage(self):
        self.DeleteLayoutFrom(self.newsExcertPageUi.scrollAreaWidgetContents)
        layout = QVBoxLayout(self.newsExcertPageUi.scrollAreaWidgetContents)
        for value in self.model.scraper.linkDict.values():
            button = self.RenderButton(value[0])
            layout.addWidget(button)

        self.newsExcertPageUi.scrollAreaWidgetContents.setLayout(layout)
        self.SetScrollBarStyle()
                  
    def OpenMainPage(self):
        self.pageStack.setCurrentWidget(self.mainPage)
    
    def OpenSettingDialog(self):
        dialog = SettingDialog(self.model)
        dialog.exec_()
        
    def GenerateExcert(self):
        self.mainPageUi.textOutMt5.clear()
        
        if not self.judgeTextIn():
            return
        
        textIn = self.mainPageUi.textIn.toPlainText()
        self.DisableButton(self.mainPageUi.Mt5Button_3, icon="textout2.png", size=48)
        self.worker = self.Worker(self.model.ProcessTextIn, textIn, self.currentModelType)
        self.worker.finished.connect(self.OnGenerateExcertFinished)
        self.worker.start()
        
    def OnGenerateExcertFinished(self, result):
        self.EnableButton(self.mainPageUi.Mt5Button_3, icon="textout1.png", size=48)
        self.mainPageUi.textOutMt5.setText(result)
        
    def OpenFileDialog(self):
        fileDirList, _ = QFileDialog.getOpenFileNames(QWidget(), "多文件选择", '', "*")
        self.FileTitleList = fileDirList
        fileNameList = []
        for fileDir in fileDirList:
            fileNameList.append(self.GetFileName(fileDir) + "\n")
            
        if fileNameList:
            fileNames = "".join(fileNameList)
            self.mainPageUi.upload.setIcon(QIcon())
            self.mainPageUi.upload.setText(fileNames)
    
    def AckOpenFile(self):
        if not self.judgeSelectedFileList():
            return

        self.DisableButton(self.mainPageUi.AckButton)
        self.worker = self.Worker(self.model.ProcessUploadFile, self.FileTitleList, self.currentModelType)
        self.worker.finished.connect(self.OnAckOpenFileFinished)
        self.worker.start()
        
        self.mainPageUi.upload.setText("")
        self.mainPageUi.upload.setIcon(QIcon(self.icon_path + "upload.png"))
    
    def OnAckOpenFileFinished(self, result):      
        self.EnableButton(self.mainPageUi.AckButton)
        self.FileTitleList.clear()
        
    def RefreshPage(self):        
        self.HtmlTitleList.clear()
        self.DeleteButtonFrom(self.newsExcertPageUi.scrollAreaWidgetContents)
        self.RenderNewsPage()
        if self.newsExcertPageUi.AckButton.isEnabled() is False:
            self.EnableButton(self.newsExcertPageUi.AckButton)
            
        self.pageStack.setCurrentWidget(self.newsExcertPage)
    
    def SubmitHtml(self):
        self.DisableButton(self.newsExcertPageUi.AckButton)
        
        self.worker = self.Worker(self.model.ProcessHTML, self.HtmlTitleList, self.currentModelType)
        self.worker.finished.connect(self.OnSubmitHtmlFinished)
        self.worker.start()
    
    def OnSubmitHtmlFinished(self, result):
        self.RenderExcertNewsPage(result)
    
    def DisableButton(self, button : QPushButton, icon = "suspend.png", size=64):
        button.setIcon(QIcon(self.icon_path + icon))
        button.setIconSize(QSize(size, size))
        button.setEnabled(False)
    
    def EnableButton(self, button : QPushButton, icon = "ack3.png", size=48):
        button.setIcon(QIcon(self.icon_path + icon))
        button.setIconSize(QSize(size, size))
        button.setEnabled(True)
                    
    def RenderExcertNewsPage(self, textList):    
        self.DeleteButtonFrom(self.newsExcertPageUi.scrollAreaWidgetContents)
        layout = self.newsExcertPageUi.scrollAreaWidgetContents.layout()
        for text in textList:
            button = self.RenderButton(text, 128)
            layout.addWidget(button)
    
    def DeleteButtonFrom(self, widget : QWidget):
        components = widget.children()
        for component in components:
            if isinstance(component, QWidget):
                component.setParent(None)
                component.deleteLater()
                
    def RenderButton(self, text, size=64):
        button = QPushButton(f"{text}")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        button.setSizePolicy(sizePolicy)
        button.setFixedHeight(size)
        button.setCursor(QCursor(Qt.PointingHandCursor))
        self.SetButtonStyle(button=button)
        button.clicked.connect(lambda _, button=button: self.ToggleButtonColor(button=button))
        return button
        
    def judgeSelectedFileList(self):
        if self.FileTitleList == []:
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
    
    def DeleteLayoutFrom(self, widget):
        existLayout = widget.layout()
        if existLayout is not None:
            QWidget().setLayout(existLayout)
            
    def judgeIsSelected(self, button : QPushButton):
        backgroundColor = button.styleSheet().split("background-color:")[1].split(";")[0]
        if backgroundColor == "#607D8B":
            return True
        else:
            return False
    
    def GetFileName(self, fileDir):
        fileName = fileDir.split("/")[-1]
        return fileName
    
    def ChangeCurrentModelType(self):
        self.currentModelType = self.mainPageUi.modelType.currentText()
        print(self.currentModelType)
    
    def WarningDialog(self, warning):
        msgBox = QMessageBox(QMessageBox.Icon.Warning, "Warning", warning)
        msgBox.exec_()
        
    def InitSlot(self):
        self.mainPageUi.modelType.currentTextChanged.connect(self.ChangeCurrentModelType)
        self.mainPageUi.Mt5Button_3.clicked.connect(self.GenerateExcert)
        self.mainPageUi.upload.clicked.connect(self.OpenFileDialog)
        self.mainPageUi.AckButton.clicked.connect(self.AckOpenFile)
        self.mainPageUi.setting.clicked.connect(self.OpenSettingDialog)
        self.mainPageUi.news_excert.clicked.connect(self.OpenNewsExcert)
        self.mainPageUi.main_page.clicked.connect(self.OpenMainPage)
        
        self.newsExcertPageUi.AckButton.clicked.connect(self.SubmitHtml)
        self.newsExcertPageUi.setting.clicked.connect(self.OpenSettingDialog)
        self.newsExcertPageUi.news_excert.clicked.connect(self.OpenNewsExcert)
        self.newsExcertPageUi.main_page.clicked.connect(self.OpenMainPage)
        self.newsExcertPageUi.refreshButton.clicked.connect(self.RefreshPage)
        
    class Worker(QThread):
        finished = pyqtSignal(object)
        def __init__(self, function : Callable, *args, **kwargs):
            super().__init__()
            self.function = function
            self.args = args
            self.kwargs = kwargs

        def run(self):
            result = self.function(*self.args, **self.kwargs)
            self.finished.emit(result)
        
    def ToggleButtonColor(self, button : QPushButton):
        if button.text() in self.HtmlTitleList:
            self.HtmlTitleList.remove(button.text())
        else:
            self.HtmlTitleList.append(button.text())
        
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