from PyQt5.QtWidgets import QMessageBox, QFileDialog, QWidget
from PyQt5.QtGui import QIcon
from page import Ui_Form
from model import Model

class Controller:
    def __init__(self, model : Model, view : Ui_Form):
        self.model = model
        self.view = view
        
        self.view.Mt5Button_3.clicked.connect(self.EmitMt5)
        self.view.upload.clicked.connect(self.OpenFileDialog)
        self.view.AckButton.clicked.connect(self.AckOpenFile)
        
    def WarningDialog(self, warning):
        msgBox = QMessageBox(QMessageBox.Icon.Warning, "Warning", warning)
        msgBox.exec_()
        
    def EmitMt5(self):
        self.view.textOutMt5.clear()
        
        textIn = self.view.textIn.toPlainText()
        
        if not self.judge(textIn):
            return
        
        text = self.model.ProcessTextIn(textIn)
        self.view.textOutMt5.setText(text)
        
    def OpenFileDialog(self):
        fileDirList, _ = QFileDialog.getOpenFileNames(QWidget(), "多文件选择", '', "*")
        self.selectedFileList = fileDirList
        fileNameList = []
        for fileDir in fileDirList:
            fileNameList.append(fileDir.split("/")[-1])
            
        if fileNameList:
            fileNames = "".join(fileNameList)
            self.view.upload.setIcon(QIcon())
            self.view.upload.setText(fileNames)
    
    def AckOpenFile(self):
        self.model.ProcessUploadFile(self.selectedFileList)
        self.view.upload.setText("")
        self.view.upload.setIcon(QIcon("asset/upload.png"))
            
    def judge(self, textIn):
        
        if textIn == "":
            self.WarningDialog("请输入被摘要文本")
            self.view.textIn.setFocus()
            return False
        
        return True