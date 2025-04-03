import math
from PyQt5.QtWidgets import QGridLayout


class UniformGridLayout(QGridLayout):
    """
    自定义网格布局，模拟WPF的UniformGrid
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSpacing(0)
        self.setContentsMargins(0, 0, 0, 0)
        self._optimal_columns = 1
        self._items = []

    def addWidget(self, widget):
        self._items.append(widget)
        self.updateLayout()

    def removeWidget(self, widget):
        if widget in self._items:
            self._items.remove(widget)
            super().removeWidget(widget)
            widget.deleteLater()
            self.updateLayout()

    def updateLayout(self):
        # 计算最佳列数
        item_count = len(self._items)
        if item_count > 0:
            self._optimal_columns = int(math.ceil(math.sqrt(item_count)))
        else:
            self._optimal_columns = 1

        # 重新添加所有项目到网格
        for index, widget in enumerate(self._items):
            row = index // self._optimal_columns
            col = index % self._optimal_columns
            super().addWidget(widget, row, col)
