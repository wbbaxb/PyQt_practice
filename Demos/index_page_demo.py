import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QScrollArea, QFrame,  QMessageBox
from PyQt5.QtCore import Qt,  pyqtSlot
from Common.menu_wrap_layout import WrapLayout, MenuTile


class MenuData:
    def __init__(self, name, visible=True):
        self.name = name
        self.visible = visible

    def __str__(self):
        return self.name


class IndexPageDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WrapPanel")
        self.resize(800, 600)

        # 创建菜单数据
        self.menu_items = []

        # 初始化UI
        self.setup_ui()

        # 初始加载菜单
        self.load_menu_list()

    def setup_ui(self):
        # 主布局
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)
        self.setLayout(main_layout)

        # 顶部控制区域
        top_bar = QWidget()
        top_layout = QHBoxLayout(top_bar)
        top_layout.setContentsMargins(100, 20, 100, 20)

        # 添加按钮
        self.add_button = QPushButton("添加")
        self.add_button.clicked.connect(self.add_menu_item)
        top_layout.addWidget(self.add_button)

        # 按钮间距
        spacer = QWidget()
        spacer.setFixedWidth(50)
        top_layout.addWidget(spacer)

        # 删除按钮
        self.remove_button = QPushButton("删除")
        self.remove_button.clicked.connect(self.remove_menu_item)
        top_layout.addWidget(self.remove_button)

        # 添加顶部控制栏到主布局
        main_layout.addWidget(top_bar)

        # 创建一个滚动区域
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        main_layout.addWidget(self.scroll_area)

        # 创建滚动区域内容
        self.content_widget = QWidget()
        self.content_widget.setStyleSheet("background-color: white;")

        # 创建自定义的WrapLayout
        self.menu_layout = WrapLayout(
            self.content_widget, max_items_per_row=4, spacing=20)
        self.content_widget.setLayout(self.menu_layout)

        # 将内容添加到滚动区域
        self.scroll_area.setWidget(self.content_widget)

    def load_menu_list(self):
        # 清除现有菜单
        while self.menu_layout.count():
            item = self.menu_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        # 添加所有菜单
        for i, menu_data in enumerate(self.menu_items):
            if menu_data.visible:
                menu_tile = MenuTile(
                    f"新菜单{i+21}" if i >= 5 else menu_data.name, menu_data)
                menu_tile.clicked.connect(self.on_menu_clicked)
                self.menu_layout.addWidget(menu_tile)

    def calculate_items_per_row(self, total_items, max_items_per_row):
        """计算每行最优的项目数量"""
        # 计算需要多少行来均匀分布所有元素
        rows_needed = (total_items + max_items_per_row -
                       1) // max_items_per_row

        # 根据行数计算每行应该有多少个元素
        if rows_needed <= 0:
            return 1
        items_per_row = (total_items + rows_needed - 1) // rows_needed

        return min(items_per_row, max_items_per_row)

    @pyqtSlot(object)
    def on_menu_clicked(self, data):
        """菜单点击处理"""
        if isinstance(data, MenuData):
            QMessageBox.information(self, "菜单点击", f"你点击了：{data.name}")
        else:
            QMessageBox.information(self, "菜单点击", f"你点击了：{str(data)}")

    def add_menu_item(self):
        """添加新菜单项"""
        count = len(self.menu_items) + 1
        new_menu = MenuData(f"新菜单{count}")
        self.menu_items.append(new_menu)
        self.load_menu_list()

    def remove_menu_item(self):
        """删除最后一个菜单项"""
        if self.menu_items:
            self.menu_items.pop()
            self.load_menu_list()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = IndexPageDemo()
    window.show()
    sys.exit(app.exec_())
