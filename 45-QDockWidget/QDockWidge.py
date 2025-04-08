from PyQt5.QtWidgets import (QMainWindow, QDockWidget, QScrollArea, QWidget, QPushButton,
                             QVBoxLayout, QGroupBox, QCheckBox, QApplication, QFileDialog)
from PyQt5.QtCore import Qt
import sys
import json
from pathlib import Path
from Common.flowLayout import FlowLayout
from attribut_edit_dialog import AttributeEditDialog
from Common.utils import WindowUtils
from attribute_config_helper import AttributeConfigHelper


class AnnotationTool(QMainWindow):
    def __init__(self):
        super().__init__()

        self.attributes = AttributeConfigHelper.get_config()
        self.image_attribute_dict = {}
        self.image_attribute_path = Path(__file__).parent / "舌图.json"
        self.load_image_attribute()
        self.font_size = 16
        self.setup_style()
        self.setup_ui()

    def load_image_attribute(self):
        """
        加载图片属性文件
        """

        if not self.image_attribute_path.exists():
            print(f"图片标注文件不存在: {self.image_attribute_path}")
            return

        with open(self.image_attribute_path, "r", encoding="utf-8") as f:
            image_data = json.load(f)

            shapes = image_data.get("shapes", [])

            if not shapes:
                return

            attributes = shapes[0].get("attributes", {})

            if not attributes:
                return

            # 为了兼容之前标注过的舌图JSON文件,处理字符串或者列表
            for key, val in attributes.items():
                if isinstance(val, str):
                    self.image_attribute_dict[key] = [val]
                elif isinstance(val, list):
                    self.image_attribute_dict[key] = val

    def setup_style(self):
        self.setStyleSheet(f"""
            QCheckBox {{
                font-size: {self.font_size}px;
                color: black;
            }}
            QPushButton#edit_btn, QPushButton#toggle_dock_btn {{
                color: white;
                border-radius: 10px;
            }}
            
            QPushButton#edit_btn {{
                background-color: green;
                height: 30px;
            }}
            QPushButton#toggle_dock_btn {{
                background-color: orange;
                height: 50px;
            }}
            
            QPushButton#edit_btn:hover, QPushButton#toggle_dock_btn:hover {{
                background-color: rgb(73, 170, 159);
            }}
            QPushButton#edit_btn:pressed, QPushButton#toggle_dock_btn:pressed {{
                background-color: rgb(234, 208, 112);
            }}
            
            QGroupBox {{
                font-size: {self.font_size}px;
                border: 1px solid lightblue;
                border-radius: 3px;
                margin-top: 20px;
                padding: 20px 10px;  /* 增加垂直和水平内边距 */
            }}
            QGroupBox::title {{
                left: 0;
                padding: 0;
                background-color: lightblue;
                border-radius: 2px;
                font-size: {self.font_size}px;
            }}
            QWidget#main_container {{
                background-color: lightblue;
            }}
        """)

    def setup_ui(self):
        """
        初始化UI
        """

        self.main_layout = QVBoxLayout()

        container = QWidget()
        container.setObjectName('main_container')
        container.setLayout(self.main_layout)

        self.setCentralWidget(container)  # 将widget设置为中央窗口部件

        self.btn_toggle = QPushButton("切换停靠控件")
        self.btn_toggle.setObjectName("toggle_dock_btn")
        self.btn_toggle.setCursor(Qt.PointingHandCursor)
        self.btn_toggle.clicked.connect(self.toggle_dock)
        self.main_layout.addWidget(self.btn_toggle)

        if not self.attributes:
            self.btn_import = QPushButton("尚未导入属性文件，点击导入")
            self.btn_import.setCursor(Qt.PointingHandCursor)
            self.btn_import.clicked.connect(self.import_attribute)
            self.main_layout.addWidget(self.btn_import)

        self.set_dock_widget()

    def set_dock_widget(self):
        """
        设置停靠窗口
        """

        self.dock = QDockWidget("属性设置", self)
        self.dock.setMinimumWidth(500)
        self.dock.setMinimumHeight(300)
        self.dock.visibilityChanged.connect(self.dock_visibility_changed)

        # 第一个参数是停靠窗口的位置，第二个参数是停靠窗口（QDockWidget对象）
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock)

        self.dock_container = QWidget()
        self.dock.setWidget(self.dock_container)

        self.dock_layout = QVBoxLayout()
        self.dock_container.setLayout(self.dock_layout)

        self.add_edit_group_box()

        # 创建滚动区域容器
        scroll = QScrollArea()
        content = QWidget()

        # 创建布局并设置给内容控件
        self.attributes_layout = QVBoxLayout()
        content.setLayout(self.attributes_layout)

        scroll.setWidget(content)  # 设置滚动区域的部件为content
        scroll.setWidgetResizable(True)  # 设置滚动区域部件是否可调整大小

        # 将滚动区域添加到dock_layout中
        self.dock_layout.addWidget(scroll)

    def add_edit_group_box(self):
        """
        添加编辑组框
        """

        self.v_layout = QVBoxLayout()
        self.v_layout.setSpacing(30)
        self.dock_layout.addLayout(self.v_layout)
        edit_group_box = QGroupBox("编辑")
        edit_layout = QVBoxLayout()
        edit_group_box.setLayout(edit_layout)
        self.v_layout.addWidget(edit_group_box)

        btn_edit = QPushButton("编辑")
        btn_edit.setCursor(Qt.PointingHandCursor)
        btn_edit.setObjectName("edit_btn")
        edit_layout.addWidget(btn_edit)
        btn_edit.clicked.connect(self.show_edit_window)

    def set_attribute_group_box(self):
        """
        设置属性组框
        """
        # 检查attributes是否有嵌套结构
        if len(self.attributes) == 1 and isinstance(next(iter(self.attributes.values())), dict):
            # 如果是嵌套结构，获取第一个键对应的值作为属性字典
            first_key = next(iter(self.attributes.keys()))
            attribute_dict = self.attributes[first_key]
        else:
            # 如果不是嵌套结构，直接使用attributes
            attribute_dict = self.attributes

        # 先清空attributes_layout中的所有控件
        while self.attributes_layout.count():
            item = self.attributes_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        for key, val in attribute_dict.items():
            group_box = QGroupBox(key)

            flow_layout = FlowLayout(spacing=20)

            # 添加选项
            for option in val:
                check_box = QCheckBox(option)
                check_box.setCursor(Qt.PointingHandCursor)

                # 设置属性存储分类名称和选项名称
                check_box.setProperty("attribute_type", key)
                check_box.setProperty("option_name", option)

                if key in self.image_attribute_dict:
                    if option in self.image_attribute_dict[key]:
                        check_box.setChecked(True)

                check_box.toggled.connect(self.check_box_toggled)
                flow_layout.addWidget(check_box)

            group_box.setLayout(flow_layout)
            self.attributes_layout.addWidget(group_box)

    def show_edit_window(self):
        """
        显示编辑窗口,需要设置parent=self，否则编辑窗口会闪退
        """
        dialog = AttributeEditDialog(attributes=self.attributes, parent=self)
        WindowUtils.center_on_parent(dialog)
        dialog.exec()

    def check_box_toggled(self, value):
        """
        复选框状态变化时触发
        """
        sender = self.sender()  # 获取发送信号的复选框对象

        if sender:
            # 获取存储在复选框属性中的分类和选项名称
            attribute_type = sender.property("attribute_type")
            option_name = sender.property("option_name")

            self.update_attribute_list(attribute_type, option_name, value)

    def update_attribute_list(self, attribute_type, option_name, value):
        """
        更新属性列表
        """

        if not self.image_attribute_dict:
            self.image_attribute_dict = {}

        if attribute_type not in self.image_attribute_dict:
            self.image_attribute_dict[attribute_type] = []

        if value:
            if option_name not in self.image_attribute_dict[attribute_type]:
                self.image_attribute_dict[attribute_type].append(option_name)
        else:
            if option_name in self.image_attribute_dict[attribute_type]:
                self.image_attribute_dict[attribute_type].remove(option_name)

        self.save_image_attribute()

    def save_image_attribute(self):
        """
        保存图片属性到舌图JSON文件
        """
        if not self.image_attribute_path.exists():
            return

        try:
            # 读取当前的JSON文件
            with open(self.image_attribute_path, "r", encoding="utf-8") as f:
                image_data = json.load(f)

                shapes = image_data.get("shapes", [])

                if not shapes:
                    return

                shapes[0]["attributes"] = self.image_attribute_dict

            # 将更新后的数据写回文件
            with open(self.image_attribute_path, "w", encoding="utf-8") as f:
                json.dump(image_data, f, ensure_ascii=False, indent=2)

        except Exception as e:
            print(f"保存舌图属性时出错: {str(e)}")

    def import_attribute(self):
        """
        导入属性文件（json或者Excel）
        """
        result = QFileDialog.getOpenFileName(
            self,
            "选择一个Json文件或者Excel文件",
            "./",
            "所有文件(*);;Json文件(*.json);;Excel文件(*.xlsx *.xls)",
            "Json文件(*.json)"
        )

        if isinstance(result, tuple) and result[0]:
            # 导入成功后，读取文件内容
            with open(result[0], "r", encoding="utf-8") as f:
                self.attributes = json.load(f)

            self.btn_import.deleteLater()
            self.set_attribute_group_box()

    def dock_visibility_changed(self, visible):
        """
        停靠窗口可见性变化时触发
        """
        if visible:
            self.btn_toggle.setText("隐藏停靠窗口")
        else:
            self.btn_toggle.setText("显示停靠窗口")

    def toggle_dock(self):
        """
        切换停靠窗口的可见性
        """
        if self.dock.isVisible():
            self.dock.hide()
        else:
            self.dock.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AnnotationTool()
    window.resize(1000, 800)
    # window.setWindowIcon(QIcon("./Icons/python_96px.ico"))
    # window.setWindowTitle("QDockWidget Demo")
    WindowUtils.center_on_screen(window)
    window.show()
    sys.exit(app.exec_())
