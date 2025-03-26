import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("QAbstractButton 信号")
window.resize(500, 500)
window.move(400, 250)

btn = QPushButton(window)
btn.setText("按钮1")
btn.move(200, 200)
btn.setCheckable(True)  # 设置按钮为可被选中,否则toggled信号不会发送

# 按钮选中状态变化时发送信号； value值为按钮是否被选中
btn.toggled.connect(
    lambda value: print("按钮选中状态发生了变化", value)
)

window.show()

sys.exit(app.exec_())
