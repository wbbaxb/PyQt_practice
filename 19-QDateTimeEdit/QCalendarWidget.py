import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCalendarWidget
from PyQt5.QtCore import QDate

class CalendarExample(QWidget):
    """
    只显示日期选择器，不显示时间
    """
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建布局
        layout = QVBoxLayout()

        # 创建 QCalendarWidget 控件
        calendar = QCalendarWidget(self)
        
        # 设置默认日期（可选）
        calendar.setSelectedDate(QDate.currentDate())

        # 连接信号到槽函数（获取用户选择的日期）
        calendar.selectionChanged.connect(self.on_date_changed)

        # 添加到布局
        layout.addWidget(calendar)

        # 设置窗口布局和属性
        self.setLayout(layout)
        self.setWindowTitle('日历选择器')
        self.setGeometry(300, 300, 400, 300)

    def on_date_changed(self):
        selected_date = self.sender().selectedDate()
        print(f"选择的日期是: {selected_date.toString('yyyy-MM-dd')}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CalendarExample()
    ex.show()
    sys.exit(app.exec_())