from PyQt5.QtWidgets import QWidget,  QLabel, QPushButton, QVBoxLayout, QScrollArea, QFrame, QGridLayout, QHBoxLayout
import sys
from PyQt5.QtWidgets import QApplication, QSizePolicy
from PyQt5.QtCore import Qt
from Common.UniformGridLayout import UniformGridLayout


class UniformGridItem(QWidget):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.setFixedSize(120, 120)

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(5, 5, 5, 5)
        main_layout.setSpacing(5)
        self.setLayout(main_layout)
        self.setStyleSheet("background-color: lightgreen;")

        self.label = QLabel(text)
        self.label.setStyleSheet("font-size: 12px; ")
        self.label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.label)

        btn_layout = QHBoxLayout()
        main_layout.addLayout(btn_layout)

        btn_add = QPushButton("编辑")
        btn_add.setMinimumHeight(30)
        btn_add.setStyleSheet("background-color: yellowgreen;")
        btn_add.clicked.connect(self.btn_edit_clicked)
        btn_layout.addWidget(btn_add)

        btn_remove = QPushButton("删除")
        btn_remove.setMinimumHeight(30)
        btn_remove.setStyleSheet("background-color: red;")
        btn_remove.clicked.connect(self.btn_remove_clicked)
        btn_layout.addWidget(btn_remove)

    def btn_edit_clicked(self):
        print(f"按钮被点击，项内容: {self.label.text()}")

    def btn_remove_clicked(self):
        # 移除自身
        self.parent().layout().removeWidget(self)
        self.deleteLater()


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt UniformGridLayout")
        self.resize(800, 600)

        main_layout = QVBoxLayout(self)
        self.setLayout(main_layout)

        add_button = QPushButton("Add")
        add_button.clicked.connect(self.add_item)
        main_layout.addWidget(add_button)

        # 创建滚动区域
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scroll_area.setFrameShape(QFrame.NoFrame)

        self.container = QWidget() # 创建一个容器小部件，放置UniformGrid布局

        # 创建自定义网格布局
        self.uniform_grid = UniformGridLayout(self.container)
        self.container.setLayout(self.uniform_grid)

        # 设置容器居中对齐
        self.container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # 将容器添加到滚动区域
        self.scroll_area.setWidget(self.container)
        main_layout.addWidget(self.scroll_area)

        # 创建初始数据
        self.create_data()

        # 窗口大小变化时更新布局
        self.resizeEvent = self.on_resize

    def on_resize(self, event):
        self.uniform_grid.updateLayout()
        super().resizeEvent(event)

    def add_item(self):
        item = UniformGridItem(f"Item {self.uniform_grid.count() + 1}")
        self.uniform_grid.addWidget(item)

    def create_data(self):
        for _ in range(10):
            self.add_item()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
