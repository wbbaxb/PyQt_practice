import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QGroupBox, QLabel, QGridLayout
)
from PyQt5.QtCore import Qt

"""
QLineEdit 的信号

信号	                         说明	                               备注
textEdited(str text)	文本内容被编辑时发送此信号	只有用户的操作才视为编辑，使用代码设置文本内容则不发送此信号
textChanged(str text)	文本内容改变时发送此信号	使用代码改变文本也发送此信号
selectionChanged()	用户选择变化时发送此信号	光标按下并有移动即触发，不是选中范围改变才触发
cursorPositionChanged(int oldPos, int newPos)	当光标移动时发射此信号，传出旧新光标位置	pos为光标竖线右侧字符的位置数，从0开始
editingFinished()	用户结束编辑时发送此信号	当QLineEdit失去焦点时则认为是结束编辑
inputRejected()	输入被拒绝时发送此信号	用户输入不符合验证器或长度超过限制时发送此信号
returnPressed()	按下Enter键发送的信号	当设置了验证器或掩码时，只有验证器掩码通过后才发送此信号
"""

class LineEditSignalDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # 设置窗口
        self.setWindowTitle("QLineEdit信号演示")
        self.resize(600, 400)
        self.move(400, 250)
        
        # 创建主布局
        main_layout = QVBoxLayout()
        
        # 创建说明标签
        title_label = QLabel("QLineEdit信号演示")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 16pt; font-weight: bold; margin: 10px;")
        main_layout.addWidget(title_label)
        
        # 创建文本输入框和显示区域
        input_group = QGroupBox("文本输入")
        input_layout = QVBoxLayout()
        
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("请在此输入文本...")
        self.status_label = QLabel("状态信息显示区域")
        self.status_label.setStyleSheet("background-color: #f0f0f0; padding: 5px; min-height: 50px;")
        
        input_layout.addWidget(QLabel("文本框:"))
        input_layout.addWidget(self.line_edit)
        input_layout.addWidget(QLabel("状态:"))
        input_layout.addWidget(self.status_label)
        input_group.setLayout(input_layout)
        main_layout.addWidget(input_group)
        
        # 创建按钮区域
        button_group = QGroupBox("信号演示按钮")
        button_layout = QGridLayout()
        
        # 创建各种演示按钮
        self.create_demo_buttons(button_layout)
        
        button_group.setLayout(button_layout)
        main_layout.addWidget(button_group)
        
        # 连接信号
        self.connect_signals()
        
        # 设置布局
        self.setLayout(main_layout)
    
    def create_demo_buttons(self, layout):
        # 第一行按钮
        self.btn_set_text = QPushButton("设置文本(触发textChanged)")
        self.btn_clear = QPushButton("清空文本")
        layout.addWidget(self.btn_set_text, 0, 0)
        layout.addWidget(self.btn_clear, 0, 1)
        
        # 第二行按钮
        self.btn_select_all = QPushButton("全选文本(触发selectionChanged)")
        self.btn_move_cursor = QPushButton("移动光标(触发cursorPositionChanged)")
        layout.addWidget(self.btn_select_all, 1, 0)
        layout.addWidget(self.btn_move_cursor, 1, 1)
        
        # 第三行说明
        signal_label = QLabel("其他信号演示：\n- 编辑文本框内容将触发textEdited和textChanged\n- 按Enter键将触发returnPressed\n- 点击其他地方将触发editingFinished")
        signal_label.setStyleSheet("background-color: #e0e0e0; padding: 5px;")
        layout.addWidget(signal_label, 2, 0, 1, 2)
    
    def connect_signals(self):
        # 按钮连接
        self.btn_set_text.clicked.connect(lambda: self.line_edit.setText("这是通过代码设置的文本"))
        self.btn_clear.clicked.connect(self.line_edit.clear)
        self.btn_select_all.clicked.connect(self.line_edit.selectAll)
        self.btn_move_cursor.clicked.connect(lambda: self.line_edit.setCursorPosition(0))
        
        # QLineEdit信号连接
        self.line_edit.textEdited.connect(lambda text: self.update_status(f"textEdited信号: '{text}'"))

        self.line_edit.textChanged.connect(lambda text: self.update_status(f"textChanged信号: '{text}'"))

        self.line_edit.selectionChanged.connect(
            lambda: self.update_status(f"selectionChanged信号: 选中'{self.line_edit.selectedText()}'")
        )

        self.line_edit.cursorPositionChanged.connect(
            lambda old, new: self.update_status(f"cursorPositionChanged信号: {old} -> {new}")
        )

        self.line_edit.editingFinished.connect(
            lambda: self.update_status("editingFinished信号: 编辑结束")
        )
        
        self.line_edit.returnPressed.connect(
            lambda: self.update_status("returnPressed信号: 回车键被按下")
        )
    
    def update_status(self, message):
        current_text = self.status_label.text()
        # 保留最近5条信息
        lines = current_text.split("\n")
        if len(lines) >= 5:
            lines.pop(0)
        current_text = "\n".join(lines)
        self.status_label.setText(f"{current_text}\n{message}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = LineEditSignalDemo()
    demo.show()
    sys.exit(app.exec_())
