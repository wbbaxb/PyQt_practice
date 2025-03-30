import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import QObject, Qt


class MyObject(QObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.timer_id = None
        self.label = QLabel("1")
        self.label.setAlignment(Qt.AlignCenter)

        self.label.setStyleSheet(
            "font-size: 50px;align: center;font-weight: bold;color: red;"
        )

    def timerEvent(self, evt):
        """
        重写timerEvent方法，当定时器事件发生时，会调用该方法
        """
        val = self.label.text()
        self.label.setText(str(int(val) + 1))


class MyButton(QPushButton):
    def __init__(self, text, color, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setText(text)
        self.setCursor(Qt.PointingHandCursor)
        self.setStyleSheet(
            f"font-size: 30px;background-color: {color};color: white;height:30px;"
        )


app = QApplication(sys.argv)

window = QWidget()
main_layout = QVBoxLayout()
window.setLayout(main_layout)


obj = MyObject()

main_layout.addWidget(obj.label)

btn_start = MyButton("开始", "green")
main_layout.addWidget(btn_start)


def start_timer():
    obj.timer_id = obj.startTimer(1000)


btn_start.clicked.connect(start_timer)

btn_stop = MyButton("停止", "red")
main_layout.addWidget(btn_stop)

btn_stop.clicked.connect(lambda: obj.killTimer(obj.timer_id))


window.setWindowTitle("QObject定时器")
window.resize(500, 500)
window.move(400, 250)


window.show()

sys.exit(app.exec_())
