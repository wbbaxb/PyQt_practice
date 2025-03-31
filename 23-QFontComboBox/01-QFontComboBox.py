import sys

from PyQt5.QtWidgets import QApplication, QWidget, QFontComboBox, QLabel


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFontComboBox")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):

        label = QLabel(self)
        label.move(100, 100)
        label.setText("bill")
        label.setStyleSheet("font-size: 40px;")

        fcb = QFontComboBox(self)
        fcb.move(100, 200)
        fcb.setFontFilters(QFontComboBox.AllFonts)  # 设置显示所有字体
        """
        QFontComboBox.AllFonts  显示所有字体
        QFontComboBox.ScalableFonts  显示可缩放字体
        QFontComboBox.MonospacedFonts  显示等宽字体
        QFontComboBox.ProportionalFonts  显示比例字体
        """

        fcb.setEditable(False)  # 禁止用户编辑
        fcb.setMinimumWidth(200)  # 设置最小宽度
        fcb.setMinimumHeight(40)  # 设置最小高度

        def set_font(font):
            label.setFont(font)
            label.adjustSize()

        fcb.currentFontChanged.connect(lambda font: set_font(font))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
