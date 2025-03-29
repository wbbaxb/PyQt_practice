import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel
from PyQt5.QtCore import QObject

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test")
        self.resize(500, 500)
        self.move(400, 250)
        self.test()

    def test(self):
        obj = QObject()
        widget = QWidget()
        btn = QPushButton()
        label = QLabel()

        objs = [obj, widget, btn, label]

        for o in objs:
            print(f"""{o.objectName()} 是否为QObject类型: {isinstance(o, QObject)},
                  是否继承自QAbstractButton: {o.inherits("QAbstractButton")}""")
            
        # output:
        # True, False 
        # True, False
        # True, True
        # True, False

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
