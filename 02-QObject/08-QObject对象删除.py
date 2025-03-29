import sys

from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QWidget, QApplication


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QObject对象删除")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        self.test_delete()

    def test_delete(self):
        # 删除一个对象时，也会解除与父对象的关系
        obj1 = QObject()
        obj1.setObjectName("obj1")
        obj2 = QObject()
        obj2.setObjectName("obj2")
        obj3 = QObject()
        obj3.setObjectName("obj3")

        obj3.setParent(obj2)
        obj2.setParent(obj1)

        # 当一个对象被释放时,会触发destroyed信号            
        obj1.destroyed.connect(lambda: print("obj1被释放了")) 
        obj2.destroyed.connect(lambda: print("obj2被释放了"))
        obj3.destroyed.connect(lambda: print("obj3被释放了"))

        # obj2删除后，其子对象obj3也会被删除，其父对象obj1不会被删除

        # 但是这里obj1还是被释放了,因为obj2被释放后，obj1的引用计数为0，其没有其他引用，所以被释放

        obj2.deleteLater()  # 和delete的区别,delete会立即释放,deleteLater会延迟释放(下一次消息循环)
        print([item.objectName() for item in obj1.children()]) # QObject.children() 方法返回的是当前对象的直接子对象列表，而不包括孙子对象
        print(obj2.objectName())

        """
        综上， output:
        ['obj2']
        obj2
        obj1被释放了
        obj2被释放了
        obj3被释放了
        """


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
