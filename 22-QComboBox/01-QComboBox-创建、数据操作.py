import sys

from PyQt5.QtWidgets import (QApplication, QWidget, QComboBox, QPushButton, 
                            QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QGroupBox)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QComboBox 演示")
        self.resize(600, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        # 创建主布局
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        
        # 创建说明标签
        title_label = QLabel("QComboBox 操作演示")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 16pt; font-weight: bold; margin-bottom: 10px;")
        main_layout.addWidget(title_label)
        
        # 创建组合框
        self.cbx = QComboBox()
        self.cbx.setMinimumWidth(200)
        
        # 创建操作按钮组
        operations_group = QGroupBox("操作区")
        operations_layout = QGridLayout()
        operations_group.setLayout(operations_layout)
        
        # 添加项按钮
        add_item_btn = QPushButton("添加项")
        add_item_btn.clicked.connect(self.add_items)
        operations_layout.addWidget(add_item_btn, 0, 0)
        
        # 插入项按钮
        insert_item_btn = QPushButton("插入项")
        insert_item_btn.clicked.connect(self.insert_items)
        operations_layout.addWidget(insert_item_btn, 0, 1)
        
        # 设置项属性按钮
        set_item_btn = QPushButton("设置项属性")
        set_item_btn.clicked.connect(self.set_item_properties)
        operations_layout.addWidget(set_item_btn, 0, 2)
        
        # 删除项按钮
        remove_item_btn = QPushButton("删除项")
        remove_item_btn.clicked.connect(self.remove_item)
        operations_layout.addWidget(remove_item_btn, 1, 0)
        
        # 插入分隔线按钮
        insert_separator_btn = QPushButton("插入分隔线")
        insert_separator_btn.clicked.connect(self.insert_separator)
        operations_layout.addWidget(insert_separator_btn, 1, 1)
        
        # 设置当前项按钮
        set_current_btn = QPushButton("设置选中项")
        set_current_btn.clicked.connect(self.set_current_item)
        operations_layout.addWidget(set_current_btn, 1, 2)
        
        # 切换可编辑按钮
        toggle_editable_btn = QPushButton("切换可编辑")
        toggle_editable_btn.clicked.connect(self.toggle_editable)
        operations_layout.addWidget(toggle_editable_btn, 2, 0)
        
        # 清空下拉框按钮
        clear_btn = QPushButton("清空下拉框")
        clear_btn.clicked.connect(self.clear_combobox)
        operations_layout.addWidget(clear_btn, 2, 1)
        
        # 显示状态区域
        status_group = QGroupBox("状态区")
        status_layout = QVBoxLayout()
        status_group.setLayout(status_layout)
        
        # 当前选择的显示标签
        self.status_label = QLabel("当前未选择任何项")
        status_layout.addWidget(self.status_label)
        
        # 组合框与状态显示区域布局
        combo_status_layout = QHBoxLayout()
        combo_status_layout.addWidget(self.cbx)
        combo_status_layout.addWidget(status_group)
        
        # 将组合框和操作区添加到主布局
        main_layout.addLayout(combo_status_layout)
        main_layout.addWidget(operations_group)
        
        # 连接信号到槽
        self.cbx.currentTextChanged.connect(self.on_selection_changed)
        
        # 设置样式
        self.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 1px solid #999;
                border-radius: 5px;
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px;
            }
            QPushButton {
                min-height: 30px;
                background-color: #f0f0f0;
                border: 1px solid #999;
                border-radius: 3px;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
            }
            QComboBox {
                min-height: 30px;
                padding: 5px;
                border: 1px solid #999;
                border-radius: 3px;
            }
        """)
        
    def add_items(self):
        self.cbx.addItem(QIcon("./Icons/audio_mid_48px.ico"), "选项1")
        self.cbx.addItem(QIcon("./Icons/audio_mute_48px.ico"), "选项2")
        self.cbx.addItems([f"数字{x}" for x in range(3)])
    
    def insert_items(self):
        self.cbx.insertItems(1, ("插入项A", "插入项B", "插入项C"))
    
    def set_item_properties(self):
        if self.cbx.count() > 2:
            self.cbx.setItemIcon(2, QIcon("./Icons/audio_low_48px.ico"))
            self.cbx.setItemText(2, "修改后的文字")
    
    def remove_item(self):
        if self.cbx.count() > 0:
            self.cbx.removeItem(self.cbx.count() - 1)
    
    def insert_separator(self):
        if self.cbx.count() > 3:
            self.cbx.insertSeparator(3)
    
    def set_current_item(self):
        if self.cbx.count() > 1:
            self.cbx.setCurrentIndex(1) # 设置选中的项为索引为1的项
    
    def toggle_editable(self):
        self.cbx.setEditable(not self.cbx.isEditable())
        if self.cbx.isEditable():
            self.cbx.setEditText("可编辑的文本")
    
    def clear_combobox(self):
        self.cbx.clear()
    
    def on_selection_changed(self, text):
        self.status_label.setText(f"当前选择: {text}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
