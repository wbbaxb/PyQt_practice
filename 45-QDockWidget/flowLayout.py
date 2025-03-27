from PyQt5.QtWidgets import QLayout
from PyQt5.QtCore import Qt, QSize, QRect, QPoint


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
                    y_offset = (current_line_height -
                                item_j_height) // 2 + 3  # 垂直居中关键计算

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
            y_offset = (current_line_height -
                        item_j_height) // 2 + 3  # 垂直居中关键计算

            if not test_only:
                pos = QPoint(item_j.geometry().x(), y + y_offset)
                item_j.setGeometry(QRect(pos, widget_j.sizeHint()))

        return y + line_height - rect.y()
