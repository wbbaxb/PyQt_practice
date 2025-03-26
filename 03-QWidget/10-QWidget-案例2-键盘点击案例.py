import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtCore import Qt


class MyLabel(QLabel):
    """
    自定义标签类,重写keyPressEvent事件
    当键盘按下时，会触发该事件，前提是控件（label）获取焦点
    """

    def keyPressEvent(self, evt):
        if evt.key() == Qt.Key_CapsLock:
            self.setText("CapsLock键被点击了")
        # 注意Ctrl、Alt等修饰键的写法
        if evt.modifiers() == Qt.ControlModifier and evt.key() == Qt.Key_S:
            self.setText("Ctrl + S 被点击了")
        # 多个修饰键之间用按位或来连接
        if (
            evt.modifiers() == Qt.ControlModifier | Qt.ShiftModifier
            and evt.key() == Qt.Key_S
        ):
            self.setText("Ctrl + Shift + S 被点击了")


app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("QWidget案例2")
window.resize(500, 500)
window.move(400, 250)

label = MyLabel(window)
label.resize(200, 200)
label.move(140, 120)
label.setStyleSheet("background-color: cyan;")
# grabKeyboard() 方法实际上是"劫持"了所有的键盘输入，无论界面上哪个控件获得了焦点,label的keyPressEvent事件都会被触发
# label.grabKeyboard()

label.setFocusPolicy(Qt.StrongFocus)  # 设置label获取焦点，这个方法不会劫持键盘输入

button = QPushButton("按钮", window)
button.resize(100, 100)
button.move(400, 300)

window.show()

sys.exit(app.exec_())
