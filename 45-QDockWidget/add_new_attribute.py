from PyQt5.QtWidgets import (QDialog, QHBoxLayout, QPushButton, QVBoxLayout, QWidget, QListWidgetItem,
                             QLabel, QLineEdit, QListWidget, QFrame, QMessageBox)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from customitem_widget import CustomItemWidget


class AddNewAttributeDialog(QDialog):
    def __init__(self, parent=None, exits_attributes: list[str] = None):
        super().__init__(parent=parent)
        self.exits_attributes = exits_attributes
        self.setObjectName("addNewAttributeDialog")
        self.font_size = 16
        self.setup_ui()
        self.setup_style()

    def setup_style(self):
        """
        防止继承父对话框的样式
        """
        self.setStyleSheet(f"""
            /* 重置从父对话框继承的样式 */
            #addNewAttributeDialog, #nameGroup, #valuesGroup, #nameInput, #valueInput, #valuesList {{
                background-color: white;
            }}
            
            /* 通用按钮样式 */
            #addValueBtn, #confirmBtn, #cancelBtn {{
                border-radius: 5px;
                background-color: #2196F3;
                padding: 10px 20px;
                font-size: {self.font_size}px;
                font-weight: bold;
            }}
            
            /* 红色按钮样式 */
            #cancelBtn {{
                background-color: #f44336;
            }}
            
            /* 按钮状态 */
            #addValueBtn:disabled, #confirmBtn:disabled {{
                background-color: gray;
                color: white;
            }}
            #addValueBtn:hover, #confirmBtn:hover {{
                background-color: rgb(73, 170, 159);
            }}
            #addValueBtn:pressed, #confirmBtn:pressed {{
                background-color: rgb(234, 208, 112);
            }}
            #cancelBtn:hover {{
                background-color: rgb(198, 122, 211);
            }}
            #cancelBtn:pressed {{
                background-color: rgb(206, 200, 229);
            }}
            
            /* 其他控件样式 */
            #nameTitle, #valuesTitle {{
                font-size: {self.font_size}px;
                font-weight: bold;
                color: black;
                border: none;
            }}
            #nameInput, #valueInput {{
                font-size: {self.font_size}px;
                border: 1px solid #2196F3;
                border-radius: 5px;
                padding: 4px;
            }}
            #valuesList {{
                border: 2px solid #cccccc;
                border-radius: 8px;
                height: 150px;
            }}
            #valuesList::item {{
                height: 20px;
                padding: 0px 20px  /* 上下0px，左右20px */
            }}
            #nameGroup, #valuesGroup {{
                border-radius: 5px;
            }}
        """)

    def setup_ui(self):
        self.setWindowTitle("添加属性")
        self.setWindowIcon(QIcon("./Icons/python_96px.ico"))
        self.resize(500, 550)
        self.move(500, 500)
        self.setWindowFlags(Qt.Window | Qt.WindowTitleHint |
                            Qt.WindowMaximizeButtonHint | Qt.WindowCloseButtonHint)

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        # 属性名称部分
        name_group = QFrame()
        name_group.setObjectName("nameGroup")
        name_group.setFrameShape(QFrame.StyledPanel)  # 设置为圆角
        name_layout = QVBoxLayout(name_group)
        self.main_layout.addWidget(name_group)

        # 属性名标题
        name_title = QLabel("属性名称")
        name_title.setObjectName("nameTitle")
        name_layout.addWidget(name_title)

        # 属性名输入
        name_input_layout = QHBoxLayout()
        name_layout.addLayout(name_input_layout)

        self.name_input = QLineEdit()
        self.name_input.setObjectName("nameInput")
        self.name_input.setPlaceholderText("请输入属性名称")
        self.name_input.setClearButtonEnabled(True)
        name_input_layout.addWidget(self.name_input)

        # 属性值部分
        values_group = QFrame()
        values_group.setObjectName("valuesGroup")
        values_group.setFrameShape(QFrame.StyledPanel)  # 设置为圆角
        values_layout = QVBoxLayout(values_group)
        self.main_layout.addWidget(values_group)

        # 属性值标题
        values_title = QLabel("属性值")
        values_title.setObjectName("valuesTitle")
        values_layout.addWidget(values_title)

        # 属性值输入
        value_input_layout = QHBoxLayout()
        values_layout.addLayout(value_input_layout)

        self.value_input = QLineEdit()
        self.value_input.setObjectName("valueInput")
        self.value_input.setPlaceholderText("请输入属性值")
        self.value_input.setClearButtonEnabled(True)
        self.value_input.textChanged.connect(
            lambda: self.add_value_btn.setEnabled(self.value_input.text() != ""))
        value_input_layout.addWidget(self.value_input)

        # 添加属性值按钮
        self.add_value_btn = QPushButton("添加值")
        self.add_value_btn.setObjectName("addValueBtn")
        self.add_value_btn.setEnabled(False)
        self.add_value_btn.setCursor(Qt.PointingHandCursor)
        self.add_value_btn.clicked.connect(self.add_attribute_value)
        value_input_layout.addWidget(self.add_value_btn)

        # 显示已添加的值列表
        self.values_list = QListWidget()
        self.values_list.setObjectName("valuesList")
        self.values_list.setMinimumHeight(150)
        values_layout.addWidget(self.values_list)

        # 底部按钮
        btn_layout = QHBoxLayout()
        self.main_layout.addLayout(btn_layout)

        # 确认添加按钮
        btn_confirm = QPushButton("确认")
        btn_confirm.setObjectName("confirmBtn")
        btn_confirm.setCursor(Qt.PointingHandCursor)
        btn_confirm.clicked.connect(self.confirm_add_attribute)
        btn_layout.addWidget(btn_confirm)

        # 取消按钮
        btn_cancel = QPushButton("取消")
        btn_cancel.setObjectName("cancelBtn")
        btn_cancel.setCursor(Qt.PointingHandCursor)
        btn_cancel.clicked.connect(self.cancel)
        btn_layout.addWidget(btn_cancel)

    def add_attribute_value(self):
        """添加属性值到列表"""
        value = self.value_input.text().strip()
        if not value:
            return

        if value in self.get_all_items():
            QMessageBox.warning(self, "警告", "该值已存在!", QMessageBox.Ok)
            return

        self.add_attribute_value_to_list(value)
        self.value_input.clear()

    def delete_attribute_value(self, item):
        """删除选中的属性值"""
        index = self.values_list.row(item)
        self.values_list.takeItem(index)

    def get_all_items(self) -> list[str]:
        """
        获取所有列表项
        """
        item_count = self.values_list.count()
        all_items = []

        # 遍历所有项目
        for i in range(item_count):
            item = self.values_list.item(i)
            widget = self.values_list.itemWidget(item)
            if widget:
                all_items.append(widget.label.text())

        return all_items

    def add_attribute_value_to_list(self, value):
        """添加属性值到列表"""
        item = QListWidgetItem()
        self.values_list.addItem(item)

        # 创建自定义 Widget 并关联到 Item
        custom_widget = CustomItemWidget(value)
        self.values_list.setItemWidget(item, custom_widget)

        # 设置更合适的大小提示，以确保QFrame正确居中显示
        size = custom_widget.get_size()
        item.setSizeHint(size)

        custom_widget.button.clicked.connect(
            lambda checked=False, item=item: self.delete_attribute_value(item))

    def confirm_add_attribute(self):
        """确认添加属性"""
        attribute_name = self.name_input.text().strip()

        if not attribute_name:
            QMessageBox.warning(self, "警告", "请输入属性名!")
            return

        if self.exits_attributes and attribute_name in self.exits_attributes:
            QMessageBox.critical(self, "错误", f'{attribute_name}已存在!')
            return

        value_list = self.get_all_items()
        if not value_list:
            QMessageBox.warning(self, "警告", "请至少添加一个属性值!")
            return

        # 设置对话框的返回数据
        self.attribute_data = {
            "name": attribute_name,
            "values": value_list
        }

        self.accept()

    def cancel(self):
        self.reject()
