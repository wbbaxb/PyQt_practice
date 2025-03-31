import sys

from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTextEdit-set_text")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()
        self.set_text()

    def setup_ui(self):
        self.te = QTextEdit("一开始就有的文字", self)  # 虽然已经写入了文字，但光标会在行首

        self.test_btn = QPushButton("清空", self)
        self.test_btn.move(400, 150)
        self.test_btn.clicked.connect(self.clear_text)

    def clear_text(self):
        self.te.clear()
        self.te.setPlaceholderText("<h3>h3标题</h3>")

    def set_text(self):
        # 设置普通文本内容
        # self.te.setPlainText("<h3>h3标题</h3>")  # 会先清空，再以纯文本写入
        # self.te.insertPlainText("<h4>h4标题</h4>")  # 不会先清空
        # print(self.te.toPlainText())  # 以纯文本返回内容

        # 富文本
        # self.te.setHtml("<h3>h3标题</h3>")
        # self.te.insertHtml("<h4>这是一个h4标题</h4>")
        # print(self.te.toHtml())  # 转换为HTML4 之后输出

        # 设置文本（根据内容自动识别纯文本/富文本）
        self.te.setText("普通文本")
        self.te.setText("<h3>富文本</h3>")  # 先清空，再以富文本写入

        # 追加（自动识别纯文本/富文本）
        self.te.append("<h3>富文本</h3>")  # 追加，自动识别纯文本/富文本


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
