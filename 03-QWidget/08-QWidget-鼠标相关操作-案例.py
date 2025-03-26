import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap, QCursor

"""替换鼠标图标、创建一个Label并使其跟随鼠标移动"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.move(350, 250)
        self.setWindowTitle("鼠标相关操作案例")
        self.setMouseTracking(True)  # 启动鼠标追踪，即使不按下鼠标左键，也时刻追踪鼠标位置

        # 检查文件是否存在
        # icon_path = "../Icons/snowflake_128px.ico"

        # icon_path需要改为从当前文件夹中查找
        # 因为当运行脚本时，当前工作目录（CWD）是Python 命令的目录，而不是脚本文件所在的目录。
        icon_path = "./Icons/snowflake_128px.ico"

        pixmap = QPixmap(icon_path).scaled(30, 30)  # 设置鼠标图标大小

        # 如果图片不存在,则使用默认的鼠标图标
        if not pixmap.isNull():
            cursor = QCursor(pixmap)  # 创建鼠标对象
            self.setCursor(cursor)  # 设置鼠标图标
        else:
            print("图片不存在")
            sys.exit()

        label = QLabel(self)
        self.label = label
        label.setText("Moving Label")
        self.label.setStyleSheet("background-color: cyan; font-size: 24px;")

    def mouseMoveEvent(self, mv):
        # 重写QWidget的鼠标移动事件，mv是鼠标移动事件对象
        # print("鼠标移动", mv.localPos())
        label = self.findChild(QLabel)  # 查找QLabel控件,这里返回的是__init__方法中创建的label
        label.move(int(mv.localPos().x()), int(mv.localPos().y()))


app = QApplication(sys.argv)

window = Window()

window.show()
sys.exit(app.exec_())
