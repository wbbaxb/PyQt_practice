import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton

app = QApplication(sys.argv)

window = QWidget()
# window.resize(500, 500)
window.setFixedSize(500, 500)  # 固定尺寸（右上角最大化按钮被禁用，且窗口无法resize）
window.move(200, 200)

label = QLabel(window)
label.setText("ABC")
label.move(100, 100)
label.setStyleSheet("background-color: cyan;")


# 定义槽函数
def change_cao():
    new_content = label.text() + "ABC"
    label.setText(new_content)
    label.adjustSize()  # 根据内容自适应大小


btn = QPushButton(window)
btn.setText("增加内容")
btn.move(100, 300)
# connect 方法将信号（signal）连接到槽（slot）
btn.clicked.connect(change_cao)  # 将按钮的点击事件绑定到槽函数

window.show()

print(window.x())  # 获取窗口左上角到屏幕左上角的距离（200）
print(window.width())  # 获取窗口的宽度（500）
print(window.geometry())  # 返回QRect对象，获取窗口的尺寸和位置（PyQt5.QtCore.QRect(201, 231, 500, 500)）
# 为啥不是(200, 200, 500, 500)？因为move()设置的是窗口的外部位置，而geometry()获取的是窗口的内部位置

sys.exit(app.exec_())
