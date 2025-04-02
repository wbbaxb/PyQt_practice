import sys

from PyQt5.QtWidgets import QWidget, QErrorMessage, QApplication, QVBoxLayout, QPushButton


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QErrorMessage")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        self.setStyleSheet(
            "background-color: white;QPushButton{margin: 20px;height: 30px;}")

        btn_show_error_message = QPushButton("显示错误提示框")
        main_layout.addWidget(btn_show_error_message)
        btn_show_error_message.clicked.connect(self.show_error_message)

        btn_show_typed_message = QPushButton("显示带类型的错误提示框")
        main_layout.addWidget(btn_show_typed_message)
        btn_show_typed_message.clicked.connect(self.show_typed_message)

    def show_error_message(self):
        em = QErrorMessage(self)
        em.setWindowTitle("错误提示")

        # 设置类型为"general_error"
        em.showMessage("在此处展示一些错误提示信息", "general_error")
        em.showMessage("在此处展示一些错误提示信息")  # 由于上面设置了类型，所以这里还是会弹出
        # 如果取消勾选'show this message again'，则不会再显示相同的文本
        em.showMessage("在此处展示一些错误提示信息")
        em.showMessage("另外的一些错误提示信息")  # 提示信息不同的其他提示框依然会显示

        # em.exec()  # 应用程序级的模态

    def show_typed_message(self):
        em = QErrorMessage(self)
        em.setWindowTitle("类型化错误提示")

        # 使用不同类型的错误消息
        # 当用户选择"不再显示此消息"时，仅会忽略对应类型的消息
        em.showMessage("这是一个网络错误", "network_error")
        em.showMessage("这是一个数据库错误", "database_error")
        # 如果用户选择了不再显示"network_error"类型的消息，则此方法将不执行任何操作
        em.showMessage("这是另一个网络错误", "network_error")
        em.showMessage("这是一个文件系统错误", "filesystem_error")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
