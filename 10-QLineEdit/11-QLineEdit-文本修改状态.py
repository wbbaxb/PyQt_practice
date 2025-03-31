import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton

"""
QLineEdit 的文本修改状态
当文本内容被编辑后（即使编辑后的内容与编辑前的内容相同，比如输入'123'，再删除'123'）isModified() 方法返回 True

setModified(bool) 方法用于设置 QLineEdit 的文本修改状态。

"""

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("QLineEdit-文本修改状态")
window.resize(500, 500)
window.move(400, 250)

le = QLineEdit(window)


def cao():
    print(le.isModified())
    le.setModified(False)  # 重置文本修改状态


btn = QPushButton("显示", window)
btn.move(200, 0)
btn.clicked.connect(cao)

window.show()

sys.exit(app.exec_())
