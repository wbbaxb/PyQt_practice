import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("QLineEdit-对齐方式")
window.resize(500, 500)
window.move(400, 250)

le = QLineEdit(window)
le.resize(200, 200)
# le.setAlignment(Qt.AlignHCenter)  # 水平居中
# le.setAlignment(Qt.AlignVCenter)  # 垂直居中
# le.setAlignment(Qt.AlignCenter)  # 居中
# le.setAlignment(Qt.AlignTop)  # 上对齐
le.setAlignment(Qt.AlignRight | Qt.AlignBottom)  # 右下角
le.setTextMargins(0, 0, 20, 20)  # 离右下角稍有距离

window.show()

sys.exit(app.exec_())
