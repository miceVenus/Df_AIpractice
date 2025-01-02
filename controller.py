from genericpath import exists
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QWidget
from PyQt5.QtGui import QIcon
from page import Ui_Form
from model import Model

class Controller:
    def __init__(self, model : Model, view : Ui_Form):
        self.model = model
        self.view = view
        
        self.view.Mt5Button_3.clicked.connect(self.GenerateExcert)
        self.view.upload.clicked.connect(self.OpenFileDialog)
        self.view.AckButton.clicked.connect(self.AckOpenFile)
        
    def WarningDialog(self, warning):
        msgBox = QMessageBox(QMessageBox.Icon.Warning, "Warning", warning)
        msgBox.exec_()
        
    def GenerateExcert(self):
        self.view.textOutMt5.clear()
        
        textIn = self.view.textIn.toPlainText()
        modelType = self.view.modelType.currentText()
        
        if not self.judge(textIn):
            return
        
        text = self.model.ProcessTextIn(textIn, modelType)
        self.view.textOutMt5.setText(text)
        
    def OpenFileDialog(self):
        fileDirList, _ = QFileDialog.getOpenFileNames(QWidget(), "多文件选择", '', "*")
        self.selectedFileList = fileDirList
        fileNameList = []
        for fileDir in fileDirList:
            fileNameList.append(self.GetFileName(fileDir) + "\n")
            
        if fileNameList:
            fileNames = "".join(fileNameList)
            self.view.upload.setIcon(QIcon())
            self.view.upload.setText(fileNames)
    
    def AckOpenFile(self):
        modelType = self.view.modelType.currentText()
        self.model.ProcessUploadFile(self.selectedFileList,modelType)
        self.view.upload.setText("")
        self.view.upload.setIcon(QIcon("asset/upload.png"))
            
    def judge(self, textIn):
        
        if textIn == "":
            self.WarningDialog("请输入被摘要文本")
            self.view.textIn.setFocus()
            return False
        
        return True
    
    def GetFileName(self, fileDir):
        fileName = fileDir.split("/")[-1]
        return fileName