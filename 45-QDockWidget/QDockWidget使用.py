from PyQt5.QtWidgets import (QMainWindow, QDockWidget, QScrollArea, QWidget, QPushButton,
                             QVBoxLayout, QGroupBox, QCheckBox, QLabel, QApplication, QHBoxLayout, QLayout, QSizePolicy)
from PyQt5.QtCore import Qt, QPoint, QRect, QSize
from PyQt5.QtGui import QIcon
import sys
import json
from pathlib import Path


# 自定义流式布局类
class FlowLayout(QLayout):
    def __init__(self, parent=None, margin=0, spacing=-1):
        super().__init__(parent)
        self.setContentsMargins(margin, margin, margin, margin)
        self.setSpacing(spacing)
        self._items = []
        
    def __del__(self):
        while self._items:
            self.takeAt(0)
            
    def addItem(self, item):
        self._items.append(item)
        
    def count(self):
        return len(self._items)
        
    def itemAt(self, index):
        if 0 <= index < len(self._items):
            return self._items[index]
        return None
        
    def takeAt(self, index):
        if 0 <= index < len(self._items):
            return self._items.pop(index)
        return None
        
    def expandingDirections(self):
        return Qt.Orientations(0)
        
    def hasHeightForWidth(self):
        return True
        
    def heightForWidth(self, width):
        return self._do_layout(QRect(0, 0, width, 0), True)
        
    def setGeometry(self, rect):
        super().setGeometry(rect)
        self._do_layout(rect, False)
        
    def sizeHint(self):
        return self.minimumSize()
        
    def minimumSize(self):
        size = QSize()
        for item in self._items:
            size = size.expandedTo(item.minimumSize())
        margin = self.contentsMargins().left()
        size += QSize(2 * margin, 2 * margin)
        return size
        
    def _do_layout(self, rect, test_only):
        x = rect.x()
        y = rect.y()
        line_height = 0
        spacing = self.spacing()
        
        # 记录每行的起始索引和高度
        line_start = 0
        
        for i in range(len(self._items)):
            item = self._items[i]
            widget = item.widget()
            item_width = widget.sizeHint().width()
            item_height = widget.sizeHint().height()
            
            next_x = x + item_width + spacing
            
            # 换行判断
            if next_x - spacing > rect.right() and line_height > 0:
                # 当前行结束，调整该行所有item的垂直位置
                current_line_height = line_height
                for j in range(line_start, i):
                    item_j = self._items[j]
                    widget_j = item_j.widget()
                    item_j_height = widget_j.sizeHint().height()
                    y_offset = (current_line_height - item_j_height) // 2 + 3 # 垂直居中关键计算
                    
                    if not test_only:
                        pos = QPoint(item_j.geometry().x(), y + y_offset)
                        item_j.setGeometry(QRect(pos, widget_j.sizeHint()))
                
                x = rect.x()
                y = y + line_height + spacing
                next_x = x + item_width + spacing
                line_height = 0
                line_start = i  # 新行起始索引
                
            if not test_only:
                # 先按顶部对齐临时定位
                item.setGeometry(QRect(QPoint(x, y), item.sizeHint()))
            
            line_height = max(line_height, item_height)
            x = next_x
            
        # 处理最后一行
        current_line_height = line_height
        for j in range(line_start, len(self._items)):
            item_j = self._items[j]
            widget_j = item_j.widget()
            item_j_height = widget_j.sizeHint().height()
            y_offset = (current_line_height - item_j_height) // 2 + 3 # 垂直居中关键计算
            
            if not test_only:
                pos = QPoint(item_j.geometry().x(), y + y_offset)
                item_j.setGeometry(QRect(pos, widget_j.sizeHint()))
        
        return y + line_height - rect.y()


class AnnotationTool(QMainWindow):
    def __init__(self):
        super().__init__()
        self.attributes_list = []
        self.load_attributes()  # 加载属性

        if not self.attributes_list:
            print("属性为空,请检查attributes.json文件")
            return

        self.setup_ui()

    def load_attributes(self):
        """
        加载属性
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
        v_layout = QVBoxLayout(content) # 设置垂直布局
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
                flow_layout.addWidget(check_box)
                
            group_box.setLayout(flow_layout)
            v_layout.addWidget(group_box)

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
