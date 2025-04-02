import sys
import random
from PyQt5.QtWidgets import QWidget, QApplication, QTabWidget, QLabel,  QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTabWidget")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.tab_layout = QVBoxLayout()
        self.btn_layout = QVBoxLayout()
        self.main_layout.addLayout(self.tab_layout)
        self.main_layout.addLayout(self.btn_layout)

        self.tab_widget = QTabWidget()
        self.tab_layout.addWidget(self.tab_widget)
        self.setup_tab()
        self.setup_btn()
        self.set_tab_signal()

    def add_tab(self):
        tab_count = self.tab_widget.count()  # 返回当前tab的数量
        str_tab = f"Tab {tab_count}"
        label = QLabel(str_tab)
        self.tab_widget.addTab(label, str_tab)

    def setup_tab(self):
        for _ in range(3):
            self.add_tab()

    def setup_btn(self):
        btn_add = QPushButton("Add Tab")
        btn_add.clicked.connect(self.add_tab)
        self.btn_layout.addWidget(btn_add)

        btn_set_pos = QPushButton("Set Tab Position")
        btn_set_pos.clicked.connect(self.set_tab_position)
        self.btn_layout.addWidget(btn_set_pos)

        btn_set_shape = QPushButton("Set Tab Shape")
        btn_set_shape.clicked.connect(self.set_tab_shape)
        self.btn_layout.addWidget(btn_set_shape)

        btn_set_movable = QPushButton("Set Tab Movable")
        btn_set_movable.clicked.connect(
            lambda: self.tab_widget.setMovable(not self.tab_widget.isMovable()))
        self.btn_layout.addWidget(btn_set_movable)

        btn_set_closable = QPushButton("Set Tab Closable")
        btn_set_closable.clicked.connect(self.set_tab_closable)
        self.btn_layout.addWidget(btn_set_closable)

        btn_set_auto_hide = QPushButton("Set Tab Auto Hide")
        btn_set_auto_hide.clicked.connect(
            # 设置标签自动隐藏,当只剩一个标签页时自动隐藏tabbar
            lambda: self.tab_widget.setTabBarAutoHide(True))
        self.btn_layout.addWidget(btn_set_auto_hide)

        btn_set_document_mode = QPushButton("Set Tab Document Mode")
        btn_set_document_mode.clicked.connect(
            # 设置文档模式
            # 此属性设置为True时，不会呈现选项卡部件框架，即选项卡页面和其后的窗口等页面无框架区分看起来是一个整体。
            # 此模式对于页面需要显示文档类型的情况非常有用，因为节省了选项卡部件框架占用的部分空间。
            lambda: self.tab_widget.setDocumentMode(not self.tab_widget.documentMode()))
        self.btn_layout.addWidget(btn_set_document_mode)

        btn_remove_last_tab = QPushButton("Remove Last Tab")
        btn_remove_last_tab.clicked.connect(self.remove_last_tab)
        self.btn_layout.addWidget(btn_remove_last_tab)

        btn_clear_tabs = QPushButton("Clear Tabs")
        btn_clear_tabs.clicked.connect(lambda: self.tab_widget.clear())
        self.btn_layout.addWidget(btn_clear_tabs)

        btn_set_last_tab_disabled = QPushButton("Set Last Tab Disabled")
        btn_set_last_tab_disabled.clicked.connect(self.set_last_tab_disabled)
        self.btn_layout.addWidget(btn_set_last_tab_disabled)

        btn_set_tab_scroll_buttons = QPushButton("Set Tab Scroll Buttons")
        btn_set_tab_scroll_buttons.clicked.connect(
            # 控制当选项卡栏有多个选项卡无足够空间显示时是否使用按钮滚动选项卡
            # 默认为True，当空间不足以显示全部页签时，添加一个滚动按钮以滚动显示被隐藏的页签
            # 如果为False，则不显示滚动按钮，当不够显示时，会自动撑大宽度
            lambda: self.tab_widget.setUsesScrollButtons(not self.tab_widget.usesScrollButtons()))
        self.btn_layout.addWidget(btn_set_tab_scroll_buttons)

        btn_set_icon = QPushButton("Set Tab Icon")
        btn_set_icon.clicked.connect(self.set_tab_icon)
        self.btn_layout.addWidget(btn_set_icon)

        btn_insert_tab_by_icon = QPushButton("Insert Tab By Icon")
        btn_insert_tab_by_icon.clicked.connect(self.insert_tab_by_icon)
        self.btn_layout.addWidget(btn_insert_tab_by_icon)

    def set_tab_icon(self):
        """设置tab标签图标"""
        self.tab_widget.setTabIcon(self.tab_widget.count() - 1, QIcon("./Icons/OS_Ubuntu_128px.ico"))

    def insert_tab_by_icon(self):
        """在最前面插入tab标签图标并设置图标"""
        self.tab_widget.insertTab(0, QLabel("First Tab"), QIcon("./Icons/OS_Ubuntu_128px.ico"), "First Tab")

    def set_last_tab_disabled(self):
        """
        设置最后一个标签页不可用
        页面上仍然能看到标签页，但是变成灰色、不可选中
        同时选中的标签页会自动切换到前一个标签页
        """
        tab_count = self.tab_widget.count()

        if tab_count > 1:
            self.tab_widget.setTabEnabled(tab_count - 1, False)
        else:
            print("只剩一个标签页，不能设置为不可用")

    def remove_last_tab(self):
        """删除最后一个标签页"""
        tab_count = self.tab_widget.count()

        if tab_count > 1:
            self.tab_widget.removeTab(tab_count - 1)
        else:
            print("只剩一个标签页，不能删除")

    def set_tab_closable(self):
        """设置标签可关闭"""

        if self.tab_widget.tabsClosable():
            self.tab_widget.setTabsClosable(False)
        else:
            # 这一步只是外观上添加关闭按钮，真正关闭标签页需要连接关闭信号
            self.tab_widget.setTabsClosable(True)

        def close_tab(index):
            """
            真正关闭标签页的槽函数

            Args:
                index: 要关闭的标签页的索引
            """
            self.tab_widget.removeTab(index)  # 删除指定索引的标签页

        self.tab_widget.tabCloseRequested.connect(close_tab)

    def set_tab_position(self):
        """设置tab标签位置"""
        random_pos = random.randint(0, 3)
        self.tab_widget.setTabPosition(random_pos)
        # self.tab_widget.setTabPosition(QTabWidget.North) # 标签在上方
        # self.tab_widget.setTabPosition(QTabWidget.South) # 标签在下方
        # self.tab_widget.setTabPosition(QTabWidget.West) # 标签在左侧
        # self.tab_widget.setTabPosition(QTabWidget.East) # 标签在右侧

    def set_tab_shape(self):
        """设置tab标签形状"""
        random_shape = random.randint(0, 1)
        self.tab_widget.setTabShape(random_shape)
        # self.tab_widget.setTabShape(QTabWidget.Rounded) # 圆角
        # self.tab_widget.setTabShape(QTabWidget.Triangular) # 三角形

    def set_tab_signal(self):
        """设置tab标签信号"""
        self.tab_widget.currentChanged.connect(
            lambda index: print(f"当前页面变成了{index}！"))
        self.tab_widget.tabBarClicked.connect(
            lambda index: print(f"索引为{index}的页签被点击了！"))
        self.tab_widget.tabBarDoubleClicked.connect(
            lambda index: print(f"索引为{index}的页签被双击了！"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
