from PyQt5.QtWidgets import QMessageBox, QDialog
from model import Model
from setting import Ui_Dialog

class SettingDialog(QDialog):
    def __init__(self, model : Model, page : Ui_Dialog):
        super().__init__()
        self.model = model
        self.page = page
        self.page.setupUi(self)
        self.page.saveButton.clicked.connect(self.SaveSetting)
        self.page.resetButton.clicked.connect(self.ResetSetting)
        self.LoadingSetting()
    
    def LoadingSetting(self):
        settingTuple = self.model.GetConfig()   
        self.page.serverIp.setText(settingTuple[0])
        self.page.serverPort.setText(settingTuple[1])
        self.page.coding.setText(settingTuple[2])
        self.page.outputDir.setText(settingTuple[3])

    def SaveSetting(self):
        serverIp = self.page.serverIp.text()
        if self.judgeIp(serverIp) == False:
            return
        serverPort = self.page.serverPort.text()
        if self.judgePort(serverPort) == False:
            return
        coding = self.page.coding.text()
        outputDir = self.page.outputDir.text()
        settingTuple = (serverIp, serverPort, coding, outputDir)
        self.model.WriteConfig(settingTuple)
        self.close()
    
    def ResetSetting(self):
        defualtSettingTuple = self.model.GetDefaultConfig()
        self.page.serverIp.setText(defualtSettingTuple[0])
        self.page.serverPort.setText(defualtSettingTuple[1])
        self.page.coding.setText(defualtSettingTuple[2])
        self.page.outputDir.setText(defualtSettingTuple[3])
    
    
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