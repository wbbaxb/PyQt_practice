import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFontDialog, QLabel, QVBoxLayout
from PyQt5.QtGui import QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFontDialog-静态方法")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        btn = QPushButton("测试按钮", self)
        btn.move(100, 100)
        label = QLabel(self)
        label.move(100, 200)
        label.setText("bill")

        def font_set():
            font = QFont()
            font.setFamily("宋体")
            font.setPointSize(22)
            result = QFontDialog.getFont(
                font, self, "选择一个字体", QFontDialog.ScalableFonts
            )
            if result[1]:
                label.setFont(result[0])
                label.adjustSize()

        btn.clicked.connect(font_set)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
