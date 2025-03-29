import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.Qt import QObject


"""
关于PyQt信号(Signal)与槽(Slot)机制，后面还有一个43-pyqtSignal目录讲解
可以在学习各种控件的过程中逐渐体会信号与槽的连接、传参等等
一个信号可以连接多个槽，类似于C#中一个事件可以绑定多个方法
一个槽也可以被多个信号连接，类似于C#中一个方法可以被多个事件绑定
"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("信号与槽演示")
        self.resize(800, 600)
        self.move(400, 250)
        
        # 应用样式表
        self.load_stylesheet()
        
        # 创建一个测试对象
        self.test_obj = QObject()
        
        # 设置界面
        self.setup_ui()
        
    def load_stylesheet(self):
        """加载外部样式表"""
        try:
            with open("02-QObject/style.qss", "r", encoding="utf-8") as f:
                style = f.read()
                self.setStyleSheet(style) # 设置样式表（应用于当前窗口）
        except:
            print("样式表加载失败")
        
    def setup_ui(self):
        # 创建主布局
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        
        # 创建状态标签
        self.status_label = QLabel("状态信息显示区域")
        main_layout.addWidget(self.status_label)
        
        # 创建用于对象名称更改的按钮
        self.name_btn = QPushButton("更改对象名称")
        self.name_btn.setObjectName("name_btn") # 设置按钮的名称,用于样式表选择
        self.name_btn.clicked.connect(self.change_object_name)
        main_layout.addWidget(self.name_btn)
        
        # 创建用于连接信号的按钮
        self.connect_btn = QPushButton("连接信号")
        self.connect_btn.setObjectName("connect_btn") # 设置按钮的名称,用于样式表选择
        self.connect_btn.clicked.connect(self.connect_signal)
        main_layout.addWidget(self.connect_btn)
        
        # 创建用于断开信号的按钮
        self.disconnect_btn = QPushButton("断开信号")
        self.disconnect_btn.setObjectName("disconnect_btn") # 设置按钮的名称,用于样式表选择
        self.disconnect_btn.clicked.connect(self.disconnect_signal)
        main_layout.addWidget(self.disconnect_btn)
        
        # 创建用于阻断信号的按钮
        self.block_btn = QPushButton("阻断信号")
        self.block_btn.setObjectName("block_btn") # 设置按钮的名称,用于样式表选择
        self.block_btn.clicked.connect(self.block_signal)
        main_layout.addWidget(self.block_btn)
        
        # 创建用于恢复信号的按钮
        self.unblock_btn = QPushButton("恢复信号")
        self.unblock_btn.setObjectName("unblock_btn") # 设置按钮的名称,用于样式表选择
        self.unblock_btn.clicked.connect(self.unblock_signal)
        main_layout.addWidget(self.unblock_btn)
        
        # 创建用于释放对象的按钮
        self.destroy_btn = QPushButton("释放对象")
        self.destroy_btn.setObjectName("destroy_btn") # 设置按钮的名称,用于样式表选择
        self.destroy_btn.clicked.connect(self.destroy_object)
        main_layout.addWidget(self.destroy_btn)
        
        # 初始连接信号
        self.signal_connected = False
        self.update_status()
        
    def update_status(self):
        """更新状态信息"""
        status_text = f"对象名称: {self.test_obj.objectName()}\n"
        status_text += f"信号连接状态: {'已连接' if self.signal_connected else '未连接'}\n"
        status_text += f"信号阻断状态: {'已阻断' if self.test_obj.signalsBlocked() else '未阻断'}\n"
        
        if self.signal_connected:
            status_text += f"连接的槽数量: {self.test_obj.receivers(self.test_obj.objectNameChanged)}"
            
        self.status_label.setText(status_text)
        
    def name_changed_slot(self, name):
        """对象名称变化时的槽函数"""
        print(f"对象名称发生了改变: {name}")
        self.update_status()
        
    def connect_signal(self):
        """连接信号与槽"""
        if not self.signal_connected:
            self.test_obj.objectNameChanged.connect(self.name_changed_slot)
            self.signal_connected = True
            self.update_status()
            
    def disconnect_signal(self):
        """断开信号与槽"""
        if self.signal_connected:
            self.test_obj.objectNameChanged.disconnect(self.name_changed_slot)
            self.signal_connected = False
            self.update_status()
            
    def change_object_name(self):
        """改变对象名称，触发信号"""
        current_name = self.test_obj.objectName() # 获取对象的名称
        if not current_name or current_name == "测试对象C":
            new_name = "测试对象A"
        elif current_name == "测试对象A":
            new_name = "测试对象B"
        else:
            new_name = "测试对象C"
            
        self.test_obj.setObjectName(new_name)
        self.update_status()
        
    def block_signal(self):
        """阻断信号"""
        self.test_obj.blockSignals(True) # 阻断信号,阻止信号的传递，直到恢复信号
        self.update_status()
        
    def unblock_signal(self):
        """恢复信号"""
        self.test_obj.blockSignals(False) # 恢复信号,允许信号的传递
        self.update_status()
        
    def destroy_object(self):
        """释放对象，触发destroyed信号"""
        def destroy_slot(obj):
            print(f"对象被释放了: {obj}")
            
        # 创建一个新对象并连接其destroyed信号
        temp_obj = QObject()
        temp_obj.setObjectName("即将被释放的对象")
        temp_obj.destroyed.connect(destroy_slot)
        
        # 释放该对象
        temp_obj.deleteLater()
        self.status_label.setText("对象已释放，请查看控制台输出")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
