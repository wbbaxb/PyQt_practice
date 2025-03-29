import sys
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QPushButton

app = QApplication(sys.argv)

window = QWidget()
window.resize(500, 500)
window.move(400, 300)

window.setWindowTitle('test')

main_layout = QHBoxLayout()
window.setLayout(main_layout)

btn = QPushButton('change', window)
btn.resize(500, 80)
btn.move(0, 100)

with open("02-QObject/style.qss", "r", encoding="utf-8") as f:
    style = f.read()
    btn.setStyleSheet(style)  # 设置样式表(应用于当前按钮)

# 点击按钮，窗口标题会在前面添加bill，且可以无限添加
btn.clicked.connect(lambda: window.setWindowTitle(
    'bill' + window.windowTitle()))


def window_title_changed_old(new_title):
    """
    这个方法不正确，因为每次改变窗口标题，都会触发这个槽，导致死循环
    """
    window.setWindowTitle(new_title)


def window_title_changed(new_title):
    # 应该先阻断信号，再改变窗口标题，再恢复信号
    window.blockSignals(True)  # 阻断信号,避免死循环
    window.setWindowTitle(new_title)
    window.blockSignals(False)  # 恢复信号,使下一次还能进行修改


# 当窗口标题变化时，window.windowTitleChanged 信号会被发出，连接到的槽 window_title_changed 会被调用。
window.windowTitleChanged.connect(window_title_changed)

window.show()
sys.exit(app.exec())
