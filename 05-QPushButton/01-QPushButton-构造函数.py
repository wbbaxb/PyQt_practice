import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("QPushButton的创建")
window.resize(500, 500)
window.move(400, 250)

btn = QPushButton(QIcon("./Icons/minus_48px.ico"), "Button", window)  # 设置图标、文本、父控件
btn.move(100, 100)
# 设置按扁平化
btn.setFlat(True)
print("btn是否为扁平化：", btn.isFlat())
window.show()

sys.exit(app.exec_())
