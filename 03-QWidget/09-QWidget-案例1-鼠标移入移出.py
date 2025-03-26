import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class MyLabel(QLabel):
    """自定义标签类,重写enterEvent和leaveEvent事件"""

    def enterEvent(self, *args, **kwargs):
        self.setText("鼠标进入")

    def leaveEvent(self, *args, **kwargs) -> None:
        self.setText("鼠标离开")


app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("鼠标操作的案例1")
window.resize(500, 500)
window.move(400, 250)

label = MyLabel(window)
label.resize(200, 200)
label.move(100, 100)
label.setStyleSheet("background-color: cyan;")

window.show()

sys.exit(app.exec_())
