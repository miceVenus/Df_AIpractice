from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建主窗口的中央小部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # 创建一个垂直布局
        self.layout = QVBoxLayout()
        central_widget.setLayout(self.layout)

        # 创建一个按钮并将其添加到布局中
        self.button = QPushButton("添加标签")
        self.layout.addWidget(self.button)

        # 连接按钮点击事件到槽函数
        self.button.clicked.connect(self.add_label)

    def add_label(self):
        # 创建一个新的标签并将其添加到布局中
        new_label = QLabel("这是一个新标签")
        self.layout.addWidget(new_label)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()