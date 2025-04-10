from PyQt5.QtWidgets import (QDialog, QHBoxLayout, QPushButton, QVBoxLayout, QListWidgetItem,
                             QLabel, QLineEdit, QListWidget, QFrame, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from Common.customitem_widget import CustomItemWidget
from Common.utils import WindowUtils
from Common.style_util import load_style


class AttributeEditDialog(QDialog):
    def __init__(self, parent=None, mode: int = 0, attributes: dict[str, list[str]] = None, attribute_item: tuple[str, list[str]] = None):
        """
        mode: 0 添加属性 1 编辑属性
        attributes: 属性列表, 添加属性时需要传入
        attribute_item: 属性项, 编辑属性时需要传入
        """
        super().__init__(parent=parent)
        self.label_width = 80
        WindowUtils.center_on_screen(self)
        self.attributes = attributes
        self.mode = mode
        self.attribute_item = attribute_item
        self.setObjectName("editAttributeDialog")
        self.resize(400, 500)
        self.setup_ui()
        self.init_attribute_item()
        self.setup_style()

    def setup_style(self):
        self.setStyleSheet(load_style())

    def setup_ui(self):
        self.setWindowTitle("添加属性" if self.mode == 0 else "编辑属性")
        self.setWindowIcon(QIcon("./Icons/python_96px.ico"))
        self.setWindowFlags(Qt.Window | Qt.WindowTitleHint |
                            Qt.WindowMaximizeButtonHint | Qt.WindowCloseButtonHint)

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        # 属性名称部分
        name_group = QFrame()
        name_group.setObjectName("nameGroup")
        name_group.setFrameShape(QFrame.StyledPanel)  # 设置为圆角
        name_layout = QHBoxLayout(name_group)
        self.main_layout.addWidget(name_group)

        # 属性名标题
        name_title = QLabel("属性名称：")
        name_title.setFixedWidth(self.label_width)
        name_title.setObjectName("nameTitle")
        name_layout.addWidget(name_title)

        if self.mode == 0 and self.attributes:  # 添加属性
            self.name_input = QLineEdit()
            self.name_input.setObjectName("nameInput")
            self.name_input.setPlaceholderText("请输入属性名称")
            self.name_input.setClearButtonEnabled(True)
            name_layout.addWidget(self.name_input)
        elif self.mode == 1 and self.attribute_item:  # 编辑属性
            self.name_label = QLabel(self.attribute_item[0])
            self.name_label.setAlignment(
                Qt.AlignLeft | Qt.AlignVCenter)  # 左对齐，垂直居中
            self.name_label.setObjectName("nameLabel")
            name_layout.addWidget(self.name_label)
            name_layout.setStretch(1, 10)

        # 属性值部分
        values_group = QFrame()
        values_group.setObjectName("valuesGroup")
        values_group.setFrameShape(QFrame.StyledPanel)  # 设置为圆角
        values_layout = QVBoxLayout(values_group)
        self.main_layout.addWidget(values_group)

        values_input_layout = QHBoxLayout()
        values_layout.addLayout(values_input_layout)

        # 属性值标题
        values_title = QLabel("属性值：")
        values_title.setFixedWidth(self.label_width)
        values_title.setObjectName("valuesTitle")
        values_title.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)  # 左对齐，垂直居中
        values_input_layout.addWidget(values_title)

        self.value_input = QLineEdit()
        self.value_input.setObjectName("valueInput")
        self.value_input.setPlaceholderText("请输入属性值")
        self.value_input.setClearButtonEnabled(True)
        self.value_input.textChanged.connect(
            lambda: self.add_value_btn.setEnabled(self.value_input.text() != ""))
        values_input_layout.addWidget(self.value_input)

        # 添加属性值按钮
        self.add_value_btn = QPushButton("添加属性值")
        self.add_value_btn.setObjectName("addValueBtn")
        self.add_value_btn.setEnabled(False)
        self.add_value_btn.setCursor(Qt.PointingHandCursor)
        self.add_value_btn.clicked.connect(self.add_attribute_value)
        values_input_layout.addWidget(self.add_value_btn)

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

    def init_attribute_item(self):
        """初始化属性项"""
        if self.mode == 1 and self.attribute_item:  # 编辑属性
            for item in self.attribute_item[1]:
                self.add_attribute_value_to_list(item)

    def add_attribute_value(self):
        """添加属性值到列表"""
        value = self.value_input.text().strip()
        if not value:
            return

        if value in self.get_all_items():
            QMessageBox.warning(
                self, "警告", f"属性值：{value} 已存在!", QMessageBox.Ok)
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

        # 确保QFrame正确居中显示
        size = custom_widget.get_size()
        item.setSizeHint(size)

        custom_widget.button.clicked.connect(
            lambda checked=False, item=item: self.delete_attribute_value(item))

    def confirm_add_attribute(self) -> tuple[str, list[str]]:
        """确认添加属性"""

        attribute_name = self.name_input.text().strip(
        ) if self.mode == 0 else self.name_label.text()

        if self.mode == 0:
            if not attribute_name:
                QMessageBox.warning(self, "警告", "请输入属性名!")
                return

            root_name = next(iter(self.attributes.keys()))

            if self.attributes and attribute_name in self.attributes[root_name]:
                QMessageBox.critical(
                    self, "错误", f'属性：{attribute_name} 已存在，请勿重复添加!')
                return

        value_list = self.get_all_items()

        if not value_list:
            QMessageBox.warning(self, "警告", "请至少添加一个属性值!")
            return

        # 设置对话框的返回数据
        self.attribute_data = (attribute_name, value_list)

        self.accept()

    def cancel(self):
        self.reject()
