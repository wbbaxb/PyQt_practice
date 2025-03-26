import sys

from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("QCheckBox-功能使用")
window.resize(500, 500)
window.move(400, 250)


cb1 = QCheckBox("&Python", window)  # 设置快捷键, & 表示快捷键, 按下Alt+P 就可以选中
cb1.setIcon(QIcon("./Icons/python_96px.ico"))
cb1.setIconSize(QSize(40, 40))
cb1.move(150, 100)
cb1.setTristate(True)  # 支持三态

# print(cb1.isTristate())
cb1.setCheckState(Qt.PartiallyChecked)  # 设置为半选中状态
# cb1.setCheckState(Qt.Checked)  # 设置为完全选中状态

cb2 = QCheckBox("&Java", window)  # 设置快捷键, & 表示快捷键, 按下Alt+J 就可以选中
cb2.setIcon(QIcon("./Icons/Java_96px.ico"))
cb2.setIconSize(QSize(40, 40))
cb2.move(150, 150)

# 添加信号
cb1.toggled.connect(lambda state: print(f'{cb1.text()} 选中状态: {state}'))
cb2.toggled.connect(lambda state: print(f'{cb2.text()} 选中状态: {state}'))

def get_checked_state():
    print(cb1.text(), cb1.isChecked())
    print(cb2.text(), cb2.isChecked())

    # 获取所有选中的item，pyqt中没有专门的api，需要遍历所有子控件
    all_checked = [item.text()
                   for item in window.findChildren(QCheckBox) if item.isChecked()]
    print(f'所有选中的item: {all_checked}')


btn = QPushButton("获取选中状态", window)
btn.move(150, 200)
btn.clicked.connect(get_checked_state)

window.show()
sys.exit(app.exec_())
