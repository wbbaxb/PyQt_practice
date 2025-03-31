import sys
from pprint import pprint

from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QTreeView
from PyQt5.QtGui import QStandardItemModel, QStandardItem

"""
下拉框的模型操作和视图操作，可自由设置下拉框的视图类型
"""

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QComboBox-模型操作、视图操作")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        cbb = QComboBox(self)
        cbb.move(100, 100)
        cbb.resize(200, 20)

        # -----模型操作-------
        model = QStandardItemModel()  # 创建树状模型

        item_1 = QStandardItem("item_1")  # 创建一级项
        item_2 = QStandardItem("item_2")  # 创建一级项
        item_22 = QStandardItem("item_22")  # 创建二级项
        item_2.appendRow(item_22)  # 将二级项添加到一级项中
        model.appendRow(item_1)  # 将一级项添加到模型中
        model.appendRow(item_2)  # 将二级项添加到模型中

        cbb.setModel(model)
        # 此时因为视图还是列表视图，无法显示二级选项

        cbb.setView(QTreeView(cbb))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
