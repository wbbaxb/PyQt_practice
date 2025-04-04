from PyQt5.QtWidgets import (QDialog, QHBoxLayout, QPushButton, QVBoxLayout,
                             QLabel, QWidget, QLineEdit, QListWidget, QScrollArea,
                             QFrame, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


class AddNewAttributeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.attribute_values = []  # 存储属性可能的值
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("添加属性")
        self.setWindowIcon(QIcon("./Icons/python_96px.ico"))
        self.resize(400, 450)
        self.move(500, 500)
        self.setWindowFlags(Qt.Window | Qt.WindowTitleHint |
                            Qt.WindowMaximizeButtonHint | Qt.WindowCloseButtonHint)

        # 设置子对话框独立的样式表，防止继承父样式
        self.setStyleSheet("""
            /* 重置从父对话框继承的样式 */
            AddNewAttributeDialog {
                background-color: #f0f0f0;
            }
            QLabel {
                font-size: 12px;
                font-weight: normal;
                color: #333333;
                border: none;
            }
            QLineEdit {
                border: 1px solid #cccccc;
                border-radius: 3px;
                padding: 4px;
                background-color: white;
            }
            QLineEdit:focus {
                border-color: #5d80c1;
            }
            QListWidget {
                border: 1px solid #cccccc;
                background-color: white;
                border-radius: 3px;
            }
            QListWidget::item {
                height: 25px;
                padding: 3px;
            }
            QListWidget::item:selected {
                background-color: #5d80c1;
                color: white;
            }
        """)

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        # 属性名称部分
        name_group = QFrame()
        name_group.setFrameShape(QFrame.StyledPanel) # 设置为圆角
        name_group.setStyleSheet(
            "background-color: white; border-radius: 5px;")
        name_layout = QVBoxLayout(name_group)
        self.main_layout.addWidget(name_group)

        # 属性名标题
        name_title = QLabel("属性名称")
        name_title.setStyleSheet("font-weight: bold; font-size: 14px;")
        name_layout.addWidget(name_title)

        # 属性名输入
        name_input_layout = QHBoxLayout()
        name_layout.addLayout(name_input_layout)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("请输入属性名称")
        name_input_layout.addWidget(self.name_input)

        # 属性值部分
        values_group = QFrame()
        values_group.setFrameShape(QFrame.StyledPanel) # 设置为圆角
        values_group.setStyleSheet(
            "background-color: white; border-radius: 5px;")
        values_layout = QVBoxLayout(values_group)
        self.main_layout.addWidget(values_group)

        # 属性值标题
        values_title = QLabel("属性值")
        values_title.setStyleSheet("font-weight: bold; font-size: 14px;")
        values_layout.addWidget(values_title)

        # 属性值输入
        value_input_layout = QHBoxLayout()
        values_layout.addLayout(value_input_layout)

        self.value_input = QLineEdit()
        self.value_input.setPlaceholderText("请输入属性值")
        self.value_input.textChanged.connect(self.update_add_value_btn_style)
        value_input_layout.addWidget(self.value_input)

        # 添加属性值按钮
        self.add_value_btn = QPushButton("添加值")
        self.add_value_btn.setStyleSheet("height: 30px;background-color: lightblue;")
        self.add_value_btn.setEnabled(False)
        self.add_value_btn.setObjectName("addValueBtn")
        self.add_value_btn.setCursor(Qt.PointingHandCursor)
        self.add_value_btn.clicked.connect(self.add_attribute_value)
        value_input_layout.addWidget(self.add_value_btn)

        # 显示已添加的值列表
        self.values_list = QListWidget()
        self.values_list.setMinimumHeight(150)
        values_layout.addWidget(self.values_list)

        # 删除选中值按钮
        delete_value_btn = QPushButton("删除")
        delete_value_btn.setObjectName("deleteValueBtn")
        delete_value_btn.setCursor(Qt.PointingHandCursor)
        delete_value_btn.clicked.connect(self.delete_attribute_value)
        values_layout.addWidget(delete_value_btn)

        self.update_values_list()

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

    def update_add_value_btn_style(self):
        """更新添加属性值按钮的样式"""
        if self.value_input.text():
            self.add_value_btn.setEnabled(True)
        else:
            self.add_value_btn.setEnabled(False)

    def add_attribute_value(self):
        """添加属性值到列表"""
        value = self.value_input.text().strip()
        if not value:
            return
        
        if value in self.attribute_values:
            QMessageBox.warning(self, "警告", "该值已存在!", QMessageBox.Ok)
            return

        self.attribute_values.append(value)
        self.update_values_list()
        self.value_input.clear()

    def delete_attribute_value(self):
        """删除选中的属性值"""
        current_item = self.values_list.currentItem()
        if current_item:
            value = current_item.text()

            self.attribute_values.remove(value)
            self.update_values_list()

    def update_values_list(self):
        """更新属性值列表显示"""
        self.values_list.clear()
        for value in self.attribute_values:
            self.values_list.addItem(value)

    def confirm_add_attribute(self):
        """确认添加属性"""
        attribute_name = self.name_input.text().strip()

        if not attribute_name:
            QMessageBox.warning(self, "警告", "请输入属性名称!")
            return

        print(f"添加属性: {attribute_name}")
        print(f"属性值: {self.attribute_values}")

        self.accept()  # 成功添加后关闭窗口

    def cancel(self):
        self.reject()  # 关闭对话框
