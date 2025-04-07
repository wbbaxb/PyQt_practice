from PyQt5.QtWidgets import (QDialog, QHBoxLayout, QPushButton, QVBoxLayout, QWidget, QListWidgetItem,
                             QLabel, QLineEdit, QListWidget, QFrame, QMessageBox)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from Common.screen_info import ScreenInfo


class CustomItemWidget(QWidget):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.screen_info = ScreenInfo.get_screen_info()
        self.font_size = int(self.screen_info[1] * 14 * 1.1)

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setAlignment(Qt.AlignVCenter)
        self.setLayout(self.main_layout)

        self.frame = QFrame()
        self.frame.setMinimumSize(QSize(100, 50))
        self.main_layout.addWidget(self.frame)

        self.h_layout = QHBoxLayout()
        self.h_layout.setContentsMargins(0, 0, 0, 0)
        self.h_layout.setAlignment(Qt.AlignVCenter)
        self.h_layout.setSpacing(0)
        self.frame.setLayout(self.h_layout)

        self.label = QLabel(text)
        self.label.setObjectName("CustomItemLabel")

        self.button = QPushButton("删除")
        self.button.setMinimumSize(QSize(50, 20))
        self.button.setObjectName("CustomItemButton")
        self.button.setCursor(Qt.PointingHandCursor)

        self.h_layout.addWidget(self.label, 6, alignment=Qt.AlignVCenter)
        self.h_layout.addWidget(self.button, 1, alignment=Qt.AlignVCenter)

        self.setup_style()

    def get_size(self) -> QSize:
        return self.frame.minimumSize()

    def setup_style(self):
        self.setStyleSheet(f"""
            #CustomItemLabel {{
                font-size: {self.font_size}px;
                color: black;
                background-color: transparent;
            }}
            #CustomItemButton {{
                background-color: red;
                color: white;
                border-radius: 4px;
                font-size: {int(self.font_size)}px;
            }}
            #CustomItemButton:hover {{
                background-color: rgb(198, 122, 211);
            }}
            #CustomItemButton:pressed {{
                background-color: rgb(206, 200, 229);
            }}
        """)


class AddNewAttributeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName("addNewAttributeDialog")
        self.screen_info = ScreenInfo.get_screen_info()
        self.font_size = int(self.screen_info[1] * 14 * 1.1)
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
                height: {int(self.screen_info[1]*30)}px;
            }}
            #valuesList::item {{
                height: {int(self.screen_info[1]*20)}px;
                padding: 0px 20px  /* 上下0px，左右20px */
            }}
            #nameGroup, #valuesGroup {{
                border-radius: 5px;
            }}
        """)

    def setup_ui(self):
        self.setWindowTitle("添加属性")
        self.setWindowIcon(QIcon("./Icons/python_96px.ico"))
        self.resize(
            int(500 * self.screen_info[1]), int(550 * self.screen_info[1]))
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
        print(f'size.width:{size.width()},size.height:{size.height()}')
        item.setSizeHint(size)

        custom_widget.button.clicked.connect(
            lambda checked=False, item=item: self.delete_attribute_value(item))

    def confirm_add_attribute(self):
        """确认添加属性"""
        attribute_name = self.name_input.text().strip()

        if not attribute_name:
            QMessageBox.warning(self, "警告", "请输入属性名称!")
            return

        if not self.get_all_items():
            QMessageBox.warning(self, "警告", "请至少添加一个属性值!")
            return

        print(f"属性名称: {attribute_name}")
        print(f"属性值: {self.get_all_items()}")

        self.accept()  # 成功添加后关闭窗口

    def cancel(self):
        self.reject()  # 关闭对话框


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    dialog = AddNewAttributeDialog()
    sys.exit(dialog.exec_())
