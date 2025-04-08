from PyQt5.QtWidgets import QWidget, QApplication


class WindowUtils:
    """
    窗口工具类
    """

    @staticmethod
    def center_on_screen(window: QWidget):
        """
        将窗口居中显示在屏幕上

        参数:
            window: 需要居中显示的窗口，必须是 QWidget 或其子类的实例
        """
        if not isinstance(window, QWidget):
            raise TypeError("窗口必须是 QWidget 或其子类的实例")

        screen = QApplication.primaryScreen()
        center_point = screen.availableGeometry().center()
        x = int(center_point.x() - window.width() / 2)
        y = int(center_point.y() - window.height() / 2)
        window.move(x, y)

    @staticmethod
    def center_on_parent(window: QWidget):
        """
        将窗口相对于父窗口居中显示
        如果没有父窗口或父窗口不可见，则相对于屏幕居中

        参数:
            window: 需要居中显示的窗口，必须是 QWidget 或其子类的实例
        """
        if not isinstance(window, QWidget):
            raise TypeError("窗口必须是 QWidget 或其子类的实例")

        parent = window.parent()

        if parent and isinstance(parent, QWidget) and parent.isVisible():
            # 相对于父窗口居中
            parent_rect = parent.geometry()
            x = parent.x() + int((parent_rect.width() - window.width()) / 2)
            y = parent.y() + int((parent_rect.height() - window.height()) / 2)
            window.move(x, y)
        else:
            # 相对于屏幕居中
            WindowUtils.center_on_screen(window)
