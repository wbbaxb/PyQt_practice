from PyQt5.QtWidgets import (QMainWindow, QDockWidget, QScrollArea, QWidget, QPushButton,
                             QVBoxLayout, QGroupBox, QCheckBox, QLabel, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import sys
import json
from pathlib import Path
from flowLayout import FlowLayout


class AnnotationTool(QMainWindow):
    def __init__(self):
        super().__init__()

        self.attributes_list = []
        self.load_attributes()  # 加载属性

        if not self.attributes_list:
            print("属性为空,请检查attributes.json文件")
            return

        self.image_attribute_dict = {}
        self.image_attribute_path = Path(__file__).parent / "舌图.json"
        self.load_image_attribute()

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
                return []

            attribute_types = attributes.get("舌头", {})

            for attribute_type, attribute_options in attribute_types.items():
                dict_attribute = {
                    'name': attribute_type,
                    'options': attribute_options
                }

                self.attributes_list.append(dict_attribute)

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

            print(type(attributes))

            if not attributes:
                return

            for key, val in attributes.items():
                if isinstance(val, str):
                    self.image_attribute_dict[key] = [val]
                elif isinstance(val, list):
                    self.image_attribute_dict[key] = val

    def setup_ui(self):
        """
        初始化UI
        """

        self.set_main_layout()
        self.set_dock_widget()

    def set_dock_widget(self):
        """
        设置停靠窗口
        """
        # 创建停靠属性面板,第一个参数是停靠窗口的标题，第二个参数是停靠窗口的父窗口
        self.dock = QDockWidget("属性设置", self)
        self.dock.setMinimumWidth(200)  # 设置最小宽度
        self.dock.setMinimumHeight(200)  # 设置最小高度

        # 第一个参数是停靠窗口的位置，第二个参数是停靠窗口（QDockWidget对象）
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock)

        # 滚动区域容器
        scroll = QScrollArea()
        content = QWidget()
        v_layout = QVBoxLayout(content)  # 设置垂直布局
        # 设置垂直布局的间距
        v_layout.setSpacing(30)

        for attribute in self.attributes_list:
            group_box = QGroupBox(attribute['name'])

            group_box.setStyleSheet("""
                QGroupBox {
                    font-size: 15px;
                    border: 1px solid lightblue;
                    border-radius: 3px;
                    margin-top: 20px;
                    padding: 20px 10px;  /* 增加垂直和水平内边距 */
                }
                QGroupBox::title {
                    left: 0;
                    padding: 0;
                    background-color: lightblue;
                    border-radius: 2px;
                }
            """)

            # 使用自定义的流式布局
            flow_layout = FlowLayout(spacing=20)

            # 添加选项
            for option in attribute['options']:
                check_box = QCheckBox(option)
                check_box.setCursor(Qt.PointingHandCursor)
                check_box.setStyleSheet("""
                    QCheckBox {
                        font-size: 15px;
                        color: #000000;
                    }
                """)

                # 设置属性存储分类名称和选项名称
                check_box.setProperty("attribute_type", attribute['name'])
                check_box.setProperty("option_name", option)

                check_box.toggled.connect(self.check_box_toggled)
                flow_layout.addWidget(check_box)

            group_box.setLayout(flow_layout)
            v_layout.addWidget(group_box)

        scroll.setWidget(content)  # 设置滚动区域的部件为content
        scroll.setWidgetResizable(True)  # 设置滚动区域部件是否可调整大小
        self.dock.setWidget(scroll)  # 设置停靠窗口的部件为scroll
        self.dock.visibilityChanged.connect(self.dock_visibility_changed)

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
        print(f"复选框状态变化: 分类[{attribute_type}] 选项[{option_name}] 状态[{value}]")

    def set_main_layout(self):
        """
        设置主布局
        """
        self.v_layout = QVBoxLayout()

        self.add_label()
        self.add_btn()

        # 创建一个容器widget来包含布局
        container = QWidget()
        container.setLayout(self.v_layout)  # 将布局设置到widget上
        container.setStyleSheet("background-color: lightblue;")

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
        self.btn.setStyleSheet("""
            QPushButton {
                background-color: orange;
                color: white;
                height: 50px;
                border-radius: 10px;
            }
        """)
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
    window.setWindowIcon(QIcon("./Icons/python_96px.ico"))
    window.setWindowTitle("QDockWidget Demo")

    # 移动窗口到屏幕中心
    screen = QApplication.primaryScreen()
    center_point = screen.availableGeometry().center()
    x = int(center_point.x() - window.width() / 2)
    y = int(center_point.y() - window.height() / 2)
    window.move(x, y)

    window.show()

    sys.exit(app.exec_())
