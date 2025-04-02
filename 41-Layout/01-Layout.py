import sys

from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication, QPushButton, QBoxLayout


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("布局管理器")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.test_layout = QVBoxLayout()
        self.btn_layout = QVBoxLayout()
        self.main_layout.addLayout(self.test_layout)
        self.main_layout.addLayout(self.btn_layout)

        self.setup_test_layout()
        self.setup_btn_layout()

    def setup_test_layout(self):
        self.labels = []

        label1 = QLabel()
        label1.setStyleSheet("background-color: blue;")
        self.labels.append(label1)

        label2 = QLabel()
        label2.setStyleSheet("background-color: green;")
        self.labels.append(label2)

        label3 = QLabel()
        label3.setStyleSheet("background-color: red;")
        self.labels.append(label3)

        # 添加widget的同时添加伸缩因子
        self.test_layout.addWidget(label1, 2)
        # 添加空白的伸缩因子
        self.test_layout.addStretch(1)
        self.test_layout.addWidget(label2, 2)
        self.test_layout.addStretch(1)
        self.test_layout.addWidget(label3, 2)

        self.test_layout.setContentsMargins(15, 15, 15, 15)  # 设置外边距，左上右下
        self.test_layout.setSpacing(30)  # 设置内边距

    def setup_btn_layout(self):
        btn_reset_stretch = QPushButton("重置伸缩因子")
        btn_reset_stretch.clicked.connect(self.reset_stretch)
        self.btn_layout.addWidget(btn_reset_stretch)

        btn_change_direction = QPushButton("改变布局方向")
        btn_change_direction.clicked.connect(self.change_direction)
        self.btn_layout.addWidget(btn_change_direction)

        btn_add_row = QPushButton("添加行")
        btn_add_row.clicked.connect(self.add_row)
        self.btn_layout.addWidget(btn_add_row)

    def add_row(self):
        self.test_layout.addRow(QLabel("新行"), 1)

    def change_direction(self):
        """
        改变布局方向
        一共四种方向：
        LeftToRight
        RightToLeft
        TopToBottom
        BottomToTop
        """
        self.test_layout.setDirection(
            QBoxLayout.TopToBottom if self.test_layout.direction() == QBoxLayout.LeftToRight else QBoxLayout.LeftToRight
        )

    def reset_stretch(self):
        """
        重置伸缩因子
        """
        for label in self.labels:
            self.test_layout.setStretchFactor(label, 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
