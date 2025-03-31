import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QCompleter
from PyQt5.Qt import Qt, QCursor
app = QApplication(sys.argv)
window = QWidget()
main_layout = QVBoxLayout()
window.setLayout(main_layout)
window.setWindowTitle("QLineEdit")
window.resize(500, 500)
window.move(400, 250)


def change_password_mode():
    """
    切换密码模式,共有四种模式，默认是Normal
    Normal = 0 # 正常模式
    NoEcho = 1  # Linux模式，输入内容不显示
    Password = 2 # 密码模式，输入内容显示为*
    PasswordEchoOnEdit = 3  # 明文模式，输入内容显示为明文，结束编辑后变密文
    """

    if tb_val.echoMode() == QLineEdit.Normal:
        tb_val.setEchoMode(QLineEdit.Password)
        lb_message.setText("已切换为密码模式")
    elif tb_val.echoMode() == QLineEdit.Password:
        tb_val.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        lb_message.setText("已切换为明文模式")
    elif tb_val.echoMode() == QLineEdit.PasswordEchoOnEdit:
        tb_val.setEchoMode(QLineEdit.NoEcho)
        lb_message.setText("已切换为Linux模式")
    elif tb_val.echoMode() == QLineEdit.NoEcho:
        tb_val.setEchoMode(QLineEdit.Normal)
        lb_message.setText("已切换为正常模式")


def get_text():
    """获取内容（包括密码模式）"""
    # 获取文本,与displayText()的区别在于，如果设置了密码模式，text()会显示密码内容，displayText()会显示****
    text = tb_val.text()
    label_info.setText(text)


def get_display_text():
    """获取显示的内容"""
    text = tb_val.displayText()  # 获取显示的内容，如果设置了密码模式，会显示****
    label_info.setText(text)


tb_val = QLineEdit()
tb_val.setText("bill")
tb_val.setClearButtonEnabled(True)  # 添加清空按钮
tb_val.setPlaceholderText("请输入内容")  # 设置占位符
# tb_val.setReadOnly(True) 

lb_message = QLabel()
lb_message.setAlignment(Qt.AlignCenter)
lb_message.setStyleSheet("font-size: 20px; color: red;")
lb_message.setMaximumHeight(30)

label_insert_text = QLineEdit()
label_insert_text.setPlaceholderText("请输入内容")
label_insert_text.setMaxLength(5)  # 设置最大长度

completer = QCompleter(["bill", "test", "best", "temp"])  # 创建填充器
label_insert_text.setCompleter(completer)  # 设置填充器，当输入内容与列表中的内容匹配时，会自动补全

btn_insert_text = QPushButton("插入内容")
btn_insert_text.pressed.connect(
    lambda: tb_val.insert(label_insert_text.text()))  # 在光标处插入内容


h_layout = QHBoxLayout()
h_layout.addWidget(label_insert_text)
h_layout.addWidget(btn_insert_text)

label_info = QLabel()
label_info.setAlignment(Qt.AlignCenter)
label_info.setStyleSheet("font-size: 20px; color: green;")
label_info.setMaximumHeight(30)

btn_change_mode = QPushButton("切换输入模式")
btn_change_mode.pressed.connect(change_password_mode)

btn_get_text = QPushButton("获取内容")
btn_get_text.pressed.connect(get_text)

btn_get_display_text = QPushButton("获取显示内容")
btn_get_display_text.pressed.connect(get_display_text)


main_layout.addWidget(lb_message)
main_layout.addWidget(tb_val)
main_layout.addLayout(h_layout)
main_layout.addWidget(label_info)

main_layout.addWidget(btn_change_mode)
main_layout.addWidget(btn_get_text)
main_layout.addWidget(btn_get_display_text)

window.show()

sys.exit(app.exec_())
