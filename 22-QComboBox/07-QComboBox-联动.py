import sys

from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QVBoxLayout


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QComboBox-联动")
        self.resize(500, 500)
        self.move(400, 250)
        self.city_dic = {
            "北京": {"东城": "001", "西城": "002", "朝阳": "003", "丰台": "004"},
            "上海": {"黄埔": "005", "徐汇": "006", "长宁": "007", "静安": "008", "松江": "009"},
            "广东": {"广州": "010", "深圳": "011", "湛江": "012", "佛山": "013"},
        }
        self.setup_ui()

    def setup_ui(self):
        self.pro_combobox = QComboBox(self)  # 省下拉列表
        self.city_combobox = QComboBox(self)  # 城市下拉列表
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        main_layout.addWidget(self.pro_combobox)
        main_layout.addWidget(self.city_combobox)

        self.pro_combobox.currentIndexChanged[str].connect(self.pro_changed)
        self.city_combobox.currentIndexChanged.connect(self.city_index_changed)
        self.load_pros()

        print('city:', self.city_combobox.currentText())  # 东城

    def load_pros(self):
        """
        加载省下拉列表的值
        """
        # for k, v in self.city_dic.items():
        #     self.pro_combobox.addItem(k, v)

        # 调用addItems方法，更方便
        self.pro_combobox.addItems(self.city_dic.keys())

    def pro_changed(self, pro_name):
        """
        当省下拉列表的值发生改变时，更新城市下拉列表的值

        Args:
            pro_name (str): 省的名称
        """
        cities = self.city_dic.get(pro_name)

        if cities:
            # 暂时阻塞信号连接，防止clear时发送信号导致获得None
            self.city_combobox.blockSignals(True)
            self.city_combobox.clear()
            self.city_combobox.blockSignals(False)  # 恢复信号连接
            for k, v in cities.items():
                self.city_combobox.addItem(k, v)

    def city_index_changed(self, index):
        """
        当城市下拉列表的值发生改变时，获取当前选中的城市名称和对应的编号

        Args:
            index (int): 城市下拉列表的索引
        """
        user_data = self.city_combobox.itemData(index)
        print(f"当前选中的城市是：{self.city_combobox.currentText()}, 编号是：{user_data}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
