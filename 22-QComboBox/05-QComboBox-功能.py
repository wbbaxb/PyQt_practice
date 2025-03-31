import sys

from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QPushButton, QCompleter
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, QTimer


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QComboBox-功能")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        cbb = QComboBox(self)
        cbb.move(100, 100)
        cbb.resize(150, 30)
        cbb.addItems(["bill", "123", "abc"])
        # 添加图标
        cbb.addItem(QIcon("./Icons/android_96px_1.ico"), "android")

        btn = QPushButton("测试按钮", self)
        btn.move(300, 200)

        # -------可编辑---------
        cbb.setEditable(True)
        # print(cbb.isEditable())

        # -------可重复-------
        cbb.setDuplicatesEnabled(True)  # 允许Text完全相同的选项
        cbb.addItems(["bill", "123", "abc"])
        # print(cbb.duplicatesEnabled())

        cbb.setIconSize(QSize(60, 60))

        # ------尺寸调整策略------
        """
        QComboBox.SizeAdjustPolicy:
        
        QComboBox.AdjustToContents  组合框将始终根据内容进行调整
        QComboBox.AdjustToContentsOnFirstShow  组合框将在第一次显示时调整其内容
        QComboBox.AdjustToMinimumContentsLength  不建议使用
        QComboBox.AdjustToMinimumContentsLengthWithIcon  出于性能原因，请在大型模型上使用此策略
        """

        cbb.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        # print(cbb.sizePolicy())

        # -------清空---------
        # btn.clicked.connect(cbb.clear)  # 清空条目内容
        # btn.clicked.connect(cbb.clearEditText)  # 仅删除编辑内容，不删除条目

        def show_popup():
            """
            显示2秒后隐藏
            """

            cbb.showPopup()

            QTimer.singleShot(2000, lambda: cbb.hidePopup())

        # ------弹出---------
        btn.clicked.connect(show_popup)

        # -------完成器------
        cbb.setCompleter(QCompleter(["abc", "123", "bill"]))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
