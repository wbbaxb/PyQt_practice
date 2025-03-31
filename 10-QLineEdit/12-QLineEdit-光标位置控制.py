import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtCore import QPoint

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("QLineEdit-光标位置控制")
window.resize(400, 300)
window.move(400, 250)


def move_cursor_to_end():
    label.end(False)
    label.setFocus()


def move_cursor_to_start():
    label.home(False)
    label.setFocus()


def get_cursor_position():
    message.setText(f"光标位置: {label.cursorPosition()}")
    label.setFocus()


label = QLineEdit('BillTest')
message = QLabel()
message.setFixedHeight(30)

btn_get_position = QPushButton("获取光标位置")
btn_get_position.clicked.connect(get_cursor_position)

btn_move_cursor_to_start = QPushButton("移动光标到行首")
btn_move_cursor_to_start.clicked.connect(move_cursor_to_start)

btn_move_cursor_to_end = QPushButton("移动光标到行尾")
btn_move_cursor_to_end.clicked.connect(move_cursor_to_end)

# 创建父容器
container = QWidget()
container_layout = QVBoxLayout()
container_layout.setSpacing(3)  # 设置父容器内部组件的间距
container.setLayout(container_layout)

# 将组件添加到父容器中
container_layout.addWidget(label)
container_layout.addWidget(message)
container_layout.addWidget(btn_get_position)
container_layout.addWidget(btn_move_cursor_to_start)
container_layout.addWidget(btn_move_cursor_to_end)

# 设置父容器的样式 (你可以根据需要修改)
container.setStyleSheet("""
    QWidget {
        background-color: #f0f0f0; /* 设置背景颜色 */
        border: 1px solid #ccc;      /* 设置边框 */
        border-radius: 3px;           /* 设置圆角 */
        padding: 5px;                /* 设置内边距 */
    }
    QPushButton {
        margin-top: 5px;             /* 设置按钮的上边距 */
    }
""")

main_layout = QVBoxLayout()
window.setLayout(main_layout)

# 将父容器添加到主布局中
main_layout.addWidget(container)

window.show()
sys.exit(app.exec_())
