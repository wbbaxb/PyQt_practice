import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import QObject


class MyLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setText("10")
        self.move(200, 200)
        self.setStyleSheet("font-size: 25px;")

    def set_sec(self, sec):
        self.setText(str(sec))

    def start_my_timer(self, ms):
        self.timer_id = self.startTimer(ms)

    def timerEvent(self, *args, **kwargs):
        # print('XXX')
        # 1.获取标签内容
        current_sec = int(self.text())
        current_sec -= 1
        self.setText(str(current_sec))

        if current_sec == 0:
            print("停止")
            self.killTimer(self.timer_id)


app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("QObject定时器案例")
window.resize(500, 500)
window.move(400, 250)

label = MyLabel(window)
label.set_sec(5)
label.start_my_timer(500)

window.show()
sys.exit(app.exec_())
