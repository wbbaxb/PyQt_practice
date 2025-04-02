import sys
from PyQt5.QtWidgets import QWidget, QApplication, QListView, QGridLayout
from PyQt5.QtCore import QStringListModel, QSize


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QListView-大小调整模式、移动")
        self.resize(500, 500)
        self.data_list = [f"Item{i}" for i in range(15)]  # 将数据列表保存在属性中
        self.setup_ui()

    def setup_ui(self):
        layout = QGridLayout(self)  # 创建网格布局管理器
        self.setLayout(layout)
        list_view = QListView()  # 创建列表视图
        list_view.resize(200, 200)
        slm = QStringListModel()  # 创建model模型
        slm.setStringList(self.data_list)  # 为模型设置数据
        list_view.setModel(slm)  # 为视图设置模型
        list_view.setWrapping(True)  # 打开自动换行，默认为False

        # ---------布局网格-----------
        list_view.setGridSize(QSize(100, 100))  # 设置每个item的大小，此属性设置非空则开启网格布局
        # 设置为水平方向填充（默认为TopToBottom垂直填充）
        list_view.setFlow(QListView.LeftToRight)

        # ---------大小调整模式--------
        # list_view.setResizeMode(QListView.Fixed)  # 项目只会在视图第一次显示时进行布局
        list_view.setResizeMode(QListView.Adjust)  # 每次视图大小改变时，项目都重新布局

        list_view.setSpacing(20)  # 设置item之间的间距

        # 设置item Style，背景色为蓝色，选择时背景色为红色
        list_view.setStyleSheet("""
            QListView {
                background-color: lightblue;
            }
            QListView::item {
                background-color: green;
            }
            QListView::item:selected {
                background-color: red;
            }
        """)

        # --------移动模式---------
        # list_view.setMovement(QListView.Static)  # 用户不能移动项目
        # list_view.setMovement(QListView.Free)  # 用户可以自由移动项目
        list_view.setMovement(QListView.Snap)  # 项目在移动时对齐到指定的网格（需要开启网格布局）

        layout.addWidget(list_view)  # 通过布局管理器实现list_view大小随窗口大小改变而变化的效果


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
