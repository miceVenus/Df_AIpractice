import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog
from model import Model
from page  import Ui_Form
from setting import Ui_Dialog
from controller import Controller

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    model = Model()
    
    viewUi  = QWidget()
    view = Ui_Form()
    view.setupUi(viewUi)
    
    controller = Controller(model, view)
    
    viewUi.show()
    sys.exit(app.exec_())