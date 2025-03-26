import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("内容边距的设定")
window.resize(500, 500)

label = QLabel(window)
label.setText("ABC")
label.resize(300, 300)
# 如果没调用move()，则默认在窗口的左上角,即(0,0)

label.setStyleSheet("background-color: cyan; font-size: 30px;")

label.setContentsMargins(100, 200, 50, 110) # 设置内容边距，分别是左、上、右、下

# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())
