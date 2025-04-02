import sys
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton
from PyQt5.QtGui import QIcon

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("QRadioButton的创建")
window.resize(500, 500)
window.move(400, 250)

rb_male = QRadioButton("男-&Male", window)  # 因为在字母M之前使用了&符号，自动添加一个Alt+M的快捷键
rb_male.setIcon(QIcon("./Icons/man_96px.ico"))
rb_male.setShortcut("Alt+M")  # 设置快捷键
rb_male.move(100, 100)
rb_male.setChecked(True)  # 手动设置已为被选中

rb_female = QRadioButton("女-&Female", window)
rb_female.setIcon(QIcon("./Icons/woman_96px.ico"))
rb_female.move(100, 150)

# 选中状态发生改变时执行print槽函数
rb_female.toggled.connect(
    lambda isChecked: print("rb_female选中状态变成了：", isChecked)
)

# QRadioButton 默认是排他性的， 如果想要取消排他性， 需要设置 autoExclusive 属性为 False
rb_female.setAutoExclusive(False)

window.show()

sys.exit(app.exec_())
