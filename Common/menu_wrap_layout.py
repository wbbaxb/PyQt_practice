from PyQt5.QtWidgets import QLayout, QVBoxLayout, QLabel, QFrame
from PyQt5.QtCore import Qt, QSize, QRect,  pyqtSignal, QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QCursor


class WrapLayout(QLayout):
    """
    仿WPF的WrapPanel
    自动调整每行显示的最大数量，使得布局更加均衡
    """

    def __init__(self, parent=None, max_items_per_row=4, spacing=20):
        super().__init__(parent)
        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(spacing)
        self._items = []
        self._max_items_per_row = max_items_per_row
        self._max_width = 0
        self._is_animating = False

    def set_max_width(self, max_width):
        """设置最大宽度"""
        self._max_width = max_width
        self.invalidate()  # 标记需要重新布局

    def calculate_items_per_row(self, total_items):
        """计算每行最优的项目数量"""
        max_items = self._max_items_per_row

        # 计算需要多少行来均匀分布所有元素
        rows_needed = (total_items + max_items - 1) // max_items

        # 根据行数计算每行应该有多少个元素
        if rows_needed <= 0:
            return 1
        items_per_row = (total_items + rows_needed - 1) // rows_needed

        return min(items_per_row, max_items)  # 确保不超过最大限制

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
        return Qt.Orientations(0)  # 不自动扩展

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
        """执行布局"""
        spacing = self.spacing()

        # 可见项目总数
        visible_items = [
            item for item in self._items if item.widget().isVisible()]
        visible_count = len(visible_items)

        if visible_count == 0:
            return 0

        # 计算每行的项目数量
        items_per_row = self.calculate_items_per_row(visible_count)

        # 获取磁贴的固定尺寸
        tile_width = 133  # 固定宽度
        tile_height = 133  # 固定高度

        # 计算需要的行数
        rows_needed = (visible_count + items_per_row - 1) // items_per_row

        # 计算总宽度（一行的宽度）
        total_width = items_per_row * tile_width + \
            (items_per_row - 1) * spacing

        # 计算水平居中的起始位置
        start_x = rect.x() + (rect.width() - total_width) // 2
        start_y = rect.y()

        # 布局所有可见项目
        row, col = 0, 0
        for item in visible_items:
            # 计算位置
            x = start_x + col * (tile_width + spacing)
            y = start_y + row * (tile_height + spacing)

            # 设置项目位置和大小
            if not test_only:
                item.setGeometry(QRect(x, y, tile_width, tile_height))

            # 更新行和列
            col += 1
            if col >= items_per_row:
                col = 0
                row += 1

        # 返回布局高度
        return start_y + rows_needed * tile_height + (rows_needed - 1) * spacing


class MenuTile(QFrame):
    clicked = pyqtSignal(object)  # 点击信号

    def __init__(self, name, data=None, parent=None):
        super().__init__(parent)
        self._data = data
        self._name = name
        self._is_hovered = False

        # 设置固定大小
        self.setFixedSize(133, 133)

        # 设置圆角和背景色
        self.setStyleSheet("""
            QFrame {
                background-color: #0078d7;
                border-radius: 5px;
            }
        """)

        # 创建垂直布局
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)

        # 创建文本标签
        self.label = QLabel(name)
        self.label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 22px;
                font-family: "Microsoft YaHei";
            }
        """)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        # 设置鼠标样式
        self.setCursor(QCursor(Qt.PointingHandCursor))

        # 创建动画效果
        self._animation = QPropertyAnimation(self, b"windowOpacity")
        self._animation.setDuration(150)
        self._animation.setEasingCurve(QEasingCurve.InOutCubic)

    def enterEvent(self, event):
        self._is_hovered = True
        self._animation.setStartValue(1.0)
        self._animation.setEndValue(0.8)
        self._animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._is_hovered = False
        self._animation.setStartValue(0.8)
        self._animation.setEndValue(1.0)
        self._animation.start()
        super().leaveEvent(event)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit(self._data or self._name)
        super().mousePressEvent(event)

    def getData(self):
        return self._data

    def getName(self):
        return self._name
