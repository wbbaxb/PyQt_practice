from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QPushButton, QVBoxLayout,
                             QListWidget, QListWidgetItem, QApplication)
import sys


class CustomItemWidget(QWidget):
    """
    自定义列表项小部件
    """

    def __init__(self, text, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout()
        self.label = QLabel(text)
        self.label.setStyleSheet("""
            QLabel {{
                background-color: black;
                color: white;
            }}
        """)
        self.button = QPushButton("删除")
        self.button.setStyleSheet("""
            QPushButton {{
                background-color: black;
                color: white;
            }}
        """)
        layout.addWidget(self.label)

        layout.addWidget(self.button)
        self.setLayout(layout)
        self.setStyleSheet("""
            QWidget {{
                background-color: lightblue;
            }}
        """)


class TestCustomItemWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(900, 800)
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        self.list_widget = QListWidget()
        main_layout.addWidget(self.list_widget)

        btn_get_item = QPushButton("获取列表项")
        btn_get_item.setStyleSheet("""
            QPushButton {{
                background-color: black;
                color: white;
            }}
        """)

        main_layout.addWidget(btn_get_item)
        btn_get_item.clicked.connect(self.get_all_items)

        # 初始化列表项
        self.init_list_items()

    def get_all_items(self):
        # 获取所有列表项
        item_count = self.list_widget.count()
        print(f"列表中共有 {item_count} 个项目")
        
        # 遍历所有项目
        for i in range(item_count):
            item = self.list_widget.item(i)
            widget = self.list_widget.itemWidget(item)
            if widget:
                text = widget.label.text()
                print(f"项目 {i}: {text}")

    def remove_item(self, item):
        index = self.list_widget.row(item)
        self.list_widget.takeItem(index)
        print(f"删除了第 {index} 项")

    def init_list_items(self):
        """初始化列表项"""
        for i in range(10):
            # 创建并添加自定义 Item
            item = QListWidgetItem()
            self.list_widget.addItem(item)

            # 创建自定义 Widget 并关联到 Item
            custom_widget = CustomItemWidget("Custom Item " + str(i))
            self.list_widget.setItemWidget(item, custom_widget)

            # 设置Item的大小
            custom_widget_size = custom_widget.sizeHint()
            item.setSizeHint(custom_widget_size)
            custom_widget.setObjectName("custom_widget" + str(i))

            custom_widget.button.clicked.connect(
                lambda checked=False, widget_item=item: self.remove_item(widget_item))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    test = TestCustomItemWidget()
    test.show()
    sys.exit(app.exec_())
