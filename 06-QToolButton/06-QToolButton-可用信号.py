import sys

from PyQt5.QtWidgets import QApplication, QWidget, QToolButton, QMenu, QAction
from PyQt5.QtGui import QIcon

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("QToolButton-可用信号")
window.resize(500, 500)
window.move(400, 250)

tb = QToolButton(window)
tb.setText("工具")

menu = QMenu(tb)
sub_menu = QMenu()
sub_menu.setTitle("子菜单")
sub_menu.setIcon(QIcon("./Icons/plus_48px.ico"))
action1 = QAction(QIcon("./Icons/menu_48px.ico"), "行为", menu)
action1.setData([1, 2, 3])

# action1.triggered.connect(lambda: print("行为本身发射的信号"))
action2 = QAction(QIcon("./Icons/image_48px.ico"), "行为2", menu)
action2.setData({"key": "value"})

menu.addMenu(sub_menu)
menu.addSeparator() # 添加分隔符
menu.addAction(action1) # 添加行为 行为本身发射信号
menu.addAction(action2) # 添加行为 行为本身发射信号
tb.setMenu(menu)
tb.setPopupMode(QToolButton.MenuButtonPopup) # 设置菜单弹出方式，点击后弹出，有分隔符


def do_action(act):
    print("tb发射的信号", act.data()) # 获取行为的data


tb.triggered.connect(do_action) # 连接tb发射的信号
window.show()

sys.exit(app.exec_())
