from PyQt5.QtWidgets import QDialog, QHBoxLayout, QPushButton, QVBoxLayout, QLabel, QWidget, QMessageBox, QLineEdit, QFileDialog
from PyQt5.QtCore import Qt, pyqtSignal, QTimer
from PyQt5.QtGui import QIcon
from Common.UniformGridLayout import UniformGridLayout
from attribute_edit_dialog import AttributeEditDialog
from Common.custom_message_box import CustomMessageBox
from Common.attribute_config_helper import AttributeConfigHelper
from Common.excel_helper import ExcelHelper
from pathlib import Path
import json
import shutil


class ShowAttributesDialog(QDialog):
    attributes_changed = pyqtSignal(dict)  # 属性变化信号

    def __init__(self, attributes: dict, parent=None):
        super().__init__(parent=parent)
        self.attributes = attributes
        self.font_size = 16
        self.setup_style()
        self.setup_ui()

    def setup_style(self):
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
                background-color: #2196F3; /* 蓝色 */
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
            QLabel#rootNameLabel {{
                font-size: {self.font_size}px;
                font-weight: normal;
                color: black;
            }}
            QPushButton#saveBtn:disabled {{
                background-color: #f0f0f0; /* 灰色 */
            }}
            QLineEdit#rootNameInput {{
                border: 1px solid #2196F3; /* 蓝色 */
                border-radius: 5px;
                height: 35px;
                font-size: {self.font_size}px;
            }}
        """)

    def setup_ui(self):
        self.setWindowTitle("属性编辑")
        self.setWindowIcon(QIcon("./Icons/python_96px.ico"))
        self.resize(800, 600)
        self.setWindowFlags(Qt.Window | Qt.WindowTitleHint |
                            Qt.WindowMaximizeButtonHint | Qt.WindowCloseButtonHint)

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.top_layout = QHBoxLayout()
        self.main_layout.addLayout(self.top_layout)

        root_name_layout = QHBoxLayout()
        root_name_layout.setContentsMargins(0, 20, 0, 20)  # 设置布局上下边距为20
        self.main_layout.addLayout(root_name_layout)

        root_name_label = QLabel("根节点:")
        root_name_label.setObjectName("rootNameLabel")
        root_name_label.setAlignment(Qt.AlignCenter)
        root_name_layout.addWidget(root_name_label)

        root_name = next(iter(self.attributes.keys()))
        self.root_name_intput = QLineEdit(root_name)
        self.root_name_intput.setObjectName("rootNameInput")
        self.root_name_intput.setPlaceholderText("请输入根节点名称")
        root_name_layout.addWidget(self.root_name_intput)

        btn_save_root_name = QPushButton("保存")
        btn_save_root_name.setObjectName("saveBtn")
        btn_save_root_name.setFixedHeight(35)
        btn_save_root_name.setCursor(Qt.PointingHandCursor)
        btn_save_root_name.clicked.connect(self.update_root_name)
        root_name_layout.addWidget(btn_save_root_name)

        self.root_name_intput.textChanged.connect(
            lambda: btn_save_root_name.setEnabled(self.root_name_intput.text() != ""))

        self.grid_layout = UniformGridLayout()
        self.grid_layout.setSpacing(30)
        self.main_layout.addLayout(self.grid_layout)

        btn_show_add_attribute_dialog = QPushButton("添加")
        btn_show_add_attribute_dialog.setCursor(Qt.PointingHandCursor)
        btn_show_add_attribute_dialog.clicked.connect(
            self.show_add_attribute_dialog)

        self.btn_add = btn_show_add_attribute_dialog

        btn_import_attribute = QPushButton("导入")
        btn_import_attribute.setObjectName("importBtn")
        btn_import_attribute.setCursor(Qt.PointingHandCursor)
        btn_import_attribute.clicked.connect(self.import_attribute)

        self.top_layout.addWidget(btn_show_add_attribute_dialog, 1)
        self.top_layout.addWidget(btn_import_attribute, 1)

        self.show_attributes()
        btn_show_add_attribute_dialog.setFocus()

    def emit_attributes_changed(self):
        """异步发送属性变化信号"""
        QTimer.singleShot(
            0, lambda: self.attributes_changed.emit(self.attributes))

    def update_root_name(self):
        new_root_name = self.root_name_intput.text()
        old_root_name = next(iter(self.attributes.keys()))  # 始终从字典中获取根节点名称

        if new_root_name != old_root_name:
            # 获取旧键对应的值
            root_attributes = self.attributes[old_root_name]
            # 删除旧键
            del self.attributes[old_root_name]
            # 添加新键，值保持不变
            self.attributes[new_root_name] = root_attributes

            AttributeConfigHelper.save_config(self.attributes)  # 保存配置
            self.emit_attributes_changed()

            QMessageBox.information(self, "提示", f"根节点名称已更新为: {new_root_name}")

    def show_attributes(self):
        """
        显示所有属性
        """

        root_name = next(iter(self.attributes.keys()))
        attributes = self.attributes[root_name]

        # 清空布局中的所有控件
        for i in reversed(range(self.grid_layout.count())):
            widget = self.grid_layout.itemAt(i).widget()
            if widget:
                self.grid_layout.removeWidget(widget)
                widget.hide()
                widget.deleteLater()

        for item in attributes.items():
            self.add_attribute(item)

    def add_attribute(self, attribute_item: tuple[str, list[str]]):
        container = QWidget()
        container.setObjectName("attributeContainer")
        content_layout = QVBoxLayout()
        content_layout.setContentsMargins(10, 10, 10, 10)
        container.setLayout(content_layout)
        self.grid_layout.addWidget(container)

        attr_name = attribute_item[0]
        attr_values = attribute_item[1]

        label = QLabel(attr_name)
        label.setAlignment(Qt.AlignCenter)
        content_layout.addWidget(label)

        h_layout = QHBoxLayout()
        content_layout.addLayout(h_layout)

        btn_edit_attribute = QPushButton("编辑")
        btn_edit_attribute.setObjectName("editBtn")
        btn_edit_attribute.setCursor(Qt.PointingHandCursor)
        btn_edit_attribute.clicked.connect(self.show_edit_attribute_dialog)
        btn_edit_attribute.setProperty("attr_name", attr_name)
        btn_edit_attribute.setProperty("container", container)
        h_layout.addWidget(btn_edit_attribute)

        btn_delete_attribute = QPushButton("删除")
        btn_delete_attribute.setObjectName("deleteBtn")
        btn_delete_attribute.setCursor(Qt.PointingHandCursor)
        btn_delete_attribute.clicked.connect(self.delete_attribute)
        btn_delete_attribute.setProperty("attr_name", attr_name)
        btn_delete_attribute.setProperty("container", container)
        h_layout.addWidget(btn_delete_attribute)

        self.set_tooltip(container, attr_name, attr_values)

    def set_tooltip(self, container: QWidget, attr_name: str, attr_values: list[str]):
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
        sender = self.sender()
        container = sender.property("container")
        attr_name = sender.property("attr_name")

        message_box = CustomMessageBox(self)
        result = message_box.exec("提示", f"确定删除: {attr_name} 吗？")

        if result == QMessageBox.Yes:
            self.grid_layout.removeWidget(container)
            container.hide()
            container.deleteLater()

            root_name = next(iter(self.attributes.keys()))

            if attr_name in self.attributes[root_name]:
                del self.attributes[root_name][attr_name]
                AttributeConfigHelper.save_config(self.attributes)
                self.emit_attributes_changed()

            self.btn_add.setFocus()

            if attr_name in self.attributes[root_name]:
                QMessageBox.critical(self, "提示", f"属性: {attr_name} 删除失败")

    def import_attribute(self):
        """
        导入属性文件（json或者Excel）
        """

        result = QFileDialog.getOpenFileName(
            self,
            "选择Json或者Excel文件",
            "./",
            "Json文件(*.json);;Excel文件(*.xlsx *.xls)",
            "Json文件(*.json)"
        )

        if not isinstance(result, tuple):
            return

        file_path = result[0]

        if not file_path:
            return

        if Path(file_path).suffix == ".json":
            self.handle_json_file(file_path)
        elif Path(file_path).suffix in [".xlsx", ".xls"]:
            self.handle_excel_file(file_path)
        else:
            print(f"不支持的文件类型: {file_path}")
            return

    def handle_json_file(self, file_path):
        """
        处理JSON文件
        """
        with open(file_path, "r", encoding="utf-8") as f:
            self.attributes = json.load(f)

        config_path = AttributeConfigHelper.get_config_path()
        config_path.parent.mkdir(parents=True, exist_ok=True)  # 确保配置目录存在

        try:
            # 复制源文件到目标路径，保留元数据，如果目标文件存在会被覆盖
            shutil.copy2(file_path, config_path)
        except Exception as e:
            AttributeConfigHelper.save_config(self.attributes)

        self.show_attributes()

    def handle_excel_file(self, file_path):
        """
        处理Excel文件
        """
        print(f"处理Excel文件: {file_path}")

    def show_add_attribute_dialog(self):
        dialog = AttributeEditDialog(
            parent=self, mode=0, exits_attributes=self.attributes.keys())
        # dialog.setWindowModality(Qt.ApplicationModal)
        # dialog.show() # 即使设置了setWindowModality(Qt.ApplicationModal)，
        # 使用show()或者open()还是不会阻塞，所以如果需要获取返回值，需要使用exec_()

        # 使用exec_()会阻塞，直到对话框关闭
        result = dialog.exec_()

        if result == QDialog.Accepted:
            attribute_data = dialog.attribute_data
            self.add_attribute(attribute_data)

            # 将attribute_data添加到self.attributes中
            root_name = next(iter(self.attributes.keys()))
            self.attributes[root_name][attribute_data[0]] = attribute_data[1]

            # 保存配置并发送信号
            AttributeConfigHelper.save_config(self.attributes)
            self.emit_attributes_changed()

    def show_edit_attribute_dialog(self):
        sender = self.sender()
        attr_name = sender.property("attr_name")
        container = sender.property("container")
        root_name = next(iter(self.attributes.keys()))

        # 从数据源获取属性值
        if attr_name in self.attributes[root_name]:
            attr_values = self.attributes[root_name][attr_name]
            attribute_item = (attr_name, attr_values)

            dialog = AttributeEditDialog(
                parent=self, mode=1, attribute_item=attribute_item)

            result = dialog.exec_()

            if result == QDialog.Accepted:
                # 获取新属性数据
                new_attr_name = dialog.attribute_data[0]
                new_attr_values = dialog.attribute_data[1]

                # 如果属性名改变了，需要删除旧的属性
                if attr_name != new_attr_name:
                    del self.attributes[root_name][attr_name]

                # 更新属性值
                self.attributes[root_name][new_attr_name] = new_attr_values

                # 保存配置并发送信号
                AttributeConfigHelper.save_config(self.attributes)
                self.emit_attributes_changed()

                self.set_tooltip(container, new_attr_name, new_attr_values)
        else:
            QMessageBox.warning(self, "警告", f"找不到属性: {attr_name}")
