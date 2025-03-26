import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

app = QApplication(sys.argv)

window = QWidget()
window.resize(500, 500)
window.move(400, 250)
icon = QIcon("./Icons/Photoshop.ico")
window.setWindowIcon(icon)  # 设置窗口图标

window.setWindowTitle("Title")  # 设置窗口标题

window.setWindowOpacity(0.78)  # 设置窗口不透明度
print(window.windowOpacity())

window.show()

sys.exit(app.exec_())
