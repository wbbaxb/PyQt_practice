import sys

from PyQt5.QtWidgets import QWidget, QMessageBox, QCheckBox, QApplication, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

"""
QMessageBox.Icon
QMessageBox.NoIcon
QMessageBox.Question
QMessageBox.Information
QMessageBox.Warning
QMessageBox.Critical

QMessageBox.ButtonRole
QMessageBox.InvalidRole  该按钮无效
QMessageBox.AcceptRole  单击该按钮将使对话框被接受（例如，确定）
QMessageBox.RejectRole  单击该按钮会导致拒绝对话框（例如取消）
QMessageBox.DestructiveRole  单击该按钮会导致破坏性更改（例如，对于 Discarding Change
QMessageBox.ActionRole  单击该按钮将导致更改对话框中的元素
QMessageBox.HelpRole  可以单击该按钮以请求帮助
QMessageBox.YesRole  按钮是一个“是”按钮
QMessageBox.NoRole  按钮是一个“否”按钮
QMessageBox.ApplyRole  该按钮应用当前更改
QMessageBox.ResetRole  该按钮将对话框的字段重置为默认值

QMessageBox.StandardButton
QMessageBox.Ok 使用AcceptRole定义的“确定”按钮
QMessageBox.Open 使用AcceptRole定义的“打开”按钮
QMessageBox.Save 使用AcceptRole定义的“保存”按钮
QMessageBox.Cancel 使用AcceptRole定义的“取消”按钮
QMessageBox.Close 使用AcceptRole定义的“关闭”按钮
QMessageBox.Discard “丢弃”或“不保存”按钮，具体取决于使用DestructiveRole定义的平台
QMessageBox.Apply 使用ApplyRole定义的“应用”按钮
QMessageBox.Reset 使用ResetRole定义的“重置”按钮
QMessageBox.RestoreDefaults 使用ResetRole定义的“恢复默认值”按钮
QMessageBox.Help 使用HelpRole定义的“帮助”按钮
QMessageBox.SaveAll 使用AcceptRole定义的“全部保存”按钮
QMessageBox.Yes 使用YesRole定义的“是”按钮
QMessageBox.YesToAll 使用YesRole定义的“Yes to All” 按钮
QMessageBox.No  使用NoRole定义的“否”按钮
QMessageBox.NoToAll  使用NoRole定义的“No to All”按钮
QMessageBox.Abort  使用RejectRole定义的”中止“按钮
QMessageBox.Retry  使用AcceptRole定义的”重试“按钮
QMessageBox.Ignore  使用AcceptRole定义的”忽略“按钮
"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMessageBox")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        self.setStyleSheet("background-color: white;QPushButton{margin: 20px;height: 30px;}")

        btn_show_message_box = QPushButton("显示消息提示框")
        main_layout.addWidget(btn_show_message_box)
        btn_show_message_box.clicked.connect(self.show_message_box)

        btn_show_custom_message_box = QPushButton("显示自定义消息提示框")
        main_layout.addWidget(btn_show_custom_message_box)
        btn_show_custom_message_box.clicked.connect(
            self.show_custom_message_box)

    def show_message_box(self):
        message_box = QMessageBox(self)
        # message_box = QMessageBox(QMessageBox.Critical, '窗口标题', '主标题', QMessageBox.Ok | QMessageBox.Discard, self)
        # message_box.setModal(False)  # 强行设置为非模态
        # message_box.setWindowModality(Qt.NonModal)  # 强行设置为非模态
        # message_box.show()  # 一定为模态，即使使用show()方法也仍为模态

        message_box.setWindowTitle("消息提示")

        # 设置图标
        # message_box.setIcon(QMessageBox.Information)  # 设置标准图标
        message_box.setIconPixmap(
            QPixmap("./Icons/python_96px.ico").scaled(40, 40))  # 设置自定义图标

        # 设置主标题
        message_box.setText("<h3>这是主标题</h3>")  # 设置主标题
        # message_box.setTextFormat(Qt.PlainText)  # 设置主标题文本格式
        # message_box.setTextFormat(Qt.RichText)
        message_box.setTextFormat(Qt.AutoText)

        # 设置提示文本（副标题）
        message_box.setInformativeText("这是副标题")  # 设置副标题
        # print(message_box.informativeText())

        # 设置详细文本
        message_box.setDetailedText("这是详细文本")  # 设置详情（不支持富文本）
        # print(message_box.detailedText())

        # 设置复选框
        message_box.setCheckBox(QCheckBox("下次不再提醒", message_box))  # 设置复选框
        message_box.checkBox().toggled.connect(lambda: print("复选框被点击了"))

        message_box.open()

    def show_custom_message_box(self):
        message_box = QMessageBox(self)
        message_box.setWindowTitle("消息提示")

        yes_btn = message_box.addButton("Yes!Yes!Yes!", QMessageBox.YesRole)

        # 设置标准按钮
        message_box.setStandardButtons(
            QMessageBox.Apply | QMessageBox.No | QMessageBox.Cancel)

        # 默认按钮(默认哪个按钮获取到焦点）
        message_box.setDefaultButton(QMessageBox.Apply)

        # 退出按钮（按下键盘Esc键时激活的按钮）
        message_box.setEscapeButton(QMessageBox.No)

        # 按钮信号槽
        apply_btn = message_box.button(QMessageBox.Apply)  # 获取按钮对象

        def btn_clicked(btn):
            if btn == yes_btn:
                print("点击了yes按钮")
            elif btn == apply_btn:
                print("点击了apply按钮")

            role = message_box.buttonRole(btn)

            if role == QMessageBox.YesRole:
                print("点击了Yes按钮")
            elif role == QMessageBox.NoRole:
                print("点击了No按钮")

        message_box.buttonClicked.connect(btn_clicked)

        message_box.open()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
