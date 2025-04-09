import json
import pandas as pd
from pathlib import Path


class ExcelHelper:
    def __init__(self):
        self.dir_path = Path(__file__).parent
        self.xlsx_path = self.dir_path / "xlsx_for_read.xlsx"
        self.xls_path = self.dir_path / "xls_for_read.xls"

    def read_excel(self, path: str):
        excel_path = Path(path)

        if not excel_path.exists():
            print(f"找不到Excel文件: {excel_path}")
            return

        # pandas会自动检测文件格式（.xlsx或.xls）
        df = pd.read_excel(excel_path)

        if not self.check_excel_data(df):
            print("Excel数据不符合要求")
            return

        organized_data = self.organize_data(df)

        if organized_data:
            file_name = excel_path.stem  # 获取文件名（不包含扩展名）
            self.save_json_file(
                organized_data, self.dir_path / f"{file_name}.json")

    def check_excel_data(self, df: pd.DataFrame) -> bool:
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

    def organize_data(self, df):
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

    def save_json_file(self, dict_data: dict, output_path: str):
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(dict_data, f, ensure_ascii=False, indent=2)

    def json_to_excel(self, mode: int):
        """
        将JSON数据转换为Excel文件
        mode: 0 表示xlsx格式, 1 表示xls格式
        """
        json_path = self.dir_path / "attribute.json"
        output_path = self.dir_path / \
            "attribute.xlsx" if mode == 0 else self.dir_path / "attribute.xls"

        # 读取JSON文件
        if not json_path.exists():
            print(f"找不到JSON文件: {json_path}")
            return

        with open(json_path, 'r', encoding='utf-8') as f:
            json_data = json.load(f)

        # 转换数据为DataFrame
        df = pd.DataFrame()

        # 遍历JSON数据
        for category, attributes in json_data.items():
            # 遍历属性
            for attr_name, values in attributes.items():
                # 遍历属性值
                for value in values:
                    # 创建新行
                    new_row = pd.DataFrame(
                        [{'Category': category, 'Attribute': attr_name, 'Value': value}])
                    # 添加新行到DataFrame
                    df = pd.concat([df, new_row], ignore_index=True)

        # 对于新版pandas（1.5.0及以上），使用openpyxl引擎保存两种格式
        df.to_excel(output_path, index=False, engine='openpyxl')
        print(f"Excel文件已保存至: {output_path}")

    def main(self):
        # self.read_excel(self.xlsx_path)
        # self.read_excel(self.xls_path)
        self.json_to_excel(0)
        self.json_to_excel(1)


if __name__ == "__main__":
    ExcelTest().main()
