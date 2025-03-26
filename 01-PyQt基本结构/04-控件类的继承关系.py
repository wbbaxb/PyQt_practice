from PyQt5.QtWidgets import QAbstractButton, QDialog


def get_sub_classes(class_):
    """递归的显示某一对象的所有子对象"""
    for subclass in class_.__subclasses__():
        print(subclass)
        if len(class_.__subclasses__()) > 0:
            get_sub_classes(subclass)


get_sub_classes(QAbstractButton) # 打印出QAbstractButton的所有子类
# 打印结果：
# <class 'PyQt5.QtWidgets.QPushButton'> # 按钮类
# <class 'PyQt5.QtWidgets.QRadioButton'> # 单选按钮类
# <class 'PyQt5.QtWidgets.QCheckBox'> # 复选框类
# <class 'PyQt5.QtWidgets.QToolButton'> # 工具按钮类
# <class 'PyQt5.QtWidgets.QCommandLinkButton'> # 命令链接按钮类

print("*"*100)

get_sub_classes(QDialog) # 打印出QDialog的所有子类
# 打印结果：
# <class 'PyQt5.QtWidgets.QColorDialog'> # 颜色对话框类
# <class 'PyQt5.QtWidgets.QErrorMessage'> # 错误消息对话框类
# <class 'PyQt5.QtWidgets.QFileDialog'> # 文件对话框类
# <class 'PyQt5.QtWidgets.QFontDialog'> # 字体对话框类
# <class 'PyQt5.QtWidgets.QInputDialog'> # 输入对话框类
# <class 'PyQt5.QtWidgets.QMessageBox'> # 消息对话框类
# <class 'PyQt5.QtWidgets.QProgressDialog'> # 进度对话框类
# <class 'PyQt5.QtWidgets.QWizard'> # 向导对话框类




