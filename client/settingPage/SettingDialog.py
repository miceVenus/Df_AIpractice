from PyQt5.QtWidgets import QMessageBox, QDialog
from model import Model
from settingPage.setting import Ui_Dialog

class SettingDialog(QDialog):
    def __init__(self, model : Model):
        super().__init__()
        self.model = model
        self.pageUi = Ui_Dialog()
        self.pageUi.setupUi(self)
        self.pageUi.saveButton.clicked.connect(self.SaveSetting)
        self.pageUi.resetButton.clicked.connect(self.ResetSetting)
        self.LoadingSetting()
    
    def LoadingSetting(self):
        settingTuple = self.model.GetConfig()   
        self.pageUi.serverIp.setText(settingTuple[0])
        self.pageUi.serverPort.setText(settingTuple[1])
        self.pageUi.coding.setText(settingTuple[2])
        self.pageUi.outputDir.setText(settingTuple[3])

    def SaveSetting(self):
        serverIp = self.pageUi.serverIp.text()
        if self.judgeIp(serverIp) == False:
            return
        serverPort = self.pageUi.serverPort.text()
        if self.judgePort(serverPort) == False:
            return
        coding = self.pageUi.coding.text()
        outputDir = self.pageUi.outputDir.text()
        settingTuple = (serverIp, serverPort, coding, outputDir)
        self.model.WriteConfig(settingTuple)
        self.close()
    
    def ResetSetting(self):
        defualtSettingTuple = self.model.GetDefaultConfig()
        self.pageUi.serverIp.setText(defualtSettingTuple[0])
        self.pageUi.serverPort.setText(defualtSettingTuple[1])
        self.pageUi.coding.setText(defualtSettingTuple[2])
        self.pageUi.outputDir.setText(defualtSettingTuple[3])
    
    
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
        
    def WarningDialog(self, warning):
        msgBox = QMessageBox(QMessageBox.Icon.Warning, "Warning", warning)
        msgBox.exec_()