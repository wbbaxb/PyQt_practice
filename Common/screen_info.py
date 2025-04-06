import tkinter as tk
import ctypes


class ScreenInfo:
    """
    屏幕信息工具类
    用于获取显示器的逻辑分辨率、物理分辨率和缩放比例
    """

    @staticmethod
    def get_logical_resolution():
        """
        获取屏幕的逻辑分辨率

        Returns:
            tuple: 包含宽度和高度的元组 (width, height)
        """
        root = tk.Tk()
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        root.destroy()
        return width, height

    @staticmethod
    def get_scaling_factor():
        """
        获取屏幕的DPI缩放比例

        Returns:
            float: 屏幕缩放比例，例如1.0表示100%，1.5表示150%
        """
        try:
            # Windows 8.1及以上版本的DPI感知方法
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
            scale = ctypes.windll.shcore.GetScaleFactorForDevice(0) / 100
        except:
            # 对于不支持上述方法的Windows版本，使用替代方法
            hdc = ctypes.windll.user32.GetDC(0)
            dpi = ctypes.windll.gdi32.GetDeviceCaps(hdc, 88)  # LOGPIXELSX = 88
            ctypes.windll.user32.ReleaseDC(0, hdc)
            scale = dpi / 96  # 标准DPI为96

        return scale

    @staticmethod
    def get_physical_resolution(logical_resolution=None, scale=None):
        """
        获取屏幕的物理分辨率

        Args:
            logical_resolution (tuple, optional): 逻辑分辨率. 默认为None，将自动获取
            scale (float, optional): 缩放比例. 默认为None，将自动获取

        Returns:
            tuple: 包含物理宽度和高度的元组 (physical_width, physical_height)
        """
        if logical_resolution is None:
            logical_resolution = ScreenInfo.get_logical_resolution()

        if scale is None:
            scale = ScreenInfo.get_scaling_factor()

        physical_width = int(logical_resolution[0] * scale)
        physical_height = int(logical_resolution[1] * scale)

        return physical_width, physical_height

    @staticmethod
    def get_screen_info():
        """
        获取屏幕的完整信息，包括逻辑分辨率、缩放比例和物理分辨率

        Returns:
            tuple: 包含三个元素的元组:
                  (logical_resolution, scale, physical_resolution)
        """
        logical_res = ScreenInfo.get_logical_resolution()
        scale = ScreenInfo.get_scaling_factor()
        physical_res = ScreenInfo.get_physical_resolution(logical_res, scale)

        return logical_res, scale, physical_res


# 演示用法
if __name__ == "__main__":
    # 获取所有屏幕信息
    logical_res, scale, physical_res = ScreenInfo.get_screen_info()

    # 打印结果
    print(f"逻辑分辨率: {logical_res[0]}x{logical_res[1]}")
    print(f"缩放比例: {scale}")
    print(f"物理分辨率: {physical_res[0]}x{physical_res[1]}")

    # 也可以单独使用各个方法
    # print(f"逻辑分辨率: {ScreenInfo.get_logical_resolution()}")
    # print(f"缩放比例: {ScreenInfo.get_scaling_factor()}")
    # print(f"物理分辨率: {ScreenInfo.get_physical_resolution()}")
