import sys
from PyQt5.QtWidgets import QApplication, QWidget
from model import Model
from page  import Ui_Form
from controller import Controller

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    model = Model()
    
    ui  = QWidget()
    view = Ui_Form()
    view.setupUi(ui)
    
    controller = Controller(model, view)
    
    ui.show()
    sys.exit(app.exec_())