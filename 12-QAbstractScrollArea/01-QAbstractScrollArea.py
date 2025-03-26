import sys

from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

# 滚动区域的低级抽象
# 继承自QFrame
app = QApplication(sys.argv)
window = QWidget()

window.setWindowTitle("QAbstractScrollArea")
window.resize(500, 500)

te = QTextEdit("TestTestTest", window)

# 滚动条显示类型有三种
# 0 按需显示 Qt.ScrollBarAsNeeded
# 1 始终不显示 Qt.ScrollBarAlwaysOff
# 2 始终显示 Qt.ScrollBarAlwaysOn

te.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded) # 纵向滚动条, 按需显示
te.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn) # 横向滚动条, 始终显示

print(te.verticalScrollBarPolicy()) # 纵向滚动条策略,0: 按需显示
print(te.horizontalScrollBarPolicy()) # 横向滚动条策略,2: 始终显示

btn = QPushButton(window)
btn.setIcon(QIcon("./Icons/python_96px.ico"))

te.setCornerWidget(btn)  # 设置横纵滚动条构成角落位置的控件

window.show()

sys.exit(app.exec_())
