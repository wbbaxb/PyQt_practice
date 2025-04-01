import sys

from PyQt5.QtWidgets import QWidget, QApplication, QSlider, QLabel, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QAbstractSlider")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        top_layout = QVBoxLayout()
        buttom_layout = QVBoxLayout()

        main_layout.addLayout(top_layout)
        main_layout.addLayout(buttom_layout)

        # 设置伸缩因子，使两个布局各占一半
        main_layout.setStretch(0, 1)  # top_layout 占 1
        main_layout.setStretch(1, 1)  # buttom_layout 占 1

        # 设置按钮和标签的样式
        self.setStyleSheet(
            "QPushButton{font-size: 12px;color: green;}QLabel{font-size: 20px;color: red;}")

        label = QLabel()
        label.setText("0")
        label.setAlignment(Qt.AlignCenter)
        sd = QSlider()
        sd.setTickPosition(QSlider.TicksBothSides)  # 设置刻度位置
        sd.setCursor(Qt.PointingHandCursor)
        sd.valueChanged.connect(lambda val: label.setText(str(val)))

        top_layout.addWidget(label)

        slider_layout = QHBoxLayout()
        slider_layout.addWidget(sd)

        # 将水平布局添加到上部布局中
        top_layout.addLayout(slider_layout)

        btn_set_range = QPushButton("设置范围")
        btn_set_range.clicked.connect(lambda: sd.setRange(50, 100))
        buttom_layout.addWidget(btn_set_range)

        btn_set_value = QPushButton("设置数值为20")
        # 当设置的数值小于最小值时，会自动设置为最小值，即50
        btn_set_value.clicked.connect(lambda: sd.setValue(20))
        buttom_layout.addWidget(btn_set_value)

        btn_set_single_step = QPushButton("设置单步长为2")
        btn_set_single_step.clicked.connect(lambda: sd.setSingleStep(2))
        buttom_layout.addWidget(btn_set_single_step)

        btn_set_page_step = QPushButton("设置页步长为5")
        btn_set_page_step.clicked.connect(lambda: sd.setPageStep(5))
        buttom_layout.addWidget(btn_set_page_step)

        def set_tracking():
            sd.setTracking(not sd.hasTracking())
            print(f'是否追踪: {sd.hasTracking()}')

        btn_set_tracking = QPushButton("切换追踪")
        btn_set_tracking.clicked.connect(set_tracking)
        buttom_layout.addWidget(btn_set_tracking)

        def set_orientation():
            if sd.orientation() == Qt.Horizontal:
                sd.setOrientation(Qt.Vertical)
            else:
                sd.setOrientation(Qt.Horizontal)

        btn_set_orientation = QPushButton("切换方向")
        btn_set_orientation.clicked.connect(set_orientation)
        buttom_layout.addWidget(btn_set_orientation)

        btn_set_inverted_appearance = QPushButton("设置倒立外观")
        # 设置倒立外观，往下为增加，往上为减少。往左为增加，往右为减少
        btn_set_inverted_appearance.clicked.connect(lambda: sd.setInvertedAppearance(
            not sd.invertedAppearance()))
        buttom_layout.addWidget(btn_set_inverted_appearance)

        def set_slider_down():
            sd.setSliderDown(not sd.isSliderDown())
            print(f'滑块按下状态: {sd.isSliderDown()}')

        btn_set_slider_down = QPushButton("设置滑块按下")
        btn_set_slider_down.clicked.connect(set_slider_down)
        buttom_layout.addWidget(btn_set_slider_down)

        # 可用信号
        sd.actionTriggered.connect(lambda val: print(
            f'actionTriggered: {val}'))  # 当用户点击滑块时触发
        """
        SliderRangeChange = 0
        SliderSingleStepAdd = 1
        SliderSingleStepSub = 2
        SliderPageStepAdd = 3
        SliderPageStepSub = 4
        SliderToMinimum = 5
        SliderToMaximum = 6
        SliderMove = 7
        """
        sd.sliderPressed.connect(lambda: print('sliderPressed'))  # 当滑块被按下时触发
        sd.sliderReleased.connect(lambda: print('sliderReleased'))  # 当滑块被释放时触发

        sd.valueChanged.connect(lambda val: print(
            f'valueChanged: {val}'))  # 当滑块的值发生变化时触发,返回新值
        sd.sliderMoved.connect(lambda val: print(
            f'sliderMoved: {val}'))  # 当滑块被移动时触发，返回新值

        # 当滑块的范围发生变化时触发，返回一个元组(最小值，最大值)
        sd.rangeChanged.connect(lambda *val: print(f'rangeChanged: {val}'))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
