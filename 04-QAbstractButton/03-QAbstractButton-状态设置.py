import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QRadioButton, QCheckBox
from PyQt5.QtGui import QIcon

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("QAbstractButton-状态设置")
window.resize(500, 500)
window.move(400, 250)


push_button = QPushButton(window)
push_button.setText("Button")
push_button.move(100, 100)

# 通过QSS设置按下时的样式
push_button.setStyleSheet(
    "QPushButton:pressed {background-color: red;}"
)

push_button.setChecked(True)  # 设置为被选中

radio_button = QRadioButton(window)
radio_button.setText("QRadioButton")
radio_button.move(100, 150)
radio_button.setChecked(True)

check_box = QCheckBox(window)
check_box.setText("QCheckBox")
check_box.move(100, 200)
check_box.setEnabled(False)  # 设置不可用，但仍然可被 btn 的槽函数控制是否被选中
check_box.setChecked(True)

btn = QPushButton(window)
btn.setText("切换选中状态")


def slot():
    """槽函数"""
    push_button.toggle()  # 交换 非选中/被选中 状态
    radio_button.toggle()
    # check_box.toggle()
    check_box.setChecked(not check_box.isChecked())  # 等同于 toggle()


btn.pressed.connect(slot)

window.show()

sys.exit(app.exec_())
