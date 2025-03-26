import sys

from PyQt5.QtWidgets import QApplication, QWidget, QFrame

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("QFrame-功能作用")
window.resize(500, 500)
# window.move(400, 250)

frame = QFrame(window)
frame.resize(200, 200)

# frame.setFrameShape(QFrame.Box)
# frame.setFrameShape(QFrame.Panel)
# frame.setFrameShadow(QFrame.Raised)

frame.setFrameStyle(QFrame.Box | QFrame.Raised)

frame.setLineWidth(5)  # 外线宽度
frame.setMidLineWidth(6)  # 中线宽度

print(frame.frameWidth())

# frame.setFrameRect(QRect(50, 50, 50, 50))  # 框架矩形

frame.move(100, 100)


window.show()

sys.exit(app.exec_())
