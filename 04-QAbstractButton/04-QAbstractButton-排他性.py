import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox

"""
QPushButton 默认无排他性
QRadioButton 默认有排他性
QCheckBox  默认无排他性
"""
app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("QAbstractButton排他性")
window.resize(500, 500)
window.move(400, 250)

for i in range(3):
    btn = QCheckBox(window)
    btn.setText(f"btn{i}")
    btn.move(50 * i, 200)

    # QCheckBox 默认无排他性，设置为有排他性后，可以被其他按钮影响
    btn.setAutoExclusive(True)  # 设置排他性
    print(btn.autoExclusive())  # 获取排他性,True

btn = QCheckBox(window)
btn.setText("btn3不受影响")
btn.move(200, 200)

window.show()

sys.exit(app.exec_())
