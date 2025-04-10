import os

def load_style():
    """
    加载全局样式表
    
    返回:
        str: 样式表内容
    """
    # 获取当前文件所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 样式文件路径
    style_file = os.path.join(current_dir, 'qss', 'style.qss')
    
    try:
        with open(style_file, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"读取样式文件出错: {str(e)}")
        return "" 