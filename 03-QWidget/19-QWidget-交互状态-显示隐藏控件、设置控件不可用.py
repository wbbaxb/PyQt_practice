import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Window(QWidget):
    """重写窗口的绘制事件,每次显示窗口时或者窗口大小改变时都会触发"""

    def paintEvent(self, evt):
        print("窗口被绘制了")
        return super().paintEvent(evt)


class Btn(QPushButton):
    """重写按钮的绘制事件,每次显示按钮时或者窗口大小改变时都会触发"""

    def paintEvent(self, evt):
        print("按钮被绘制了")
        return super().paintEvent(evt)


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = Window()
# 2.2设置控件

window.setWindowTitle("交互状态")
window.resize(500, 500)
window.move(400, 250)

btn = Btn(window)
btn.setText("按钮")

btn.pressed.connect(lambda: btn.setVisible(False))  # 按钮功能：使自己不可见

window.show()
# window.setVisible(True)  # show()等方法都是setVisible方法的马甲
# window.setHidden(False)

print(btn.isHidden())  # 当 window没有被绘制时，也是 False
print(btn.isVisible())
print(btn.isVisibleTo(window))  # 父控件如果被显示时，子控件是否跟着被显示

sys.exit(app.exec_())
