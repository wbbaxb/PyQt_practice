import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel

# 1. 创建一个应用程序对象
# QApplication是所有QT应用的基类，管理应用程序的资源和事件，是PyQt5的入口
app = QApplication(sys.argv)


# 2.控件的操作
# 创建控件，设置控件（大小，位置，样式……），事件，信号的处理
# 2.1创建控件
# 当我们创建一个控件之后，如果该控件无父控件，则把它作为顶层控件（窗口）
# 系统会自动给窗口添加一些装饰（标题栏），窗口控件具备一些特性（设置标题、图标等）
window = QWidget()  # QWidget是所有UI组件的基类,如果其没有父类,则是一个窗口，如果其有父类,则是一个控件
# 2.2设置控件
window.setWindowTitle("这是一个窗口标题")
window.resize(500, 500)  # 设置窗口大小为500*500
window.move(400, 250)  # 设置窗口位置为(400, 250)，相对于屏幕左上角

# 控件也可以作为一个容器（承载其他控件）
label = QLabel(window)  # window参数表示label的父类是window对象，也就是label将会被添加到window窗口中
label.setText("label里的文字")
label.setStyleSheet("font-size: 20px; color: red;background-color: blue;")
label.move(100, 100)  # 设置标签位置为(100, 100)，相对于窗口左上角
label.show()

# 2.3展示控件
# 刚创建好一个控件之后（该控件无父控件），默认不会展示该控件，只有手动调用show()
window.show()

# 3.应用程序的执行， 进入到消息循环
# 让整个程序开始执行，并且进入到消息循环（无限循环）
# 检测整个程序所接收到的用户的交互信息
sys.exit(app.exec_())
