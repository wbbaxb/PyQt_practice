import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
window = QWidget()

# 窗口标题中的[*]是一个特殊的占位符
# 当调用setWindowModified(True)时，星号才会显示出来
# 这通常用于指示文档已被修改但尚未保存
window.setWindowTitle("[*]交互状态")  # *星号只有设置setWindowModified(True)才会被显示
window.resize(500, 500)
window.move(400, 250)

# 设置窗口修改状态为True，此时标题中的星号会显示
window.setWindowModified(True)
print("窗口是否被编辑：", window.isWindowModified())  # True

w2 = QWidget()  # 为验证活动窗口相关API而创建的另一个窗口
w2.show()

window.show()
w2.raise_()  # 即使被提到前面，也不一定是活动窗口

print("w2是否为活动窗口：", w2.isActiveWindow())  # False
print("window是否为活动窗口：", window.isActiveWindow())  # True
print("窗口是否被编辑：", window.isWindowModified())  # True

sys.exit(app.exec_())
