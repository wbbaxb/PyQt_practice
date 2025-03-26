import sys

from PyQt5.QtWidgets import QApplication, QWidget


class MyWindow(QWidget):
    # 重写QWidget的鼠标移动事件
    def mouseMoveEvent(self, me):
        # print("鼠标移动了", me.globalPos())  # 坐标值为相对整个电脑屏幕
        # print("鼠标移动了", me.localPos())  # 坐标值为相对本QWidget窗口,返回QPoint对象
        # self.statusBar().showMessage("鼠标位置："+str(me.localPos())) # QWidget类中没有状态栏,菜单栏等,所以不能使用
        self.setToolTip("鼠标位置："+str(me.localPos())) # 设置鼠标提示


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

window = MyWindow()

window.setWindowTitle("鼠标跟踪")
window.resize(500, 500)
window.move(400, 250)
window.setMouseTracking(True)  # 启动鼠标追踪，即使不按下鼠标左键，也时刻追踪鼠标位置
print(window.hasMouseTracking())  # 返回True，表示鼠标追踪已启动

# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())
