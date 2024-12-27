import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor

class GlassWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # # 设置窗口的半透明效果
        # self.setWindowFlag(Qt.FramelessWindowHint)  # 隐藏窗口框架
        # self.setAttribute(Qt.WA_TranslucentBackground)  # 背景透明

        # 设置背景色和透明度（模拟毛玻璃效果）
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(QPalette.Window, QColor(255, 255, 255, 160))  # 白色，带透明度
        self.setPalette(p)

        # 创建垂直布局
        layout = QVBoxLayout()

        # 创建上传文件区域
        self.upload_label = QPushButton('点击上传文件')
        self.upload_label.setStyleSheet("padding: 20px; background-color: rgba(255, 255, 255, 0.7); border: 1px solid #ccc;")
        self.upload_label.clicked.connect(self.open_file_dialog)

        # 创建确认按钮
        self.confirm_button = QPushButton('确认')
        self.confirm_button.setStyleSheet("padding: 10px; background-color: #0078D7; color: white; border-radius: 5px;")

        # 将上传区域和按钮添加到布局
        layout.addWidget(self.upload_label)
        layout.addWidget(self.confirm_button)

        # 居中对齐布局内容
        layout.setAlignment(Qt.AlignCenter)

        # 设置主布局
        self.setLayout(layout)

        # 窗口设置
        self.setWindowTitle('文件上传界面')
        self.resize(400, 300)

    def open_file_dialog(self):
        # 弹出文件选择框
        file_name, _ = QFileDialog.getOpenFileName(self, '选择文件', '', 'All Files (*)')
        if file_name:
            self.upload_label.setText(f'已选择: {file_name}')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 设置整个应用程序为半透明背景
    app.setStyle("Fusion")

    window = GlassWindow()
    window.show()
    
    sys.exit(app.exec_())