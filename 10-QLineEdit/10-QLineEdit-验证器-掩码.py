import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton

"""
掩码是另一种更为严格的输入验证方式，用户输入的每一位都必须严格
符合掩码设置的要求

案例：
总共输入5位  左边2（必须是大写字母） - 右边3（必须是数字）
"""

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("QLineEdit-验证器-掩码")
window.resize(500, 500)
window.move(400, 250)

le_a = QLineEdit(window)
le_a.move(100, 100)
le_a.setInputMask(">AA-999")  # 设置掩码。> 表示从左边开始，A 表示字母，9 表示数字，- 表示分隔符。
# 左边部分必须是2个大写字母，右边部分必须是3个数字

btn = QPushButton("获取内容", window)
btn.move(100, 150)
le_a.mask
btn.clicked.connect(lambda: print(le_a.text()))

window.show()

sys.exit(app.exec_())
