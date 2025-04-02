import sys
from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QFileDialog


class InstallWizard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("软件安装向导")
        self.setGeometry(300, 300, 400, 200)

        # 创建堆栈窗口
        self.stacked_widget = QStackedWidget()

        # 添加3个页面
        self.page_welcome = self.create_page("欢迎安装本软件！", "点击下一步继续。")
        self.page_path = self.create_page("选择安装路径", "")
        self.page_confirm = self.create_page("确认安装", "点击完成开始安装。")

        # 在第二页添加路径选择按钮
        self.btn_choose_path = QPushButton("选择路径", self.page_path)
        self.btn_choose_path.clicked.connect(self.choose_path)
        self.page_path.layout().addWidget(self.btn_choose_path)

        # 将页面添加到堆栈
        self.stacked_widget.addWidget(self.page_welcome)
        self.stacked_widget.addWidget(self.page_path)
        self.stacked_widget.addWidget(self.page_confirm)

        # 创建导航按钮
        self.btn_prev = QPushButton("上一步")
        self.btn_next = QPushButton("下一步")
        self.btn_prev.clicked.connect(self.prev_page)
        self.btn_next.clicked.connect(self.next_page)

        # 布局
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.btn_prev)
        btn_layout.addWidget(self.btn_next)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.stacked_widget)
        main_layout.addLayout(btn_layout)
        self.setLayout(main_layout)

        # 初始化按钮状态
        self.update_buttons()

    def create_page(self, title, text):
        """快速创建一个带标题和文字的页面"""
        page = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel(f"<h2>{title}</h2>"))
        layout.addWidget(QLabel(text))
        page.setLayout(layout)
        return page

    def choose_path(self):
        """选择安装路径"""
        path = QFileDialog.getExistingDirectory(self, "选择安装路径")
        if path:
            self.page_path.layout().itemAt(1).widget().setText(f"已选择路径：{path}")

    def prev_page(self):
        """切换到上一页"""
        current_index = self.stacked_widget.currentIndex()
        if current_index > 0:
            self.stacked_widget.setCurrentIndex(current_index - 1)
            self.update_buttons()

    def next_page(self):
        """切换到下一页"""
        current_index = self.stacked_widget.currentIndex()
        if current_index < self.stacked_widget.count() - 1:
            self.stacked_widget.setCurrentIndex(current_index + 1)
            self.update_buttons()

    def update_buttons(self):
        """更新按钮状态（例如最后一页改为'完成'）"""
        current_index = self.stacked_widget.currentIndex()
        self.btn_prev.setEnabled(current_index > 0)
        if current_index == self.stacked_widget.count() - 1:
            self.btn_next.setText("完成")
            self.btn_next.clicked.disconnect()
            self.btn_next.clicked.connect(self.close)
        else:
            self.btn_next.setText("下一步")
            self.btn_next.clicked.disconnect()
            self.btn_next.clicked.connect(self.next_page)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InstallWizard()
    window.show()
    sys.exit(app.exec_())
