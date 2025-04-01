import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QMovie


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLabel")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.show_basal_label()
        self.show_buddy()
        self.show_pixmap()
        self.show_movie()
        self.show_link()
        self.signal_connect()

    def show_basal_label(self):
        """
        最基础的QLabel
        """
        self.message_label = QLabel("message")
        self.message_label.setStyleSheet("color: green;font-size: 15px;")
        self.message_label.setFixedHeight(50)
        # self.message_label.adjustSize()  # 根据内容自适应大小

        # 对齐
        self.message_label.setAlignment(
            Qt.AlignRight | Qt.AlignVCenter)  # 手动设置靠右居中对齐
        # 缩进
        self.message_label.setIndent(2)  # 文本缩进，仅左右
        # 间距
        self.message_label.setMargin(10)  # 设置内容范围的边框与控件边框的间距，上下左右

        self.main_layout.addWidget(self.message_label)

    def show_buddy(self):
        """
        设置伙伴
        """
        label = QLabel("<h1>test</h1>", self)

        # 文本格式
        label.setTextFormat(Qt.PlainText)  # 纯文本
        # label.setTextFormat(Qt.RichText)  # 富文本
        # label.setTextFormat(Qt.AutoText)  # 自动识别是否富文本（默认值）

        edit_line = QLineEdit()

        label.setText("账号(&S)")
        label.setBuddy(edit_line)  # 设置伙伴,当按下Alt+S时，光标会自动跳转到edit_line

        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(edit_line)

        self.main_layout.addLayout(h_layout)

    def show_pixmap(self):
        """
        展示图片
        """
        label = QLabel()
        label.setPixmap(QPixmap("./Icons/OS_Ubuntu_128px.ico"))
        label.setScaledContents(True)  # 设置内容缩放

        self.main_layout.addWidget(label)

    def show_movie(self):
        """
        展示动图
        """
        label = QLabel()
        movie = QMovie("./Icons/打墙火柴人.gif")
        label.setMovie(movie)
        movie.setSpeed(200)  # 播放速度（百分比）
        movie.start()
        # movie.setPaused(True)  # 暂停播放

        # label.clear()  # 清空

        self.main_layout.addWidget(label)

    def show_link(self):
        """
        展示链接
        """
        label = QLabel()
        label.setText(
            "google的链接为 <a href=https://google.com>https://google.com</a>")
        label.setTextFormat(Qt.RichText)  # 富文本
        label.setOpenExternalLinks(True)  # 允许打开外部链接
        label.linkHovered.connect(lambda: label.setToolTip("google"))

        label.setWordWrap(True)  # 如果内容超出控件宽度，则以单词为分割，进行换行
        print(label.wordWrap())  # 获取是否换行,True表示换行

        self.main_layout.addWidget(label)

    def signal_connect(self):
        """
        信号连接
        """
        self.singnal_label = QLabel()
        self.singnal_label.setText(
            "baidu的链接为 <a href=https://baidu.com>https://baidu.com</a>")
        self.singnal_label.setTextFormat(Qt.RichText)  # 富文本
        self.singnal_label.setOpenExternalLinks(False)  # 不允许打开外部链接

        self.singnal_label.setWordWrap(True)  # 如果内容超出控件宽度，则以单词为分割，进行换行
        print(self.singnal_label.wordWrap())  # 获取是否换行,True表示换行

        # linkActivated仅在 OpenExternalLinks(False)时有效
        self.singnal_label.linkActivated.connect(
            lambda: self.message_label.setText("点击了百度链接"))

        self.singnal_label.linkHovered.connect(
            lambda: self.singnal_label.setToolTip("百度"))

        self.main_layout.addWidget(self.singnal_label)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
