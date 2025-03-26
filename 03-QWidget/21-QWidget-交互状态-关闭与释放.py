import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("交互状态-关闭")
window.resize(500, 500)
window.move(400, 250)

btn = QPushButton(window)
btn.setText("按钮")
btn.setAttribute(Qt.WA_DeleteOnClose)  # 设置按钮在关闭时自动释放,如果不设置，则不会触发destroyed信号
btn.destroyed.connect(lambda: print("按钮被释放了"))

btn.clicked.connect(btn.close)  # 点击按钮后释放按钮对象

window.show()

sys.exit(app.exec_())
