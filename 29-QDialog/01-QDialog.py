import sys
from PyQt5.QtWidgets import QWidget, QApplication, QDialog, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QGroupBox
from PyQt5.QtCore import Qt

"""
对话窗口的基类
对话窗口是顶级窗口，主要用于短期任务和与用户的简短通信
QDialog可能是模态的或非模态对话框：
"""

"""
模态对话框：
分类：应用程序级别与窗口级别

应用程序级别：
默认值
当该种模态的对话框出现时，用户必须首先对对话框进行交互，直到关闭对话框，然后
exec()

窗口级别：
该模态仅仅阻塞与对话框关联的窗口，但是依然允许用户与程序中其他窗口交互
open()

应用场景：文件选择、是否同意……
"""

"""
非模态对话框：
不会阻塞与对话框关联的窗口以及与其他窗口进行交互

show()
结合 setModal(True)也可以实现模态对话框
结合setWindowModality(Qt.WindowModal)也可以实现模态对话框 Qt.WindowModal Qt.ApplicationModal

应用场景：查找替换
"""


class CustomDialog(QDialog):
    """自定义对话框类"""

    def __init__(self, title="对话框", parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.resize(300, 200)

        # 创建对话框内部布局
        layout = QVBoxLayout()
        self.setLayout(layout)

        # 添加标签
        label = QLabel(f"这是一个{title}")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        # 添加关闭按钮
        close_btn = QPushButton("关闭")
        close_btn.clicked.connect(self.close)
        layout.addWidget(close_btn)
        # 显示最小化，最大化，关闭按钮
        self.setWindowFlags(Qt.Window | Qt.WindowTitleHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint | Qt.WindowCloseButtonHint)

        # 禁止窗口调整大小
        self.setFixedSize(self.size())

class DialogTest(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("对话框演示")
        self.resize(500, 500)
        self.move(400, 250)

        # 主布局
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # 添加说明标签
        desc_label = QLabel("点击按钮尝试不同类型的对话框")
        desc_label.setAlignment(Qt.AlignCenter)


        # 创建模态对话框分组
        modal_group = QGroupBox("模态对话框")
        modal_layout = QVBoxLayout()
        modal_group.setLayout(modal_layout)

        # 应用程序级模态按钮
        self.app_modal_exec_btn = QPushButton("应用程序级模态 (exec)")
        self.app_modal_exec_btn.clicked.connect(
            self.show_app_modal_exec_dialog)
        modal_layout.addWidget(self.app_modal_exec_btn)

        # 应用程序级模态按钮 - 使用setWindowModality
        self.app_modal_btn = QPushButton("应用程序级模态 (通过setWindowModality)")
        self.app_modal_btn.clicked.connect(self.show_app_modal_dialog)
        modal_layout.addWidget(self.app_modal_btn)

        # 窗口级模态按钮 - 使用open方法
        self.window_modal_open_btn = QPushButton("窗口级模态 (open)")
        self.window_modal_open_btn.clicked.connect(
            self.show_window_modal_open_dialog)
        modal_layout.addWidget(self.window_modal_open_btn)

        # 窗口级模态按钮 - 使用setWindowModality
        self.window_modal_btn = QPushButton("窗口级模态 (通过setWindowModality)")
        self.window_modal_btn.clicked.connect(self.show_window_modal_dialog)
        modal_layout.addWidget(self.window_modal_btn)

        # 创建非模态对话框分组
        non_modal_group = QGroupBox("非模态对话框")
        non_modal_layout = QVBoxLayout()
        non_modal_group.setLayout(non_modal_layout)

        # 非模态按钮
        self.non_modal_btn = QPushButton("非模态 (show)")
        self.non_modal_btn.clicked.connect(self.show_non_modal_dialog)
        non_modal_layout.addWidget(self.non_modal_btn)

        other_layout = QVBoxLayout()
        other_group = QGroupBox("其他")
        other_group.setLayout(other_layout)

        btn_common = QPushButton("其他")
        btn_common.clicked.connect(self.show_common_dialog)
        other_layout.addWidget(btn_common)

        main_layout.addWidget(desc_label)
        main_layout.addWidget(modal_group)
        main_layout.addWidget(non_modal_group)
        main_layout.addWidget(other_group)

        # 设置布局拉伸比例
        main_layout.setStretch(0, 1)
        main_layout.setStretch(1, 5)
        main_layout.setStretch(2, 5)
        main_layout.setStretch(3, 5)

    def show_common_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("通用对话框")
        dialog.setSizeGripEnabled(True)  # 设置为可调整大小，右下角显示尺寸调整控件

        # 自定义对话框内部布局
        layout = QHBoxLayout()
        dialog.setLayout(layout)

        btn1 = QPushButton("accept")
        btn1.clicked.connect(lambda: dialog.accept()) # 关闭对话框，返回1

        btn2 = QPushButton("reject")
        btn2.clicked.connect(lambda: dialog.reject()) # 关闭对话框，返回0

        btn3 = QPushButton("done")
        btn3.clicked.connect(lambda: dialog.done(8)) # 关闭对话框，返回指定值8

        btn4 = QPushButton("setResult")
        btn4.clicked.connect(lambda: dialog.setResult(888)) # 不关闭对话框，可以通过d.result()获取

        btn5 = QPushButton("result")
        btn5.clicked.connect(lambda: print(dialog.result())) # 不关闭对话框，可以通过d.result()
                
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)
        layout.addWidget(btn5)

        res = dialog.exec()
        print(f"通用对话框返回结果：{res}")

    def show_app_modal_exec_dialog(self):
        """
        显示应用程序级模态对话框
        特点：阻塞整个应用程序，用户必须先关闭此对话框才能与应用程序的其他窗口交互
        适用场景：重要的确认、必须处理的警告等
        """
        dialog = CustomDialog("应用程序级模态对话框", self)
        # 使用exec()方法显示应用程序级模态对话框
        # exec()会阻塞程序执行，直到对话框关闭，并返回一个DialogCode
        result = dialog.exec()
        print(f"应用程序级模态对话框返回结果：{result}")

    def show_app_modal_dialog(self):
        """
        显示应用程序级模态对话框
        特点：阻塞整个应用程序，用户必须先关闭此对话框才能与应用程序的其他窗口交互
        适用场景：重要的确认、必须处理的警告等
        """
        dialog = CustomDialog("应用程序级模态对话框", self)
        dialog.setWindowModality(Qt.ApplicationModal)  # 设置为应用程序级模态
        dialog.show()

    def show_window_modal_open_dialog(self):
        """
        显示窗口级模态对话框（使用open方法）
        特点：只阻塞与对话框关联的父窗口，用户仍可与应用程序中的其他窗口交互
        适用场景：文档编辑器中的查找替换等操作
        """
        dialog = CustomDialog("窗口级模态对话框 (open)", self)
        # 使用open()方法显示窗口级模态对话框
        dialog.open()

    def show_window_modal_dialog(self):
        """
        显示窗口级模态对话框（使用setWindowModality）
        特点：只阻塞与对话框关联的父窗口，用户仍可与应用程序中的其他窗口交互
        适用场景：需要用户在继续操作父窗口之前完成的任务
        """
        dialog = CustomDialog("窗口级模态对话框 (setWindowModality)", self)
        # 设置为窗口级模态
        dialog.setWindowModality(Qt.WindowModal)  # 设置为窗口级模态
        # 显示对话框
        dialog.show()

    def show_non_modal_dialog(self):
        """
        显示非模态对话框
        特点：不会阻塞任何窗口，用户可以同时与对话框和应用程序的其他部分交互
        适用场景：进度指示器、辅助信息窗口等
        """
        dialog = CustomDialog("非模态对话框", self)
        # 使用show()方法显示非模态对话框
        dialog.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_dialog = DialogTest()
    my_dialog.show()
    sys.exit(app.exec())
