import json
import pandas as pd
from pathlib import Path


class ExcelHelper:
    @staticmethod
    def read_excel(path: str) -> dict:
        excel_path = Path(path)

        if not excel_path.exists():
            print(f"找不到Excel文件: {excel_path}")
            return

        # pandas会自动检测文件格式（.xlsx或.xls）
        df = pd.read_excel(excel_path)

        if not ExcelHelper.check_excel_data(df):
            print("Excel数据不符合要求")
            return

        return ExcelHelper.organize_data(df)

    @staticmethod
    def check_excel_data(df: pd.DataFrame) -> bool:
        """
        检查Excel数据是否符合要求

        规范要求：
        1. DataFrame至少包含三列：Category、Attribute、Value
        2. 每一行的Category和Attribute不能为空
        3. Value可以为空
        """
        required_columns = ["Category", "Attribute", "Value"]

        if not all(col in df.columns for col in required_columns):
            return False

        if df.empty:
            return False

        # 检查每一行的必填字段
        empty_category_rows = df[df["Category"].isna() | (
            df["Category"] == "")].index.tolist()
        if empty_category_rows:
            print(f"错误：第 {[i+2 for i in empty_category_rows]} 行的Category为空")
            return False

        empty_attribute_rows = df[df["Attribute"].isna() | (
            df["Attribute"] == "")].index.tolist()
        if empty_attribute_rows:
            print(f"错误：第 {[i+2 for i in empty_attribute_rows]} 行的Attribute为空")
            return False

        return True

    @staticmethod
    def organize_data(df) -> dict:
        """
        将DataFrame数据组织成嵌套的字典结构
        """
        organized_data = {}

        for _, row in df.iterrows():
            try:
                category = row["Category"]
                attribute = row["Attribute"]
                value = row["Value"]

                # 如果类别不存在，创建一个新的字典
                if category not in organized_data:
                    organized_data[category] = {}

                # 如果属性不存在，创建一个新的列表
                if attribute not in organized_data[category]:
                    organized_data[category][attribute] = []

                # 添加值到相应的属性列表中
                organized_data[category][attribute].append(value)
            except Exception as e:
                pass

        return organized_data

    @staticmethod
    def dict_to_excel(dict_data: dict, output_path: str):
        # 转换数据为DataFrame
        df = pd.DataFrame()

        # 遍历JSON数据
        for category, attributes in dict_data.items():
            # 遍历属性
            for attr_name, values in attributes.items():
                # 遍历属性值
                for value in values:
                    # 创建新行
                    new_row = pd.DataFrame(
                        [{'Category': category, 'Attribute': attr_name, 'Value': value}])
                    # 添加新行到DataFrame
                    df = pd.concat([df, new_row], ignore_index=True)

        df.to_excel(output_path, index=False, engine='openpyxl')

    @staticmethod
    def json_to_excel(json_path: str, output_path: str, mode: int):
        """
        将JSON数据转换为Excel文件
        mode: 0 表示xlsx格式, 1 表示xls格式
        """
        output_path = output_path / \
            "attribute.xlsx" if mode == 0 else output_path / "attribute.xls"

        # 读取JSON文件
        if not json_path.exists():
            print(f"找不到JSON文件: {json_path}")
            return

        with open(json_path, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            ExcelHelper.dict_to_excel(json_data, output_path)
