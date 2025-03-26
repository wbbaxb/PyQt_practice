import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMenu, QAction

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("QPushbutton-菜单")
window.resize(500, 500)
window.move(400, 250)

btn = QPushButton("按钮", window)

menu = QMenu()
# 子菜单 最近打开
# 行为动作：新建、打开 [分割线] 退出
new_action = QAction(QIcon("./Icons/plus_48px.ico"), "新建")  # 可以同时设置 图标、文字
new_action.triggered.connect(lambda: print("新建文件"))
menu.addAction(new_action)  # 不用设置父对象，因为调用了menu.addAction()

open_action = QAction(QIcon("./Icons/search_48px.ico"), "打开")
open_action.triggered.connect(lambda: print("打开文件"))
menu.addAction(open_action)

open_recent_menu = QMenu()
open_recent_menu.setTitle("最近打开")

file_action = QAction("Python-GUI编程-PyQt5")
file_action.triggered.connect(lambda: print("Python-GUI编程-PyQt5"))
open_recent_menu.addAction(file_action)
menu.addMenu(open_recent_menu)  # 把一个QMenu放在另一个QMenu上，即成为子菜单

menu.addSeparator()  # 添加分割线

exit_action = QAction(QIcon("./Icons/cross_48px.ico"), "关闭")
exit_action.triggered.connect(lambda: exit())
menu.addAction(exit_action)


btn.setMenu(menu)

window.show()
# btn.showMenu()  # 菜单默认展开状态

sys.exit(app.exec_())
