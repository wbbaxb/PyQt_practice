import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap, QCursor

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("鼠标操作")
window.resize(500, 500)
window.move(400, 250)

label = QLabel(window)
label.setText("label")
label.resize(300, 300)
label.setStyleSheet("background-color: cyan;")

# 图片路径需要改为从当前文件夹中查找
# 因为当运行脚本时，当前工作目录（CWD）是Python 命令的目录，而不是脚本文件所在的目录。
pixmap = QPixmap("./Icons/python_96px.ico")
pixmap = pixmap.scaled(30, 30)  # 重新设置大小，返回新的QPixmap对象
cursor = QCursor(pixmap, 0, 0)  # 自定义图标，0, 0 为热点位置
label.setCursor(cursor)  # 设置鼠标图标为自定义图标cursor

current_cursor = label.cursor()

current_cursor.setPos(100, 100)  # 设置光标位置

# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())
