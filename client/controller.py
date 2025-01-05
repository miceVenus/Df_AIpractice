from PyQt5.QtWidgets import QMessageBox, QFileDialog, QWidget, QDialog
from PyQt5.QtGui import QIcon
from page import Ui_Form
from model import Model
from setting import Ui_Dialog

class Controller:
    def __init__(self, model : Model, view : Ui_Form, setting : Ui_Dialog):
        self.model = model
        self.view = view
        self.setting = setting
        self.selectedFileList = None
        self.settingUi = None
        
        self.view.Mt5Button_3.clicked.connect(self.GenerateExcert)
        self.view.upload.clicked.connect(self.OpenFileDialog)
        self.view.AckButton.clicked.connect(self.AckOpenFile)
        self.view.setting.clicked.connect(self.OpenSettingDialog)
        # self.view.news_excert.clicked.connect(self.OpenNewsExcert)
        # self.view.main_page.clicked.connect(self.OpenMainPage)
        
    def WarningDialog(self, warning):
        msgBox = QMessageBox(QMessageBox.Icon.Warning, "Warning", warning)
        msgBox.exec_()
        
    def GenerateExcert(self):
        self.view.textOutMt5.clear()
        
        modelType = self.view.modelType.currentText()
        
        if not self.judgeTextIn():
            return
        
        textIn = self.view.textIn.toPlainText()
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
    
    def OpenSettingDialog(self):
        settingTuple = self.model.GetConfig()
        self.settingUi = QDialog()
        self.setting.setupUi(self.settingUi)
        
        self.setting.serverIp.setText(settingTuple[0])
        self.setting.serverPort.setText(settingTuple[1])
        self.setting.coding.setText(settingTuple[2])
        self.setting.outputDir.setText(settingTuple[3])
        self.setting.saveButton.clicked.connect(self.SaveSetting)
        self.setting.resetButton.clicked.connect(self.ResetSetting)
        
        self.settingUi.show()
        
    
    def AckOpenFile(self):
        modelType = self.view.modelType.currentText()
        if not self.judgeSelectedFileList():
            return
        self.model.ProcessUploadFile(self.selectedFileList,modelType)
        self.view.upload.setText("")
        self.view.upload.setIcon(QIcon("asset/upload.png"))
    
    def SaveSetting(self):
        serverIp = self.setting.serverIp.text()
        if self.judgeIp(serverIp) == False:
            return
        serverPort = self.setting.serverPort.text()
        if self.judgePort(serverPort) == False:
            return
        coding = self.setting.coding.text()
        outputDir = self.setting.outputDir.text()
        settingTuple = (serverIp, serverPort, coding, outputDir)
        self.model.WriteConfig(settingTuple)
        self.settingUi.close()
    
    def ResetSetting(self):
        defualtSettingTuple = self.model.GetDefaultConfig()
        self.setting.serverIp.setText(defualtSettingTuple[0])
        self.setting.serverPort.setText(defualtSettingTuple[1])
        self.setting.coding.setText(defualtSettingTuple[2])
        self.setting.outputDir.setText(defualtSettingTuple[3])
        
    def judgeSelectedFileList(self):
        
        if self.selectedFileList is None:
            self.WarningDialog("请上传文件")
            return False
        
        return True
    
    def judgeIp(self, Ip):
        try:
            IpList = Ip.split(".")
            if len(IpList) != 4:
                self.WarningDialog("IP格式错误")
                return False
            for ipDice in IpList:
                ipDice = int(ipDice)
                if ipDice < 0 or ipDice > 255:
                    self.WarningDialog("IP格式错误")
                    return False
            return True
        except ValueError:
            self.WarningDialog("IP格式错误")
            return False
    
    def judgePort(self, Port):
        try:
            port = int(Port)
            if port < 0 or port > 65535:
                self.WarningDialog("端口号范围为0-65535")
                return False
            else:
                return True
        except ValueError:
            self.WarningDialog("端口号必须为整数")
            return False
    
    def judgeTextIn(self):
        
        textIn = self.view.textIn.toPlainText()
        if textIn == "":
            self.WarningDialog("请输入被摘要文本")
            self.view.textIn.setFocus()
            return False
        
        return True
    
    def GetFileName(self, fileDir):
        fileName = fileDir.split("/")[-1]
        return fileName