import sys

from PyQt5.QtWidgets import QApplication, QWidget, QKeySequenceEdit, QPushButton
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt

"""
QKeySequenceEdit 是 QWidget 的子类，用于显示和编辑按键序列。
它允许用户输入和编辑按键序列，并提供了一个方便的界面来显示和修改按键序列。

描述：

------------------- 构造函数 -----------------------
ks1 = QKeySequence(key_str)
ks2 = QKeySequence(QKeySequence.StandardKey key)
ks3 = QKeySequence(int k1, int k2, int k3, int k4)
静态方法 fromString(key_str)

-----------------------------------

转换成可读字符串 toString() -> str
键位个数 count()
"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QKeySequenceEdit")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        kse = QKeySequenceEdit(self)
        kse.move(100, 100)
        # ks = QKeySequence("Ctrl+C")
        # ks = QKeySequence(QKeySequence.Copy)
        ks = QKeySequence(Qt.CTRL + Qt.Key_C, Qt.CTRL + Qt.Key_A)  # 默认是Ctrl+C加Ctrl+A
        kse.setKeySequence(ks)
        # kse.clear()

        btn = QPushButton("测试按钮", self)
        btn.move(350, 100)
        btn.clicked.connect(
            lambda: print(kse.keySequence().toString(),
                          kse.keySequence().count())
        )

        kse.editingFinished.connect(
            lambda: print("结束编辑"))  # 编辑结束时发射的信号（往往是1s之后）
        
        kse.keySequenceChanged.connect(
            lambda key_val: print("键位序列发生改变", key_val.toString())
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
