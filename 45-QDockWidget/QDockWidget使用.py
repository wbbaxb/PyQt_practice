
from PyQt5.QtWidgets import (QMainWindow, QDockWidget, QScrollArea, QWidget, QPushButton,
                             QVBoxLayout, QGroupBox, QCheckBox, QLabel, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import sys


class AnnotationTool(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()

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

        # 设置样式表
        self.dock.setStyleSheet("""
            QWidget {
                background-color: #ffcccc;  /* 内容区域背景色 */
            }
        """)

        # 第一个参数是停靠窗口的位置，第二个参数是停靠窗口（QDockWidget对象）
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock)

        # 滚动区域容器
        scroll = QScrollArea()
        content = QWidget()
        layout = QVBoxLayout(content)

        # 示例属性组：颜色
        group_color = QGroupBox("颜色")
        color_layout = QVBoxLayout()
        color_layout.addWidget(QCheckBox("红"))
        color_layout.addWidget(QCheckBox("绿"))
        color_layout.addWidget(QCheckBox("蓝"))
        group_color.setLayout(color_layout)
        layout.addWidget(group_color)

        scroll.setWidget(content)  # 设置滚动区域的部件为content
        scroll.setWidgetResizable(True)  # 设置滚动区域部件是否可调整大小
        self.dock.setWidget(scroll)  # 设置停靠窗口的部件为scroll
        self.dock.visibilityChanged.connect(self.dock_visibility_changed)

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
