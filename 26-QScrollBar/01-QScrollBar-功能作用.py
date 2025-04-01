import sys

from PyQt5.QtWidgets import QWidget, QApplication, QScrollBar
from PyQt5.QtCore import Qt

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QScrollBar")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        slb = QScrollBar(Qt.Horizontal, self) 
        slb.resize(200, 20)
        slb.move(100, 400)

        slb.valueChanged.connect(lambda val: print(f'valueChanged: {val}'))
        slb.setPageStep(20)  # PageStep 可以控制滑块长度

        slb.grabKeyboard() # 设置为捕捉键盘，即响应PgUp/PgDn,默认是不捕捉的

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
