import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class Window(QWidget):
    """自定义窗口类,继承自QWidget"""

    def __init__(self):
        super().__init__()  # 进行父类的初始化
        self.setWindowTitle("面向对象版本的PyQt代码")
        self.resize(500, 500)
        self.move(400, 250)

    def setup_ui(self):
        label = QLabel(self)
        label.setText("Hello world")
        label.move(200, 240)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()  
    window.setup_ui() 
    window.show() 

    sys.exit(app.exec_())
