from PyQt5.QtWidgets import QMessageBox, QFileDialog, QWidget, QDialog
from PyQt5.QtGui import QIcon
from page import Ui_Form
from model import Model
from client.SettingDialog import SettingDialog
from setting import Ui_Dialog

class Controller:
    def __init__(self, model : Model, viewUi : Ui_Form):
        self.model = model
        self.viewUi = viewUi
        self.selectedFileList = None
        
        self.viewUi.Mt5Button_3.clicked.connect(self.GenerateExcert)
        self.viewUi.upload.clicked.connect(self.OpenFileDialog)
        self.viewUi.AckButton.clicked.connect(self.AckOpenFile)
        self.viewUi.setting.clicked.connect(self.OpenSettingDialog)
        # self.view.news_excert.clicked.connect(self.OpenNewsExcert)
        # self.view.main_page.clicked.connect(self.OpenMainPage)
    
    def OpenSettingDialog(self):
        dialog = SettingDialog(self.model, Ui_Dialog())
        dialog.exec_()
        
    def WarningDialog(self, warning):
        msgBox = QMessageBox(QMessageBox.Icon.Warning, "Warning", warning)
        msgBox.exec_()
        
    def GenerateExcert(self):
        self.viewUi.textOutMt5.clear()
        
        modelType = self.viewUi.modelType.currentText()
        
        if not self.judgeTextIn():
            return
        
        textIn = self.viewUi.textIn.toPlainText()
        text = self.model.ProcessTextIn(textIn, modelType)
        self.viewUi.textOutMt5.setText(text)
        
    def OpenFileDialog(self):
        fileDirList, _ = QFileDialog.getOpenFileNames(QWidget(), "多文件选择", '', "*")
        self.selectedFileList = fileDirList
        fileNameList = []
        for fileDir in fileDirList:
            fileNameList.append(self.GetFileName(fileDir) + "\n")
            
        if fileNameList:
            fileNames = "".join(fileNameList)
            self.viewUi.upload.setIcon(QIcon())
            self.viewUi.upload.setText(fileNames)
    
    def AckOpenFile(self):
        modelType = self.viewUi.modelType.currentText()
        if not self.judgeSelectedFileList():
            return
        self.model.ProcessUploadFile(self.selectedFileList,modelType)
        self.viewUi.upload.setText("")
        self.viewUi.upload.setIcon(QIcon("asset/upload.png"))
        
    def judgeSelectedFileList(self):
        
        if self.selectedFileList is None:
            self.WarningDialog("请上传文件")
            return False
        
        return True
    
    def judgeTextIn(self):
        
        textIn = self.viewUi.textIn.toPlainText()
        if textIn == "":
            self.WarningDialog("请输入被摘要文本")
            self.viewUi.textIn.setFocus()
            return False
        
        return True
    
    def GetFileName(self, fileDir):
        fileName = fileDir.split("/")[-1]
        return fileName