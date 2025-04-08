from PyQt5.QtWidgets import QDialog, QHBoxLayout, QPushButton, QVBoxLayout, QLabel, QWidget, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from Common.UniformGridLayout import UniformGridLayout
from edit_attribute import EditAttributeDialog
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
        self.setMinimumHeight(400)  # 设置最小高度，否则无法调整高度
        self.setWindowFlags(Qt.Window | Qt.WindowTitleHint |
                            Qt.WindowMaximizeButtonHint | Qt.WindowCloseButtonHint)

        # 整体应用样式
        self.setStyleSheet(f"""
            QWidget#attributeContainer {{
                border: 2px solid orange;
                border-radius: 10px;
                background-color: white;
            }}
            
            QLabel {{
                font-size: {self.font_size}px;
                font-weight: normal;
                color: black;
            }}
            
            QPushButton {{
                border-radius: 5px;
                padding: 10px 20px;
                font-size: {self.font_size}px;
                font-weight: normal;
                background-color: #2196F3;
            }}
            QPushButton:hover {{
                background-color: rgb(73, 170, 159);
            }}
            QPushButton:pressed {{
                background-color: rgb(234, 208, 112);
            }}

            QPushButton#importBtn {{
                background-color: yellowgreen;
            }}
            QPushButton#importBtn:hover {{
                background-color: rgb(198, 122, 211); /* 紫色 */
            }}
            QPushButton#importBtn:pressed {{
                background-color: rgb(206, 200, 229);  /* 淡紫色 */
            }}
                        
            QPushButton#deleteBtn {{
                background-color: #f44336; /* 红色 */
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
        self.top_layout = QHBoxLayout()
        self.main_layout.addLayout(self.top_layout)

        self.grid_layout = UniformGridLayout()
        self.grid_layout.setSpacing(30)
        self.main_layout.addLayout(self.grid_layout)

        btn_show_add_attribute_dialog = QPushButton("添加")
        btn_show_add_attribute_dialog.setCursor(Qt.PointingHandCursor)
        btn_show_add_attribute_dialog.clicked.connect(
            self.show_add_attribute_dialog)

        btn_import_attribute = QPushButton("导入")
        btn_import_attribute.setObjectName("importBtn")
        btn_import_attribute.setCursor(Qt.PointingHandCursor)
        btn_import_attribute.clicked.connect(self.import_attribute)

        self.top_layout.addWidget(btn_show_add_attribute_dialog, 1)
        self.top_layout.addWidget(btn_import_attribute, 1)

    def show_attributes(self):
        """
        显示所有属性
        """
        for item in self.attributes.items():
            self.add_attribute(item)

    def add_attribute(self, attribute_item: tuple[str, list[str]]):
        container = QWidget()
        # 设置对象名称以应用特定样式，只对容器设置边框，不影响子控件
        container.setObjectName("attributeContainer")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)  # 增加内边距
        container.setLayout(main_layout)
        self.grid_layout.addWidget(container)

        label = QLabel(attribute_item[0])
        label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(label)

        h_layout = QHBoxLayout()
        main_layout.addLayout(h_layout)

        btn_edit_attribute = QPushButton("编辑")
        btn_edit_attribute.setObjectName("editBtn")
        btn_edit_attribute.setCursor(Qt.PointingHandCursor)
        btn_edit_attribute.clicked.connect(self.show_edit_attribute_dialog)
        btn_edit_attribute.setProperty("attribute_key", attribute_item)
        h_layout.addWidget(btn_edit_attribute)

        btn_delete_attribute = QPushButton("删除")
        btn_delete_attribute.setObjectName("deleteBtn")
        btn_delete_attribute.setCursor(Qt.PointingHandCursor)
        btn_delete_attribute.clicked.connect(self.delete_attribute)
        btn_delete_attribute.setProperty("attribute_key", container)
        h_layout.addWidget(btn_delete_attribute)

        attr_name = attribute_item[0]
        attr_values = attribute_item[1]

        item_str = f"""
            <div style='background-color: #f0f0f0; padding: 12px; border-radius: 6px; border-left: 4px solid #2196F3;'>
                <div style='color: #2196F3; font-weight: bold; font-size: 16px; margin-bottom: 8px; 
                    border-bottom: 1px solid #ddd; padding-bottom: 5px;'>{attr_name}
                </div>
            <div style='max-height: 200px; overflow-y: auto;'>
        """

        for i, value in enumerate(attr_values, 1):
            bg_color = "#ffffff" if i % 2 == 0 else "#f8f8f8"
            item_str += f"""
            <div style='background-color: {bg_color}; padding: 5px 8px; margin: 3px 0; border-radius: 4px;'>
                <span style='color: #2196F3; font-weight: bold;'>{i}.</span> {value}
            </div>
            """

        item_str += """
            </div>
        </div>
        """

        container.setToolTip(item_str)

    def delete_attribute(self):
        message_box = CustomMessageBox(self)
        result = message_box.exec("提示", "确定删除该属性吗？")

        if result == QMessageBox.Yes:
            # 获取发送信号的按钮
            sender = self.sender()
            # 获取按钮的属性,QWidget对象
            container = sender.property("attribute_key")
            self.grid_layout.removeWidget(container)

    def import_attribute(self):
        print("导入属性")

    def show_add_attribute_dialog(self):
        dialog = EditAttributeDialog(
            parent=self, mode=0, exits_attributes=self.attributes.keys())
        # dialog.setWindowModality(Qt.ApplicationModal)
        # dialog.show() # 即使设置了setWindowModality(Qt.ApplicationModal)，
        # 使用show()或者open()还是不会阻塞，所以如果需要获取返回值，需要使用exec_()

        # 使用exec_()会阻塞，直到对话框关闭
        result = dialog.exec_()

        if result == QDialog.Accepted:
            attribute_data = dialog.attribute_data
            self.add_attribute(attribute_data)

    def show_edit_attribute_dialog(self):
        # 获取发送信号的按钮
        sender = self.sender()
        # 获取按钮的属性
        attribute_item = sender.property("attribute_key")
        dialog = EditAttributeDialog(
            parent=self, mode=1, attribute_item=attribute_item)
        result = dialog.exec_()

        if result == QDialog.Accepted:
            pass
