import os
import json
from pathlib import Path


class AttributeConfigHelper():
    """
    属性文件操作类
    只支持windows系统,其他系统没有测试条件
    """

    def __init__(self) -> None:
        pass

    @staticmethod
    def get_config_path():
        if os.name == 'nt':  # windows
            # os.environ['APPDATA'] 获取用户主目录
            return Path(os.environ['APPDATA']) / "AnyLabeling" / "attributes.json"
        else:
            raise OSError(f"不支持的操作系统: {os.name}")

    @staticmethod
    def get_config() -> dict:
        config_path = AttributeConfigHelper.get_config_path()

        if not config_path.exists():
            return {}

        with open(config_path, "r", encoding="utf-8") as f:
            attributes = json.load(f)

            if not attributes:
                return {}

            keys = list(attributes.keys())
            key = keys[0] if keys else []

            if not key:
                return {}

            return attributes

    @staticmethod
    def save_config(data):
        config_path = AttributeConfigHelper.get_config_path()
        config_path.parent.mkdir(parents=True, exist_ok=True)
        with open(config_path, 'w', encoding="utf-8") as f:
            # ensure_ascii=False 防止中文乱码, indent=2 缩进2个空格
            json.dump(data, f, ensure_ascii=False, indent=2)

    @staticmethod
    def load_config():
        config_path = AttributeConfigHelper.get_config_path()
        if config_path.exists():
            with open(config_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return None
