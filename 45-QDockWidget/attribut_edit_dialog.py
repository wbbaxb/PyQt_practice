from PyQt5.QtWidgets import QDialog, QHBoxLayout, QPushButton, QVBoxLayout, QGroupBox, QGridLayout, QLabel, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from Common.UniformGridLayout import UniformGridLayout


class AttributeEditDialog(QDialog):
    def __init__(self, attributes: dict, parent=None):
        super().__init__(parent=parent)
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
        self.move(500, 500)
        self.setMinimumHeight(400)  # 设置最小高度，否则无法调整高度
        self.setWindowFlags(Qt.Window | Qt.WindowTitleHint |
                            Qt.WindowMaximizeButtonHint | Qt.WindowCloseButtonHint)

        # 整体应用样式
        self.setStyleSheet("""
            QLabel {
                font-size: 14px;
                font-weight: bold;
                color: black;
            }
            QPushButton {
                border-radius: 4px;
                height: 30px;
                font-size: 13px;
            }
            QPushButton:hover {
                background-color: orange;
            }
            QPushButton:pressed {
                background-color: red;
            }
            QPushButton#editBtn {
                background-color: lightblue;
                border-radius: 4px;
                height: 30px;
                font-size: 13px;
            }  
            QPushButton#deleteBtn {
                background-color: #f44336;
            }
            QPushButton#addBtn {
                background-color: #2196F3;
                padding: 10px 20px;
                font-size: 14px;
                font-weight: bold;
            }
        """)

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.top_layout = QVBoxLayout()
        self.main_layout.addLayout(self.top_layout)

        self.grid_layout = UniformGridLayout()
        self.grid_layout.setSpacing(15)  # 增加间距
        self.main_layout.addLayout(self.grid_layout)

        btn_add_attribute = QPushButton("添加属性")
        btn_add_attribute.setObjectName("addBtn")
        btn_add_attribute.setCursor(Qt.PointingHandCursor)
        btn_add_attribute.setMinimumHeight(40)
        btn_add_attribute.clicked.connect(self.add_attribute)
        self.top_layout.addWidget(btn_add_attribute)

    def show_attributes(self):
        """
        显示所有属性
        """
        for key in self.attributes.keys():
            container = QWidget()
            # 设置对象名称以应用特定样式，只对容器设置边框，不影响子控件
            container.setObjectName("attributeContainer")

            container.setStyleSheet("""
                QWidget#attributeContainer {
                    border: 1px solid orange;
                    border-radius: 6px;
                    background-color: white;
                }
            """)
            main_layout = QVBoxLayout()
            main_layout.setContentsMargins(10, 10, 10, 10)  # 增加内边距
            container.setLayout(main_layout)
            self.grid_layout.addWidget(container)

            label = QLabel(key)
            label.setAlignment(Qt.AlignCenter)
            main_layout.addWidget(label)

            h_layout = QHBoxLayout()
            main_layout.addLayout(h_layout)

            btn_edit_attribute = QPushButton("编辑")
            btn_edit_attribute.setObjectName("editBtn")
            btn_edit_attribute.setCursor(Qt.PointingHandCursor)
            btn_edit_attribute.clicked.connect(self.edit_attribute)
            btn_edit_attribute.setProperty("attribute_key", container)
            h_layout.addWidget(btn_edit_attribute)

            btn_delete_attribute = QPushButton("删除")
            btn_delete_attribute.setObjectName("deleteBtn")  # 设置对象名称以应用特定样式
            btn_delete_attribute.setCursor(Qt.PointingHandCursor)
            btn_delete_attribute.clicked.connect(self.delete_attribute)
            btn_delete_attribute.setProperty("attribute_key", container)
            h_layout.addWidget(btn_delete_attribute)

    def add_attribute(self):
        """
        添加属性
        """
        print("添加属性")

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
        # 获取按钮的属性,QWidget对象
        container = sender.property("attribute_key")
        self.grid_layout.removeWidget(container)
