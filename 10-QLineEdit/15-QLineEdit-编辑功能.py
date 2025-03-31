import sys

from PyQt5.QtWidgets import (QApplication, QWidget, QLineEdit, QPushButton, 
                            QVBoxLayout, QHBoxLayout, QGridLayout, QLabel)

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("QLineEdit-编辑功能")
window.resize(500, 500)
window.move(400, 250)

# 创建主布局
main_layout = QVBoxLayout()

# 创建文本编辑区域和说明布局
edit_layout = QGridLayout()

# 添加第一个文本框
label1 = QLabel("文本框1 (可拖拽):")
le = QLineEdit()
le.setDragEnabled(True)  # 设置为可以拖拽
edit_layout.addWidget(label1, 0, 0)
edit_layout.addWidget(le, 0, 1)

# 添加第二个文本框
label2 = QLabel("文本框2 (不可拖拽):")
le2 = QLineEdit()
le2.setDragEnabled(False)  # 不能将le2中的文本拖拽到le中
edit_layout.addWidget(label2, 1, 0)
edit_layout.addWidget(le2, 1, 1)

message = QLabel()
edit_layout.addWidget(message, 2, 0, 1, 2) # 2,0 表示从第2行第0列开始，1,2 表示占据1行2列

# 将编辑区布局添加到主布局
main_layout.addLayout(edit_layout)

# 创建按钮区域布局
button_layout = QGridLayout()

# 添加各种功能按钮
def clear_text():
    le.clear()  # 清空

def copy_text():
    le.selectAll() # 需要先选中所有文本，才能复制
    le.copy()  # 复制选中的文本

def cut_text():
    le.selectAll() # 需要先选中所有文本，才能剪切
    le.cut()  # 剪切选中的文本

def paste_text():
    le.paste()  # 粘贴

def undo_text():
    le.undo()  # 撤销

def redo_text():
    le.redo()  # 重做

def backspace_text():
    le.backspace()  # 退格

def del_text():
    le.del_()  # 删除

def select_all_text():
    le.selectAll()  # 全选
    text = '是否全选：' + str(le.hasSelectedText()) + '\n'
    text += '选中的文本：' + le.selectedText() + '\n'
    text += '选中的开始位置：' + str(le.selectionStart()) + '\n'
    text += '选中的结束位置：' + str(le.selectionEnd()) + '\n'
    message.setText(text)

# 创建并连接按钮
clear_btn = QPushButton("清空")
clear_btn.clicked.connect(clear_text)
button_layout.addWidget(clear_btn, 0, 0)

copy_btn = QPushButton("复制")
copy_btn.clicked.connect(copy_text)
button_layout.addWidget(copy_btn, 0, 1)

cut_btn = QPushButton("剪切")
cut_btn.clicked.connect(cut_text)
button_layout.addWidget(cut_btn, 0, 2)

paste_btn = QPushButton("粘贴")
paste_btn.clicked.connect(paste_text)
button_layout.addWidget(paste_btn, 1, 0)

undo_btn = QPushButton("撤销")
undo_btn.clicked.connect(undo_text)
button_layout.addWidget(undo_btn, 1, 1)

redo_btn = QPushButton("重做")
redo_btn.clicked.connect(redo_text)
button_layout.addWidget(redo_btn, 1, 2)

backspace_btn = QPushButton("退格")
backspace_btn.clicked.connect(backspace_text)
button_layout.addWidget(backspace_btn, 2, 0)

del_btn = QPushButton("删除")
del_btn.clicked.connect(del_text)
button_layout.addWidget(del_btn, 2, 1)

select_all_btn = QPushButton("全选")
select_all_btn.clicked.connect(select_all_text)
button_layout.addWidget(select_all_btn, 2, 2)

# 将按钮布局添加到主布局
main_layout.addLayout(button_layout)

# 设置窗口的布局
window.setLayout(main_layout)

window.show()

sys.exit(app.exec_())
