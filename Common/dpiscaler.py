from PyQt5.QtWidgets import QApplication


class DpiScaler:
    BASE_DPI = 96  # 以 1080P 96DPI 为基准
    BASE_FONT_SIZE_PX = 14  # 基准字体大小

    @classmethod
    def scaled_font_size(cls, font_size = BASE_FONT_SIZE_PX):
        """
        计算缩放后的字体大小
        """
        screen = QApplication.primaryScreen()  # 获取主屏幕
        physical_dpi = screen.physicalDotsPerInch()  # 获取物理DPI
        # 计算缩放后的字体大小
        return round(font_size * physical_dpi / cls.BASE_DPI)
