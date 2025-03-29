import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QObject类型判定案例")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        self.name()

    def name(self):
        label1 = QLabel(self)
        label1.setText("这是label1")
        label1.move(100, 100)

        label2 = QLabel(self)
        label2.setText("这是label2")
        label2.move(100, 300)

        btn = QPushButton(self)
        btn.setText("Test")
        # 不可以一次连接多个槽函数
        # btn.clicked.connect(self.child_all_label,self.child_all_label2)
        btn.clicked.connect(self.child_all_label)
        btn.clicked.connect(self.child_all_label2)

        btn.move(100, 450)

    def child_all_label(self):
        """
        使用findChildren方法查找所有QLabel控件
        """
        for label in self.findChildren(QLabel):
            name = label.text()
            label.setText(f"new-{name}")

    def child_all_label2(self):
        """
        使用children方法查找所有QLabel控件
        """
        for item in self.children():
            if isinstance(item, QLabel):
                item.setStyleSheet("background-color: red;font-size: 30px;")
                item.adjustSize()  # 自适应内容,需要先设置文本和样式后,再调用


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
