import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QColorDialog, QLabel, QVBoxLayout
from PyQt5.QtGui import QColor, QPalette


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QColorDialog")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        cd = QColorDialog(QColor(20, 154, 151), self)  # 可以传入创建时的默认颜色
        cd.setWindowTitle("选择颜色")

        # 设置选项 显示alpha通道
        cd.setOptions(QColorDialog.ShowAlphaChannel)  # 典型应用场景：实时响应颜色变化

        cd.currentColorChanged.connect(self.color_changed)
        cd.colorSelected.connect(self.color_selected)

        btn = QPushButton("选择颜色", self)
        btn.setStyleSheet("font-size: 20px;height: 40px;")
        btn.move(100, 100)
        btn.clicked.connect(cd.show)

    def color_changed(self, color):
        btn = self.findChild(QPushButton)
        if btn:
            btn.setStyleSheet(
                f"font-size: 20px;height: 40px;color: rgba({color.red()},{color.green()},{color.blue()},{color.alpha()/255});")

    def color_selected(self, color):
        palette = QPalette()
        palette.setColor(QPalette.Background, color)
        self.setPalette(palette)  # 必须调用setPalette方法，否则颜色不会变化


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
