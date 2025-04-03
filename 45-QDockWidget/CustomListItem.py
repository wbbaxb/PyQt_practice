from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QVBoxLayout
import sys
from PyQt5.QtWidgets import QApplication
from Common.flowLayout import FlowLayout


class CustomListItem(QWidget):
    """
    自定义列表项
    """

    def __init__(self, text, parent=None):
        super().__init__(parent)
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)
        self.setLayout(main_layout)

        self.label = QLabel(text)
        self.label.setStyleSheet("font-size: 12px;")

        main_layout.addWidget(self.label)

        h_layout = QHBoxLayout()
        main_layout.addLayout(h_layout)

        # 添加按钮1
        self.button1 = QPushButton("按钮1")
        self.button1.setMinimumHeight(30)
        self.button1.clicked.connect(self.on_button1_clicked)
        h_layout.addWidget(self.button1)

        # 添加按钮2
        self.button2 = QPushButton("按钮2")
        self.button2.setMinimumHeight(30)
        self.button2.clicked.connect(self.on_button2_clicked)
        h_layout.addWidget(self.button2)

    def on_button1_clicked(self):
        print(f"按钮1被点击，项内容: {self.label.text()}")

    def on_button2_clicked(self):
        print(f"按钮2被点击，项内容: {self.label.text()}")


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("流式布局示例")
        self.resize(800, 600)

        # 使用FlowLayout作为主布局
        main_layout = FlowLayout(self)
        main_layout.setSpacing(10)
        self.setLayout(main_layout)

        for i in range(15):
            item_widget = CustomListItem(f"项 {i+1}")
            # 设置固定大小，类似UniformGrid
            item_widget.setFixedSize(200, 100)
            main_layout.addWidget(item_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
