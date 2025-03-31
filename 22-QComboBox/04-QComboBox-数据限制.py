import sys

from PyQt5.QtWidgets import QApplication, QWidget, QComboBox


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QComboBox-数据限制")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        cbb = QComboBox(self)
        cbb.move(100, 100)
        cbb.resize(100, 20)
        cbb.setEditable(True)

        cbb.addItems(['Item:' + str(i) for i in range(50)])
        cbb.setFixedSize(100, 20)
        cbb.setStyleSheet('font-size: 20px;')
        cbb.setMaxCount(20)  # 限制最多存储20条，达到20后无法添加新的
        cbb.setMaxVisibleItems(10)  # 限制每页最多只显示10条


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
