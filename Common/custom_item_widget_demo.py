from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QPushButton,
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


class TestCustomItemWidget:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.list_widget = QListWidget()
        self.list_widget.setMinimumSize(900, 800)

    def remove_item(self, item):
        index = self.list_widget.row(item)
        self.list_widget.takeItem(index)
        print(f"删除了第 {index} 项")

    def test(self):
        app = QApplication(sys.argv)

        # 创建一个QListWidget
        self.list_widget = QListWidget()
        self.list_widget.setMinimumSize(900, 800)

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

        self.list_widget.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    test = TestCustomItemWidget()
    test.test()
