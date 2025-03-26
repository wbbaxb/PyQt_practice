import sys

from PyQt5.QtWidgets import QApplication, QWidget, QCommandLinkButton
from PyQt5.QtGui import QIcon

"""QCommandLinkButton 继承自 QPushButton
是 QPushButton 的子类， 专门用于创建命令链接按钮，可以设置标题、描述、图标
和 QPushButton 相比， 多了描述和图标
"""

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("QCommandLinkButton的使用")
window.resize(500, 500)
window.move(400, 250)

btn = QCommandLinkButton("标题", "描述", window)
btn.setText("标题")
btn.setDescription("这是描述")
btn.setIcon(QIcon("./Icons/play_48px.ico"))

window.show()

sys.exit(app.exec_())
