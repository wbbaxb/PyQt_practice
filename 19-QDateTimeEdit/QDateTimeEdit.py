import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QDateTimeEdit
from PyQt5.QtCore import QDateTime


class DateTimeExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建布局
        layout = QVBoxLayout()

        # 创建 QDateTimeEdit 控件
        datetime_edit = QDateTimeEdit(self)

        # 设置默认日期和时间（可选）
        datetime_edit.setDateTime(QDateTime.currentDateTime())

        # 设置显示格式
        datetime_edit.setDisplayFormat("yyyy-MM-dd HH:mm:ss")

        # 启用日历下拉选择
        datetime_edit.setCalendarPopup(True)

        datetime_edit.dateTimeChanged.connect(lambda: print("当前选中的时间:", datetime_edit.dateTime().toString("yyyy-MM-dd HH:mm:ss")))

        # 添加到布局
        layout.addWidget(datetime_edit)

        # 设置窗口布局和属性
        self.setLayout(layout)
        self.setWindowTitle('日期时间选择器')
        self.setGeometry(300, 300, 300, 200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DateTimeExample()
    ex.show()
    sys.exit(app.exec_())
