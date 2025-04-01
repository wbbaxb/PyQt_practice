import sys
from time import sleep

from PyQt5.QtWidgets import QWidget, QProgressDialog, QApplication, QPushButton, QVBoxLayout
from PyQt5.QtCore import QTimer


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QProgressDialog")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        btn_show = QPushButton("显示进度条")
        btn_show.clicked.connect(self.show_progress_dialog)
        self.main_layout.addWidget(btn_show)

    def show_progress_dialog(self):
        # self.pd = QProgressDialog(self)  # 默认等待4秒后弹出，若在4秒内进度条走完，则不弹出显示
        self.pd = QProgressDialog("进度说明", "取消", 1, 100)  # 两个int为进度条范围

        self.pd.setAutoClose(True)  # 进度条走完后是否自动关闭，默认值为True
        self.pd.setAutoReset(True)  # 进度条走完后是否自动重置，默认值为True

        self.pd.open(lambda: print("对话框被取消"))  # 窗口级别模态窗口

        self.pd.setMinimumDuration(0)  # 设置最小等待时间
        print('self.run')
        self.run()

    def set_progress(self):
        print('set_progress')
        for i in range(1, 101):
            sleep(0.01)
            self.pd.setValue(i)

    def run(self):
        qtimer = QTimer()
        # 启动定时器，1000s后执行set_progress方法
        QTimer.singleShot(1000, self.set_progress)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
