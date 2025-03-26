import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QTimer


def set_w1_active():
    w1.setWindowState(Qt.WindowActive)
    print("w1 is active")


app = QApplication(sys.argv)

w1 = QWidget()

w1.setWindowTitle("w1")
w1.resize(500, 500)
w1.move(400, 250)

print(w1.windowState() == Qt.WindowNoState)  # 判断窗口是否处于正常状态,True
# w1.setWindowState(Qt.WindowMinimized)  # 最小化窗口
# w1.setWindowState(Qt.WindowMaximized)  # 最大化窗口

w1.show()

w2 = QWidget()
w2.setWindowTitle("w2")
w2.setWindowState(Qt.WindowActive)  # 设置为活动窗口
w2.show()

# 2秒后，将w1设置为活动窗口
# timer = QTimer()
# timer.timeout.connect(set_w1_active)
# timer.start(2000)  # 启动定时器，2000毫秒后触发(该方法会每隔2000毫秒触发一次)

# 如果只触发一次，则使用QTimer.singleShot
QTimer.singleShot(2000, set_w1_active)


sys.exit(app.exec_())
