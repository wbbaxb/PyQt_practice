import sys

from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QButtonGroup

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("QButtonGroup-信号")
window.resize(500, 500)
window.move(400, 250)

rb_male = QRadioButton("男", window)
rb_male.move(100, 100)
rb_female = QRadioButton("女", window)
rb_female.move(180, 100)

sex_group = QButtonGroup(window)
sex_group.addButton(rb_male, 1)  # 添加按钮，并设置id为1
sex_group.addButton(rb_female, 2)  # 添加按钮，并设置id为2


def test(val):
    print(f'id: {sex_group.id(val)}, text: {val.text()}')
    print(f'sex_group.checkedId(): {sex_group.checkedId()}')
    print(f'sex_group.checkedButton(): {sex_group.checkedButton().text()}')


# sex_group.buttonToggled.connect(test)  # 按钮状态发生改变时发送的信号
sex_group.buttonClicked.connect(test)  # 按钮被点击 信号为按钮对象
# sex_group.buttonClicked[int].connect(test)  # 信号为按钮的 id
# sex_group.buttonPressed.connect(test)  # 按钮按下时发射此信号
# sex_group.buttonReleased().connect(test)  # 按钮松开时发射此信号

window.show()

sys.exit(app.exec_())
