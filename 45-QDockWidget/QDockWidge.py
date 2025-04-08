from PyQt5.QtWidgets import (QMainWindow, QDockWidget, QScrollArea, QWidget, QPushButton,
                             QVBoxLayout, QGroupBox, QCheckBox, QLabel, QApplication)
from PyQt5.QtCore import Qt
import sys
import json
from pathlib import Path
from Common.flowLayout import FlowLayout
from attribut_edit_dialog import AttributeEditDialog


class AnnotationTool(QMainWindow):
    def __init__(self):
        super().__init__()

        self.attributes = {}  # 属性列表
        self.load_attributes()  # 加载属性

        if not self.attributes:
            print("属性为空,请检查attributes.json文件")
            return

        self.image_attribute_dict = {}
        self.image_attribute_path = Path(__file__).parent / "舌图.json"
        self.load_image_attribute()
        self.font_size = 16
        self.setup_ui()

    def load_attributes(self):
        """
        加载属性文件
        """
        path = Path(__file__).parent / "attributes.json"

        if not path.exists():
            print(f"文件不存在: {path}")
            return []

        with open(path, "r", encoding="utf-8") as f:
            attributes = json.load(f)

            if not attributes:
                return {}

            keys = list(attributes.keys())
            key = keys[0] if keys else []

            if not key:
                return {}

            self.attributes = attributes.get(key, {})

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
                    if val:
                        self.image_attribute_dict[key] = [val]
                    else:
                        self.image_attribute_dict[key] = ['unknown']
                elif isinstance(val, list):
                    self.image_attribute_dict[key] = val

                    # 如果是空列表，设置为["unknown"]
                    if not val:
                        self.image_attribute_dict[key] = ["unknown"]
                    else:
                        self.image_attribute_dict[key] = val

    def setup_ui(self):
        """
        初始化UI
        """

        self.set_main_layout()
        self.set_dock_widget()

        self.setStyleSheet(f"""
            /* 按钮通用样式 */
            QPushButton#edit_btn, QPushButton#toggle_dock_btn {{
                color: white;
                border-radius: 10px;
            }}
            
            /* 特定按钮样式 */
            QPushButton#edit_btn {{
                background-color: green;
                height: 30px;
            }}
            QPushButton#toggle_dock_btn {{
                background-color: orange;
                height: 50px;
            }}
            
            /* 按钮悬停和按下效果 */
            QPushButton#edit_btn:hover, QPushButton#toggle_dock_btn:hover {{
                background-color: rgb(73, 170, 159);
            }}
            QPushButton#edit_btn:pressed, QPushButton#toggle_dock_btn:pressed {{
                background-color: rgb(234, 208, 112);
            }}
            
            /* 组框样式 */
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
            
            /* 主容器背景 */
            QWidget#main_container {{
                background-color: lightblue;
            }}
        """)

    def set_dock_widget(self):
        """
        设置停靠窗口
        """
        # 创建停靠属性面板,第一个参数是停靠窗口的标题，第二个参数是停靠窗口的父窗口
        self.dock = QDockWidget("属性设置", self)
        self.dock.setMinimumWidth(500)  # 设置最小宽度
        self.dock.setMinimumHeight(300)  # 设置最小高度

        # 第一个参数是停靠窗口的位置，第二个参数是停靠窗口（QDockWidget对象）
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock)

        # 滚动区域容器
        scroll = QScrollArea()
        content = QWidget()
        content.setObjectName('v_layout_content')
        self.v_layout = QVBoxLayout(content)  # 设置垂直布局
        # 设置垂直布局的间距
        self.v_layout.setSpacing(30)

        self.add_edit_group_box()

        # 遍历self.attributes字典
        for key, val in self.attributes.items():
            group_box = QGroupBox(key)

            # 使用自定义的流式布局
            flow_layout = FlowLayout(spacing=20)

            # 添加选项
            for option in val:
                check_box = QCheckBox(option)
                check_box.setCursor(Qt.PointingHandCursor)

                color = 'red' if option == 'unknown' else '#000000'

                # 设置复选框的样式
                check_box.setStyleSheet(f"""
                    QCheckBox {{
                        font-size: {self.font_size}px;
                        color: {color};
                    }}
                """)

                # 设置属性存储分类名称和选项名称
                check_box.setProperty("attribute_type", key)
                check_box.setProperty("option_name", option)

                if key in self.image_attribute_dict:
                    if option in self.image_attribute_dict[key]:
                        check_box.setChecked(True)

                check_box.toggled.connect(self.check_box_toggled)
                flow_layout.addWidget(check_box)

            group_box.setLayout(flow_layout)
            self.v_layout.addWidget(group_box)

        scroll.setWidget(content)  # 设置滚动区域的部件为content
        scroll.setWidgetResizable(True)  # 设置滚动区域部件是否可调整大小
        self.dock.setWidget(scroll)  # 设置停靠窗口的部件为scroll
        self.dock.visibilityChanged.connect(self.dock_visibility_changed)

    def add_edit_group_box(self):
        """
        添加编辑组框
        """

        edit_group_box = QGroupBox("编辑")
        edit_layout = QVBoxLayout()
        edit_group_box.setLayout(edit_layout)
        self.v_layout.addWidget(edit_group_box)

        btn_edit = QPushButton("编辑")
        btn_edit.setCursor(Qt.PointingHandCursor)
        btn_edit.setObjectName("edit_btn")
        edit_layout.addWidget(btn_edit)
        btn_edit.clicked.connect(self.show_edit_window)

    def show_edit_window(self):
        """
        显示编辑窗口,需要设置parent=self，否则编辑窗口会闪退
        """
        dialog = AttributeEditDialog(attributes=self.attributes, parent=self)
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.show()

    def check_box_toggled(self, value):
        """
        复选框状态变化时触发
        """
        sender = self.sender()  # 获取发送信号的复选框对象

        if sender:
            # 获取存储在复选框属性中的分类和选项名称
            attribute_type = sender.property("attribute_type")
            option_name = sender.property("option_name")

            # 增加互斥逻辑
            if value:  # 当选中某个选项时
                # 如果选中的是 "unknown"，则取消同组中其他选项
                if option_name == "unknown":
                    self.clear_other_options(attribute_type, "unknown")
                # 如果选中的不是 "unknown"，则取消同组中的 "unknown" 选项
                else:
                    self.clear_option(attribute_type, "unknown")

            self.update_attribute_list(attribute_type, option_name, value)

    def clear_other_options(self, attribute_type, except_option):
        """
        清除同一组中除了指定选项外的所有选项
        """
        # 查找所有带有相同 attribute_type 属性的复选框
        for child in self.findChildren(QCheckBox):  # 获取当前窗口中所有复选框
            if (child.property("attribute_type") == attribute_type and child.property("option_name") != except_option and child.isChecked()):
                # 暂时断开信号连接，防止触发 toggled 信号引起循环
                child.blockSignals(True)
                child.setChecked(False)
                child.blockSignals(False)
                # 更新属性列表
                self.update_attribute_list(
                    attribute_type, child.property("option_name"), False)

    def clear_option(self, attribute_type, option_name):
        """
        清除指定组中的指定选项
        """
        # 查找特定的复选框
        for child in self.findChildren(QCheckBox):  # 获取当前窗口中所有复选框
            if (child.property("attribute_type") == attribute_type and child.property("option_name") == option_name and child.isChecked()):
                # 暂时断开信号连接，防止触发 toggled 信号引起循环
                child.blockSignals(True)
                child.setChecked(False)
                child.blockSignals(False)
                # 更新属性列表
                self.update_attribute_list(attribute_type, option_name, False)

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

                # 如果移除后该属性组没有任何选项，则自动选中unknown选项
                if not self.image_attribute_dict[attribute_type] and option_name != "unknown":
                    # 查找unknown复选框并选中它
                    for child in self.findChildren(QCheckBox):
                        if (child.property("attribute_type") == attribute_type and
                                child.property("option_name") == "unknown"):
                            # 阻止信号以避免递归
                            child.blockSignals(True)
                            child.setChecked(True)
                            child.blockSignals(False)
                            # 更新属性列表
                            self.image_attribute_dict[attribute_type].append(
                                "unknown")
                            break

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

    def set_main_layout(self):
        """
        设置主布局
        """
        self.v_layout = QVBoxLayout()

        self.add_label()
        self.add_btn()

        # 创建一个容器widget来包含布局
        container = QWidget()
        container.setObjectName('main_container')
        container.setLayout(self.v_layout)  # 将布局设置到widget上

        self.setCentralWidget(container)  # 将widget设置为中央窗口部件

    def add_label(self):
        """
        添加标签
        """
        for i in range(1, 11):
            label = QLabel(f"Label {i}")
            self.v_layout.addWidget(label)

    def add_btn(self):
        """
        添加按钮
        """
        self.btn = QPushButton("切换停靠控件")
        self.btn.setObjectName("toggle_dock_btn")
        self.btn.setCursor(Qt.PointingHandCursor)
        self.btn.clicked.connect(self.toggle_dock)
        self.v_layout.addWidget(self.btn)

    def dock_visibility_changed(self, visible):
        """
        停靠窗口可见性变化时触发
        """
        if visible:
            self.btn.setText("隐藏停靠窗口")
        else:
            self.btn.setText("显示停靠窗口")

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
    window.resize(800, 600)
    # window.setWindowIcon(QIcon("./Icons/python_96px.ico"))
    # window.setWindowTitle("QDockWidget Demo")

    # 移动窗口到屏幕中心
    screen = QApplication.primaryScreen()
    center_point = screen.availableGeometry().center()
    x = int(center_point.x() - window.width() / 2)
    y = int(center_point.y() - window.height() / 2)
    window.move(x, y)
    window.show()

    # window.showMaximized()

    sys.exit(app.exec_())
