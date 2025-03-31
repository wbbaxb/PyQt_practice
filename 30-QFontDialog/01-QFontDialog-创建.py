import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFontDialog, QLabel, QVBoxLayout
from PyQt5.QtGui import QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFontDialog")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        font = QFont()
        font.setFamily("宋体")  # 设置字体
        self.fd = QFontDialog(font, self)  # 可以在创建时传入一个QFont对象作为默认字体
        self.fd.setWindowTitle("选择一个字体") # 设置窗口标题

        # 当点击确定按钮时，会触发fontSelected信号
        self.fd.fontSelected.connect(self.font_selected)

        # 无需确定按钮，当当前字体发生变化时，会触发currentFontChanged信号

        # ------------选项控制-----------------
        """
        QFontDialog.FontDialogOption:
        QFontDialog.NoButtons  不显示“确定”和”取消“按钮。（对“实时对话框”有用）
        QFontDialog.DontUseNativeDialog  在Mac上使用Qt的标准字体对话框而不是Apple的原生字体对话框
        QFontDialog.ScalableFonts  显示可缩放字体
        QFontDialog.NonScalableFonts  显示不可缩放的字体
        QFontDialog.MonospacedFonts  显示等宽字体
        QFontDialog.ProportionalFonts  显示比例字体
        """

        # 设置选项,1.不显示确定按钮 2.只显示等宽字体
        self.fd.setOptions(QFontDialog.NoButtons | QFontDialog.MonospacedFonts)
        self.fd.currentFontChanged.connect(self.font_selected)

        self.label = QLabel("测试文本")

        btn = QPushButton("选择字体")
        btn.setStyleSheet("font-size: 20px;height: 40px;")
        btn.clicked.connect(self.fd.open)  # 点击按钮后打开字体对话框

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        main_layout.addWidget(self.label)
        main_layout.addWidget(btn)

    def font_selected(self, font):
        self.label.setFont(font)
        self.label.adjustSize()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
