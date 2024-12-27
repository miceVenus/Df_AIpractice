from PyQt5.QtWidgets import QMessageBox
from page import Ui_Form
from model import Model

class Controller:
    def __init__(self, model : Model, view : Ui_Form):
        self.model = model
        self.view = view
    
        self.view.Mt5Button_3.clicked.connect(self.EmitMt5)
        
    def WarningDialog(self, warning):
        msgBox = QMessageBox(QMessageBox.Icon.Warning, "Warning", warning)
        msgBox.exec_()
    
    def EmitGpt2(self):
        self.Emit("Gpt2")
    
    def EmitMt5(self):
        self.Emit("Mt5")
        
    def Emit(self, name):
        self.view.textOutMt5.clear()
        
        textIn = self.getMsg()
        
        if self.judge(textIn) == False:
            return
        
        if(name == "Gpt2"):
            text = self.model.ProcessTextRank(textIn)
            self.view.textOutGpt2.setText(text)
        elif(name == "Mt5"):
            text = self.model.ProcessTextMt5(textIn, stopFlag, dampingFactor, excertLength, algorithm)
            self.view.textOutMt5.setText(text)
        
        
        
        
    def getMsg(self):
        
        return (
            self.view.textIn.toPlainText()
        )

    def judge(self, textIn):
        
        if textIn == "":
            self.WarningDialog("请输入被摘要文本")
            self.view.textIn.setFocus()
            return False
        
        return True