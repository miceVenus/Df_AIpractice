from PyQt5.QtWidgets import QMessageBox
from page import Ui_Form
from model import Model

class Controller:
    def __init__(self, model : Model, view : Ui_Form):
        self.model = model
        self.view = view
    
        self.view.Gpt2Button.clicked.connect(self.EmitGpt2)
        self.view.Mt5Button.clicked.connect(self.EmitMt5)
        
    def WarningDialog(self, warning):
        msgBox = QMessageBox(QMessageBox.Icon.Warning, "Warning", warning)
        msgBox.exec_()
    
    def EmitGpt2(self):
        self.Emit("Gpt2")
    
    def EmitMt5(self):
        self.Emit("Mt5")
        
    def Emit(self, name):
        self.view.textOutGpt2.clear()
        self.view.textOutMt5.clear()
        
        textIn, stopFlag, dampingFactor, excertLength, algorithm = self.getMsg()
        
        if self.judge(textIn, dampingFactor, excertLength) == False:
            return
        
        if(name == "Gpt2"):
            text = self.model.ProcessTextRank(textIn, stopFlag, dampingFactor, excertLength, algorithm)
            self.view.textOutGpt2.setText(text)
        elif(name == "Mt5"):
            text = self.model.ProcessTextMt5(textIn, stopFlag, dampingFactor, excertLength, algorithm)
            self.view.textOutMt5.setText(text)
        
        
        
        
    def getMsg(self):
        
        return (
            self.view.textIn.toPlainText(),
            self.view.stopBox.isChecked(),
            self.view.dampingLine.text(),
            self.view.excertLine.text(),
            self.view.comboBox.currentText()
        )

    def judge(self, textIn, dampingFactor, excertLength):
        
        if textIn == "":
            self.WarningDialog("请输入被摘要文本")
            self.view.textIn.setFocus()
            return False
        
        try:
            dampingFactor = float(dampingFactor)
            
        except:
            self.WarningDialog("请输入正确的阻尼系数")
            self.view.dampingLine.setFocus()
            return False
            
        try:
            excertLength = int(excertLength)
        except:
            self.WarningDialog("请输入正确的摘要长度")
            self.view.dampingLine.setFocus()
            return False
        
        return True