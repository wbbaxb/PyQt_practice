import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QToolButton, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt

"""
setToolButtonStyle(Qt.ToolButtonIconOnly)
风格取值：（可用 int 数字简写）
Qt.ToolButtonOnly 仅显示图标  int -> 0
Qt.ToolButtonTextOnly 仅显示文字  int -> 1
Qt.ToolButtonTextBesideIcon  文本显示在图标旁边  int -> 2
Qt.ToolButtonTextUnderIcon  文本显示在图标下方  int -> 3
Qt.ToolButtonFollowStyle  遵循风格  int -> 4
"""

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("QToolButton")
window.resize(500, 500)
window.move(400, 250)

status_bar = window.statusBar()

main_layout = QVBoxLayout()

# 直接这样是不会显示的 ,因为缺少中央窗口部件
# window.setLayout(main_layout)

main_widget = QWidget()  # 使用 QWidget 作为中央窗口部件
main_widget.setLayout(main_layout)  # 将main_layout设置为中央窗口部件的布局

window.setCentralWidget(main_widget)  # 设置中央窗口部件

tb = QToolButton()
tb.setText("工具")
tb.setIcon(QIcon("./Icons/search_48px.ico"))  # 同时设置文本和图标，只显示图标
tb.setIconSize(QSize(150, 150))
tb.move(200, 200)
tb.setToolTip("Query")

main_layout.addWidget(tb)

btn_change_arrow = QPushButton("改变箭头方向")
main_layout.addWidget(btn_change_arrow)

btn_change_auto_raise = QPushButton("改变自动提升")  # 类似于扁平化的效果
main_layout.addWidget(btn_change_auto_raise)


# tb.setToolButtonStyle(Qt.ToolButtonIconOnly)  # 仅显示图标
# tb.setToolButtonStyle(Qt.ToolButtonTextOnly)  # 仅显示文字
# tb.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)  # 文本显示在图标旁边
tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  # 文本显示在图标下方
# tb.setToolButtonStyle(Qt.ToolButtonFollowStyle)  # 遵循风格


def change_style():
    if tb.toolButtonStyle() == Qt.ToolButtonIconOnly:
        tb.setToolButtonStyle(Qt.ToolButtonTextOnly)
    elif tb.toolButtonStyle() == Qt.ToolButtonTextOnly:
        tb.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
    elif tb.toolButtonStyle() == Qt.ToolButtonTextBesideIcon:
        tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
    elif tb.toolButtonStyle() == Qt.ToolButtonTextUnderIcon:
        tb.setToolButtonStyle(Qt.ToolButtonIconOnly)

    status_bar.showMessage('按钮风格已改变:' + str(tb.toolButtonStyle()))


def change_arrow():
    if tb.arrowType() == Qt.NoArrow:
        tb.setArrowType(Qt.UpArrow)
    elif tb.arrowType() == Qt.UpArrow:
        tb.setArrowType(Qt.DownArrow)
    elif tb.arrowType() == Qt.DownArrow:
        tb.setArrowType(Qt.LeftArrow)
    elif tb.arrowType() == Qt.LeftArrow:
        tb.setArrowType(Qt.RightArrow)
    elif tb.arrowType() == Qt.RightArrow:
        tb.setArrowType(Qt.NoArrow)

    status_bar.showMessage('箭头方向已改变:' + str(tb.arrowType()))


def change_auto_raise():
    if tb.autoRaise():
        tb.setAutoRaise(False)
    else:
        tb.setAutoRaise(True)

    status_bar.showMessage('自动提升已改变:' + str(tb.autoRaise()))


tb.clicked.connect(change_style)
btn_change_arrow.clicked.connect(change_arrow)
btn_change_auto_raise.clicked.connect(change_auto_raise)
window.show()

sys.exit(app.exec_())
