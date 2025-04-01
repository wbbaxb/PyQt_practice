import sys

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QInputDialog")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        top_layout = QVBoxLayout()
        top_widget = QWidget()
        top_widget.setLayout(top_layout)
        buttom_layout = QVBoxLayout()
        buttom_widget = QWidget()
        buttom_widget.setLayout(buttom_layout)

        main_layout.addWidget(top_widget)
        main_layout.addWidget(buttom_widget)

        main_layout.setStretch(0, 1)  # 上部布局拉伸比例
        main_layout.setStretch(1, 10)  # 下部布局拉伸比例

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 20px;height: 30px;")
        top_layout.addWidget(self.label)

        btn_show_get_int = QPushButton("显示整数")
        btn_show_get_int.clicked.connect(self.show_get_int)
        buttom_layout.addWidget(btn_show_get_int)

        btn_show_get_double = QPushButton("显示小数")
        btn_show_get_double.clicked.connect(self.show_get_double)
        buttom_layout.addWidget(btn_show_get_double)

        btn_show_get_text = QPushButton("显示文本")
        btn_show_get_text.clicked.connect(self.show_get_text)
        buttom_layout.addWidget(btn_show_get_text)

        btn_show_get_multi_line_text = QPushButton("显示多行文本")
        btn_show_get_multi_line_text.clicked.connect(
            self.show_get_multi_line_text)
        buttom_layout.addWidget(btn_show_get_multi_line_text)

        btn_show_get_item = QPushButton("显示选择项")
        btn_show_get_item.clicked.connect(self.show_get_item)
        buttom_layout.addWidget(btn_show_get_item)

        btn_show_instance_dialog = QPushButton("显示实例对话框")
        btn_show_instance_dialog.clicked.connect(self.show_instance_dialog)
        buttom_layout.addWidget(btn_show_instance_dialog)

        btn_show_signal_dialog = QPushButton("显示信号对话框")
        btn_show_signal_dialog.clicked.connect(self.show_signal_dialog)
        buttom_layout.addWidget(btn_show_signal_dialog)

    def set_message(self, message):
        if not isinstance(message, tuple):
            self.label.setText('未知结果')
        else:
            self.label.setText(
                f'选择项：{message[0]}，是否选择：{"是" if message[1] else "否"}')

    def show_get_int(self):
        # 返回一个元组，第一个元素是选择项，第二个元素是是否选择
        result = QInputDialog.getInt(
            self,  # 父窗口
            "窗口标题",  # 标题
            "请输入一个整数",  # 提示标签
            666,  # 默认值
        )

        self.set_message(result)

    def show_get_double(self):
        result = QInputDialog.getDouble(
            self,  # 父窗口
            "窗口标题",  # 标题
            "请输入一个小数",  # 提示标签
            66.6,  # 默认值
        )

        self.set_message(result)

    def show_get_text(self):
        result = QInputDialog.getText(
            self,  # 父窗口
            "窗口标题",  # 标题
            "请输入一个文本",  # 提示标签
            text='默认文本',
        )

        self.set_message(result)

    def show_get_multi_line_text(self):
        result = QInputDialog.getMultiLineText(
            self,  # 父窗口
            "窗口标题",  # 标题
            "请输入一个多行文本",  # 提示标签
            "默认文本",  # 默认值
        )

        self.set_message(result)

    def show_get_item(self):
        result = QInputDialog.getItem(
            self,  # 父窗口
            "窗口标题",  # 标题
            "请选择一项",  # 提示标签
            ["1", "2", "3"],  # 选项列表
            2,  # 默认选择项
            True  # 是否可以编辑
        )
        self.set_message(result)

    def show_instance_dialog(self):
        """
        通过实例化QInputDialog来创建对话框

        -------设置选项-----------
        # input_d.setOptions(QInputDialog.UseListViewForComboBoxItems)

        QInputDialog.InputDialogOption:

        QInputDialog.NoButtons  不显示“确定”和“取消”按钮（对“实时对话框”有用）
        QInputDialog。UseListViewForComboBoxItems  用QListView而不是不可编辑的QComboBox来显示使用setComboBoxItems
        QInputDialog。UsePlainTextEditForTextInput  使用QPlainTextEdit进行多行文本输入
        # print(input_d.options())

        # -------输入模式---------
        input_d.setInputMode(QInputDialog.TextInput)

                QInputDialog.InputMode:

        QInputDialog.TextInput
        QInputDialog.IntInput
        QInputDialog.DoubleInput

        # -------各个小分类详细设置--------
        InputMode  整型
            setIntMaximum(int)
            setIntMinimum(int)
            setIntRange(int, int)
            setIntStep(int)
            setIntValue(int)

        Double  浮点型
            setDoubleMaximum(float)
            setDoubleDecimals(int)
            setDoubleMinimum(float)
            setDoubleRange(float, float)
            setDoubleStep(float)
            setDoubleValue(float)

        Text  字符串
            setTextEchoMode(QLineEdit.EchoMode)
            setTextValue(str)

        ComboBox  下拉列表
            setComboBoxItems(Iterable[str])
            setComboBoxEditable(bool)
        """

        dialog = QInputDialog(self)
        dialog.setWindowTitle("实例对话框2")
        dialog.setLabelText("请输入一个文本2")
        dialog.setOkButtonText("确定2")
        dialog.setCancelButtonText("取消2")

        dialog.setOptions(QInputDialog.UseListViewForComboBoxItems)  # 设置选项

        # 设置输入模式
        dialog.setInputMode(QInputDialog.TextInput)  # 设置输入模式

        dialog.textValueSelected.connect(lambda val: print("最终输入值：", val))
        dialog.exec_()

        # 获取输入的文本，这样不对，因为个如果点击了取消，也会获取到文本，应该用信号
        # print(dialog.textValue())

    def show_signal_dialog(self):
        dialog = QInputDialog(self)
        dialog.setInputMode(QInputDialog.IntInput)
        dialog.setLabelText("请输入一个整数")
        dialog.setOkButtonText("确定")
        dialog.setCancelButtonText("取消")
        dialog.intValueChanged.connect(lambda val: print("数值发生了改变", val))
        dialog.intValueSelected.connect(lambda val: print("最终选择了", val))
        dialog.setWindowFlags(dialog.windowFlags() | Qt.MSWindowsFixedSizeDialogHint)  # 确保固定大小（Windows特有）
        dialog.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
