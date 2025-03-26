import sys
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QButtonGroup, QPushButton

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("QButtonGroup的使用")
window.resize(500, 500)
window.move(400, 250)

rb_male = QRadioButton("男", window)
rb_male.move(100, 100)
rb_female = QRadioButton("女", window)
rb_female.move(180, 100)

rb_yes = QRadioButton("yes", window)
rb_yes.move(100, 220)
rb_no = QRadioButton("no", window)
rb_no.move(180, 220)

# 处理多组互斥——糟糕的解决方案：创建多个父控件，同组的放在同一个父控件中
# 好的解决方案：QButtonGroup


def add_btn_group():
    """
    添加QButtonGroup
    男、女属于同一按钮组，互斥，只能选中其中之一
    yes、no属于另一按钮组，不受男女的影响
    """

    sex_group = QButtonGroup(window)
    sex_group.addButton(rb_male)  # 把rb_male按钮添加到sex_group按钮组
    sex_group.addButton(rb_female)  # 把rb_female按钮添加到sex_group按钮组

    answer_group = QButtonGroup(window)
    answer_group.addButton(rb_yes)
    answer_group.addButton(rb_no)

    btn = window.findChild(QPushButton, "add_button")  # 通过objectName查找
    btn.close()


btn = QPushButton("添加QButtonGroup", window)
btn.setObjectName("add_button")  # 设置objectName，方便通过window.findChild查找
btn.move(100, 300)
btn.clicked.connect(add_btn_group)


window.show()
sys.exit(app.exec_())
