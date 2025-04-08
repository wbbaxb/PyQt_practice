from PyQt5.QtWidgets import QDialog, QHBoxLayout, QPushButton, QVBoxLayout, QLabel, QWidget, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from Common.UniformGridLayout import UniformGridLayout
from add_new_attribute import AddNewAttributeDialog
from Common.custom_message_box import CustomMessageBox


class AttributeEditDialog(QDialog):
    def __init__(self, attributes: dict, parent=None):
        super().__init__(parent=parent)
        self.attributes = attributes
        self.font_size = 16
        self.setup_ui()
        self.show_attributes()

    def setup_ui(self):
        self.setWindowTitle("属性编辑")
        self.setWindowIcon(QIcon("./Icons/python_96px.ico"))
        self.resize(800, 600)
        self.move(500, 500)
        self.setMinimumHeight(400)  # 设置最小高度，否则无法调整高度
        self.setWindowFlags(Qt.Window | Qt.WindowTitleHint |
                            Qt.WindowMaximizeButtonHint | Qt.WindowCloseButtonHint)

        # 整体应用样式
        self.setStyleSheet(f"""
            /* 容器样式 */
            QWidget#attributeContainer {{
                border: 2px solid orange;
                border-radius: 10px;
                background-color: white;
            }}
            
            /* 标签样式 */
            QLabel {{
                font-size: {self.font_size}px;
                font-weight: bold;
                color: black;
            }}
            
            /* 按钮通用样式 */
            QPushButton {{
                border-radius: 5px;
                padding: 10px 20px;
                font-size: {self.font_size}px;
                font-weight: bold;
                background-color: #2196F3;
            }}
            
            /* 删除按钮特殊样式 */
            QPushButton#deleteBtn {{
                background-color: #f44336;
            }}
            
            /* 按钮状态样式 */
            QPushButton:hover {{
                background-color: rgb(73, 170, 159);
            }}
            QPushButton:pressed {{
                background-color: rgb(234, 208, 112);
            }}
            QPushButton#deleteBtn:hover {{
                background-color: rgb(198, 122, 211);
            }}
            QPushButton#deleteBtn:pressed {{
                background-color: rgb(206, 200, 229);
            }}
        """)

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.top_layout = QVBoxLayout()
        self.main_layout.addLayout(self.top_layout)

        self.grid_layout = UniformGridLayout()
        self.grid_layout.setSpacing(20)
        self.main_layout.addLayout(self.grid_layout)

        btn_show_add_attribute_dialog = QPushButton("添加属性")
        btn_show_add_attribute_dialog.setFixedHeight(50)
        btn_show_add_attribute_dialog.setCursor(Qt.PointingHandCursor)
        btn_show_add_attribute_dialog.setMinimumHeight(40)
        btn_show_add_attribute_dialog.clicked.connect(
            self.show_add_attribute_dialog)
        self.top_layout.addWidget(btn_show_add_attribute_dialog)

    def show_attributes(self):
        """
        显示所有属性
        """
        for key in self.attributes.keys():
            self.add_attribute(key)

    def add_attribute(self, attribute_name: str):
        container = QWidget()
        # 设置对象名称以应用特定样式，只对容器设置边框，不影响子控件
        container.setObjectName("attributeContainer")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)  # 增加内边距
        container.setLayout(main_layout)
        self.grid_layout.addWidget(container)

        label = QLabel(attribute_name)
        label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(label)

        h_layout = QHBoxLayout()
        main_layout.addLayout(h_layout)

        btn_edit_attribute = QPushButton("编辑")
        btn_edit_attribute.setObjectName("editBtn")
        btn_edit_attribute.setCursor(Qt.PointingHandCursor)
        btn_edit_attribute.clicked.connect(self.show_edit_attribute_dialog)
        btn_edit_attribute.setProperty("attribute_key", container)
        h_layout.addWidget(btn_edit_attribute)

        btn_delete_attribute = QPushButton("删除")
        btn_delete_attribute.setObjectName("deleteBtn")  # 设置对象名称以应用特定样式
        btn_delete_attribute.setCursor(Qt.PointingHandCursor)
        btn_delete_attribute.clicked.connect(self.delete_attribute)
        btn_delete_attribute.setProperty("attribute_key", container)
        h_layout.addWidget(btn_delete_attribute)

        # 使用HTML富文本设置tooltip
        container.setToolTip(f'''
        <div style="background-color: #f5f5f5; padding: 10px; border: 2px solid #2196F3; border-radius: 5px;">
            <h3 style="color: #2196F3; margin: 0 0 10px 0;">属性信息</h3>
            <p style="margin: 5px 0;"><b>名称:</b> {attribute_name}</p>
            <hr style="border: 1px solid #cccccc; margin: 10px 0;">
            <p style="color: #666; margin: 5px 0;">支持HTML富文本格式</p>
            <img src="./Icons/python_96px.ico" width="32" height="32" />
        </div>
        ''')

    def delete_attribute(self):
        message_box = CustomMessageBox(self)
        result = message_box.exec("提示", "确定删除该属性吗？")

        if result == QMessageBox.Yes:
            # 获取发送信号的按钮
            sender = self.sender()
            # 获取按钮的属性,QWidget对象
            container = sender.property("attribute_key")
            self.grid_layout.removeWidget(container)

    def show_add_attribute_dialog(self):
        dialog = AddNewAttributeDialog(
            parent=self, exits_attributes=self.attributes.keys())
        # dialog.setWindowModality(Qt.ApplicationModal)
        # dialog.show() # 即使设置了setWindowModality(Qt.ApplicationModal)，
        # 使用show()或者open()还是不会阻塞，所以如果需要获取返回值，需要使用exec_()

        # 使用exec_()会阻塞，直到对话框关闭
        result = dialog.exec_()
        if result == QDialog.Accepted:
            attribute_data = dialog.attribute_data
            self.add_attribute(attribute_data.get('name'))

    def show_edit_attribute_dialog(self):
        # 获取发送信号的按钮
        sender = self.sender()
        # 获取按钮的属性
        key = sender.property("attribute_key")
        print(f"编辑属性: {key}")
