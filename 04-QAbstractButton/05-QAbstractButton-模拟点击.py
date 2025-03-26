import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("QAbstractButton-模拟点击")
window.resize(500, 500)
window.move(400, 250)

btn = QPushButton(window)
btn.setText("这是按钮1")
btn.pressed.connect(lambda: print("按钮1被点击了"))

# btn.click()  # 模拟用户点击，不带动画
btn.animateClick(2000)  # 模拟持续按下 2000 ms 后再松开，带动画

btn2 = QPushButton(window)
btn2.setText("模拟点击按钮1")
btn2.move(50, 100)


def test():
    # btn.click()
    btn.animateClick(500)  # 动画点击


btn2.pressed.connect(test)

window.show()

sys.exit(app.exec_())
