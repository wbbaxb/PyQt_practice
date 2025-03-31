import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel, QHBoxLayout
from PyQt5.QtGui import QValidator, QIntValidator
from PyQt5.Qt import Qt

"""
单行文本编辑器可以设置验证器（Validator），比如限制只能输入一定范围内的数字等，设置验证器后，
只有满足验证器要求的字符才能被输入，否则用户输入不会显示在编辑器内
"""


class MyValidator(QValidator):
    """
    自定义验证器，重写 validate 和 fixup 方法。

    - validate: 实时验证输入的有效性，返回 Acceptable、Intermediate 或 Invalid 状态。
    - fixup: 输入完成后（比如失去焦点）修复不符合要求的值，确保最终输入符合预期。
    """

    def __init__(self, min: int, max: int):
        super().__init__()
        self.min = min
        self.max = max

    def validate(self, input_str: str, pos_int: int):
        """
        验证器类必须实现validate方法，用于验证输入的字符串是否满足要求
        input_str: 输入的字符串
        pos_int: 当前光标的位置
        """
        try:
            if self.min <= int(input_str) <= self.max:
                return QValidator.Acceptable, input_str, pos_int  # 返回Acceptable表示输入的字符串满足要求
            elif 1 <= int(input_str) <= self.min - 1:
                # 返回Intermediate表示输入的字符串不满足要求，但可以继续输入
                return QValidator.Intermediate, input_str, pos_int
            else:
                return QValidator.Invalid, input_str, pos_int  # 返回Invalid表示输入的字符串不满足要求，无法继续输入
        except Exception:
            # 如果用户还没有输入，输入字符为空
            if not input_str:
                # 返回Intermediate表示输入的字符串不满足要求，但可以继续输入
                return QValidator.Intermediate, input_str, pos_int
            return QValidator.Invalid, input_str, pos_int  # 返回Invalid表示输入的字符串不满足要求，无法继续输入

    def fixup(self, p_str: str) -> str:
        """
        如果用户输入不满足要求，最后还会调用fixup方法修复
        p_str: 输入的字符串
        """
        try:
            if int(p_str) < self.min:
                return str(self.min)
            elif int(p_str) > self.max:
                return str(self.max)
        except Exception:
            return str(self.min)


class MyIntValidator(QIntValidator):
    """
    继承QIntValidator类,更简单地实现年龄验证器
    """

    def __init__(self, min: int, max: int):
        super().__init__(min, max)
        self.min = min
        self.max = max

    def fixup(self, input: str) -> str:
        """
        需要重写fixup方法,当用户输入不满足要求时，会调用fixup方法修复
        """
        if len(input) == 0 or int(input) < self.min:
            return str(self.min)
        elif int(input) > self.max:
            return str(self.max)
        return input


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLineEdit-验证器的使用")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        top_layout = QHBoxLayout()
        bottom_layout = QHBoxLayout()
        main_layout.addLayout(top_layout)
        main_layout.addLayout(bottom_layout)

        text_box = QLineEdit()
        text_box.setFixedWidth(100)
        text_box.setStyleSheet("font-size: 20px;")
        text_box.setContentsMargins(0, 100, 0, 100)
        my_validator = MyValidator(30, 70)  # 使用自定义的QValidator
        text_box.setValidator(my_validator)  # 调用QWidget的setValidator方法设置验证器

        message = QLabel()
        message.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)  # 设置水平居左，垂直居中
        message.setStyleSheet("font-size: 20px; color: red;")

        btn = QPushButton("获取内容")
        btn.setFixedHeight(30)
        btn.clicked.connect(lambda: message.setText(text_box.text()))

        text_box2 = QLineEdit()
        text_box2.setFixedWidth(100)
        text_box2.setStyleSheet("font-size: 20px;")
        text_box2.setContentsMargins(0, 100, 0, 100)
        my_int_validator = MyIntValidator(20, 80)  # 使用自定义的QIntValidator
        # 调用QWidget的setValidator方法设置验证器
        text_box2.setValidator(my_int_validator)

        message2 = QLabel()
        message2.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)  # 设置水平居左，垂直居中
        message2.setStyleSheet("font-size: 20px; color: red;")

        btn2 = QPushButton("获取内容")
        btn2.setFixedHeight(30)
        btn2.clicked.connect(lambda: message2.setText(text_box2.text()))

        top_layout.addWidget(text_box)
        top_layout.addWidget(btn)
        top_layout.addWidget(message)

        bottom_layout.addWidget(text_box2)
        bottom_layout.addWidget(btn2)
        bottom_layout.addWidget(message2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
