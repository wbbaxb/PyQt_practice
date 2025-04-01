import sys

from PyQt5.QtWidgets import QWidget, QProgressBar, QPushButton, QApplication, QVBoxLayout, QButtonGroup, QLabel
from PyQt5.QtCore import Qt, QTimer


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QProgressBar")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.label_message = QLabel()
        self.label_message.setAlignment(Qt.AlignHCenter)
        self.label_message.setFixedHeight(30)
        self.label_message.setStyleSheet("font-size: 16px;color: red;")

        self.main_layout.addWidget(self.label_message)

        self.progressbar = QProgressBar()
        self.main_layout.addWidget(self.progressbar)

        self.btn_group = QButtonGroup()
        btn_group_layout = QVBoxLayout()
        self.main_layout.addLayout(btn_group_layout)

        self.btn_set_value = QPushButton("设置值")
        self.btn_set_value.clicked.connect(
            lambda: self.set_progressbar_value(30))

        self.btn_reset = QPushButton("重置")
        self.btn_reset.clicked.connect(self.reset_progressbar)

        self.btn_set_range = QPushButton("设置范围")
        self.btn_set_range.clicked.connect(self.set_progressbar_range)

        self.btn_set_format = QPushButton("设置格式")
        self.btn_set_format.clicked.connect(self.set_progressbar_format)

        self.btn_set_reverse = QPushButton("反转")
        self.btn_set_reverse.clicked.connect(self.set_progressbar_reverse)

        self.btn_run_progressbar = QPushButton("运行进度条")
        self.btn_run_progressbar.clicked.connect(self.run_progressbar)

        btn_group_layout.addWidget(self.btn_set_value)
        btn_group_layout.addWidget(self.btn_reset)
        btn_group_layout.addWidget(self.btn_set_range)
        btn_group_layout.addWidget(self.btn_set_format)
        btn_group_layout.addWidget(self.btn_set_reverse)
        btn_group_layout.addWidget(self.btn_run_progressbar)
    def set_progressbar_value(self, value):
        self.progressbar.setValue(value)

    def reset_progressbar(self):
        """
        重置进度条,VALUE会变成最小值-1
        """
        self.progressbar.reset()

    def set_progressbar_range(self):
        self.progressbar.setRange(0, 0)  #  范围设置成0-0，则进入繁忙提示

    def set_progressbar_format(self):
        """
        %p 百分比
        %v 当前值
        %m 总值
        可以通过字符串格式化方法来灵活使用
        """

        if self.progressbar.format() == "%p%":  # 默认格式（只显示百分比）
            self.progressbar.setFormat("当前进度 %v / 总进度 %m ")
            self.progressbar.setAlignment(Qt.AlignHCenter)  # 显示在进度条内，水平居中
        else:
            self.progressbar.resetFormat()  # 重置，变回默认值（仅显示百分之）

    def set_progressbar_reverse(self):
        """
        反转
        """
        self.progressbar.setInvertedAppearance(True)

    def run_progressbar(self):
        """
        运行进度条
        """
        self.progressbar.setValue(0)
        self.progressbar.setRange(0, 100)
        self.progressbar.setFormat("当前进度 %v / 总进度 %m ")
        self.progressbar.valueChanged.connect(lambda val: self.label_message.setText(f"当前进度值为{val}"))

        self.timer = QTimer()
        self.timer.timeout.connect(self.change_progressbar_value)
        self.timer.start(100)  # 每隔100ms执行一次

    def change_progressbar_value(self):
        """
        改变进度条的值
        """
        if self.progressbar.value() == self.progressbar.maximum():
            self.timer.stop()
        self.progressbar.setValue(self.progressbar.value() + 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
