import sys

from PyQt5.QtWidgets import QApplication, QWidget, QAbstractButton
from PyQt5.QtGui import QPainter, QPen, QColor

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("QAbstractButton")
window.resize(500, 500)
window.move(400, 250)


class Btn(QAbstractButton):
    """自定义按钮"""

    # 重写绘制事件，绘制按钮的界面
    def paintEvent(self, evt) -> None:
        # print("绘制")
        # 绘制按钮上要展示的一个界面内容
        # 手动绘制
        painter = QPainter(self)  # 创建一个画家；告诉画在什么地方
        pen = QPen(QColor(20, 154, 151), 5)  # 创建并设置一个笔,5是笔的宽度
        painter.setPen(pen)  # 把笔给画家
        painter.drawText(100, 100, self.text())  # 把按钮文字画在按钮上,x,y,text
        painter.drawEllipse(50, 50, 200, 120)  # 画个椭圆,x,y,w,h


btn = Btn(window)
btn.setText("Custom Button")
btn.resize(300, 200)
btn.clicked.connect(lambda: print("点击了这个按钮"))

window.show()
sys.exit(app.exec_())
