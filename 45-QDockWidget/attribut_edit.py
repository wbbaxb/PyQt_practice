from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QPushButton, QVBoxLayout, QGroupBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


class AttributeEditWindow(QMainWindow):
    def __init__(self, attributes: dict):
        super().__init__()
        self.attributes = attributes
        print(self.attributes)
        self.setup_ui()
        self.show_attributes()

    def setup_ui(self):
        """
        设置UI
        """
        self.setWindowTitle("属性编辑")
        self.setWindowIcon(QIcon("./Icons/python_96px.ico"))
        self.resize(800, 600)
        self.move(100, 100)
        self.setMinimumHeight(400)  # 设置最小高度，否则无法调整高度

        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QPushButton {
                background-color: #f0f0f0;
                border: 1px solid lightblue;
                border-radius: 3px;
                margin-top: 20px;
                padding: 20px 10px;  /* 增加垂直和水平内边距 */
            }
        """)

        # 创建中央部件
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # 在中央部件上设置布局
        self.main_layout = QVBoxLayout(self.central_widget)

        btn_add_attribute = QPushButton("添加属性")
        btn_add_attribute.clicked.connect(self.add_attribute)
        self.main_layout.addWidget(btn_add_attribute)

    def add_attribute(self):
        """
        添加属性
        """
        print("添加属性")

    def show_attributes(self):
        """
        显示属性
        """
        for key in self.attributes.keys():
            group_box = QGroupBox(key)  # 创建组框,key是组框的标题
            group_box.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 设置组框居中

            group_box.setStyleSheet("""
                QGroupBox {
                    font-size: 15px;
                    border: 1px solid lightblue;
                    border-radius: 3px;
                    margin-top: 20px;
                    padding: 20px 10px;  /* 增加垂直和水平内边距 */
                }
                QGroupBox::title {
                    left: 0;
                    padding: 0;
                    background-color: lightblue;
                    border-radius: 2px;
                }
            """)

            h_layout = QHBoxLayout()
            group_box.setLayout(h_layout)

            # 创建编辑按钮并存储key属性
            btn_edit = QPushButton("编辑")
            btn_edit.setProperty("attribute_key", key)  # 将key存储为按钮的属性
            btn_edit.clicked.connect(self.edit_attribute)
            h_layout.addWidget(btn_edit)

            # 创建删除按钮并存储key属性
            btn_delete = QPushButton("删除")
            btn_delete.setProperty("attribute_key", key)  # 将key存储为按钮的属性
            btn_delete.clicked.connect(self.delete_attribute)
            h_layout.addWidget(btn_delete)

            self.main_layout.addWidget(group_box)

    def edit_attribute(self):
        """
        编辑属性
        """
        # 获取发送信号的按钮
        sender = self.sender()
        # 获取按钮的属性
        key = sender.property("attribute_key")
        print(f"编辑属性: {key}")

    def delete_attribute(self):
        """
        删除属性
        """
        # 获取发送信号的按钮
        sender = self.sender()
        # 获取按钮的属性
        key = sender.property("attribute_key")
        print(f"删除属性: {key}")
