import os


class StyleManager:
    """
    集中管理应用程序中的所有QSS样式
    """

    FONT_SIZE = 16  # 默认字体大小

    @staticmethod
    def _read_qss_file(file_path):
        """
        读取QSS文件内容
        """
        if not os.path.exists(file_path):
            print(f"警告: QSS文件不存在 - {file_path}")
            return ""

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            print(f"读取QSS文件出错: {str(e)}")
            return ""

    @staticmethod
    def _get_qss_dir_path():
        """
        获取QSS文件所在目录的路径
        """
        # 获取当前文件所在目录
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # QSS文件目录路径
        qss_dir = os.path.join(current_dir, 'qss')
        return qss_dir

    @staticmethod
    def get_annotation_tool_style():
        """
        获取AnnotationTool的样式表
        """
        qss_dir = StyleManager._get_qss_dir_path()
        base_qss = StyleManager._read_qss_file(
            os.path.join(qss_dir, 'annotation_tool.qss'))
        scrollbar_qss = StyleManager._read_qss_file(
            os.path.join(qss_dir, 'scrollbar.qss'))

        # 添加字体大小的样式
        font_size_qss = f"""
            QCheckBox {{
                font-size: {StyleManager.FONT_SIZE}px;
            }}
            QGroupBox {{
                font-size: {StyleManager.FONT_SIZE}px;
            }}
            QGroupBox::title {{
                font-size: {StyleManager.FONT_SIZE}px;
            }}
        """

        return base_qss + scrollbar_qss + font_size_qss

    @staticmethod
    def get_show_attributes_dialog_style():
        """
        获取ShowAttributesDialog的样式表
        """
        qss_dir = StyleManager._get_qss_dir_path()
        base_qss = StyleManager._read_qss_file(
            os.path.join(qss_dir, 'show_attributes_dialog.qss'))

        # 添加字体大小的样式
        font_size_qss = f"""
            QLabel {{
                font-size: {StyleManager.FONT_SIZE}px;
            }}
            QPushButton {{
                font-size: {StyleManager.FONT_SIZE}px;
            }}
            QLabel#rootNameLabel {{
                font-size: {StyleManager.FONT_SIZE}px;
            }}
            QLineEdit#rootNameInput {{
                font-size: {StyleManager.FONT_SIZE}px;
            }}
        """

        return base_qss + font_size_qss

    @staticmethod
    def get_attribute_edit_dialog_style():
        """
        获取AttributeEditDialog的样式表
        """
        qss_dir = StyleManager._get_qss_dir_path()
        base_qss = StyleManager._read_qss_file(
            os.path.join(qss_dir, 'attribute_edit_dialog.qss'))

        # 添加字体大小的样式
        font_size_qss = f"""
            #addValueBtn, #confirmBtn, #cancelBtn {{
                font-size: {StyleManager.FONT_SIZE}px;
            }}
            #nameTitle, #valuesTitle {{
                font-size: {StyleManager.FONT_SIZE}px;
            }}
            #nameInput, #valueInput {{
                font-size: {StyleManager.FONT_SIZE}px;
            }}
        """

        return base_qss + font_size_qss

    @staticmethod
    def get_common_style():
        """
        获取通用样式，应用于整个应用程序
        """
        qss_dir = StyleManager._get_qss_dir_path()
        base_qss = StyleManager._read_qss_file(
            os.path.join(qss_dir, 'common.qss'))

        # 添加字体大小的样式
        font_size_qss = f"""
            QPushButton {{
                font-size: {StyleManager.FONT_SIZE}px;
            }}
            QLabel {{
                font-size: {StyleManager.FONT_SIZE}px;
            }}
            QLineEdit {{
                font-size: {StyleManager.FONT_SIZE}px;
            }}
            QGroupBox {{
                font-size: {StyleManager.FONT_SIZE}px;
            }}
        """

        return base_qss + font_size_qss

    @staticmethod
    def get_scrollbar_style():
        """
        获取滚动条样式
        """
        qss_dir = StyleManager._get_qss_dir_path()
        return StyleManager._read_qss_file(os.path.join(qss_dir, 'scrollbar.qss'))

    @staticmethod
    def get_combined_style(*style_names):
        """
        组合多个样式

        参数:
            style_names: 样式名称列表，可以是以下值的组合:
                         'common', 'scrollbar', 'annotation_tool', 
                         'show_attributes_dialog', 'attribute_edit_dialog'

        返回:
            组合后的样式表字符串
        """
        qss_dir = StyleManager._get_qss_dir_path()
        combined_qss = ""

        name_to_file = {
            'common': 'common.qss',
            'scrollbar': 'scrollbar.qss',
            'annotation_tool': 'annotation_tool.qss',
            'show_attributes_dialog': 'show_attributes_dialog.qss',
            'attribute_edit_dialog': 'attribute_edit_dialog.qss'
        }

        for name in style_names:
            if name in name_to_file:
                file_path = os.path.join(qss_dir, name_to_file[name])
                combined_qss += StyleManager._read_qss_file(file_path) + "\n"

        # 添加字体大小的样式
        font_size_qss = f"""
            /* 字体大小样式 */
            QLabel, QPushButton, QCheckBox, QLineEdit, QGroupBox {{
                font-size: {StyleManager.FONT_SIZE}px;
            }}
            QGroupBox::title {{
                font-size: {StyleManager.FONT_SIZE}px;
            }}
        """

        return combined_qss + font_size_qss
