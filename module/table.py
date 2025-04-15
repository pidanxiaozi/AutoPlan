import random

from module import *

"""
第六十二章_表格的封装--创建Table类并在POM中实例化

"""


class Table:
    def __init__(self, page: Page, 唯一文字: str, 表格序号: int = -1):
        self.page = page
        self.page.wait_for_load_state("networkidle")  # 等待网络空闲状态
        # 定位Ant Design表格容器
        # 1. 先通过.ant-table-wrapper类名定位所有表格容器
        # 2. 再通过filter筛选包含指定文本(唯一文字)的表格
        # 3. 最后通过nth选择指定序号(表格序号)的表格，-1表示最后一个
        self.table_div = self.page.locator(".ant-table-wrapper").filter(has_text=唯一文字).nth(表格序号)
        self.table_header_tr = self.table_div.locator("//thead/tr")

    # 获取表头文字定位
    def get_header_index(self, 表头文字: str) -> int:
        return self.table_header_tr.locator("th").all_text_contents().index(表头文字)

    # 获取行文字定位
    def get_row_locator(self, 行元素定位: Locator) -> Locator:
        return self.table_div.locator("tr").filter(has=行元素定位)

    def get_cell_locator(self, 表头文字or列序号: str or int, 行元素定位or行序号or行文字:

    Locator or int or str) -> Locator:

        if isinstance(表头文字or列序号, str):
            列序号 = self.get_header_index(表头文字or列序号)
        else:
            列序号 = 表头文字or列序号
        if isinstance(行元素定位or行序号or行文字, Locator):
            行定位 = self.get_row_locator(行元素定位or行序号or行文字)
        elif isinstance(行元素定位or行序号or行文字, str):
            行定位 = self.table_div.locator("tr").filter(has_text=行元素定位or行序号or行文字)
        elif isinstance(行元素定位or行序号or行文字, int):
            行定位 = self.table_div.locator("tbody").locator("//tr[not(@aria-hiden='true')]").nth(行元素定位or行序号or行文字)

        return 行定位.locator("td").nth(列序号)

    # 第六十五章_表格的封装 - 获取指定行的值的字典
    # 使用空获取随机行的数据,使用行的index获取指定行的数据,使用定位器获取指定行的数据
    def get_row_dict(self,行元素定位or行序号: Locator or int = "random"):
        if isinstance(行元素定位or行序号, int):
            tr = self.table_div.locator("tbody").locator("tr").locator("visible ='true'").nth(行元素定位or行序号)
        elif isinstance(行元素定位or行序号, Locator):
            tr = self.table_div.locator("tr").filter(has=行元素定位or行序号)
        else:
            all_tr = self.table_div.locator("tbody").locator("tr").locator("visible ='true'").all()
            tr = random.choice(all_tr)

        td_text_list = tr.locator("td").all_text_contents()
        header_text_list = self.table_header_tr.locator("th").all_text_contents()
        row_dict = dict(zip(header_text_list, td_text_list))
        return row_dict
    # 使用列表名称获取当前列内容
    def get_col_list(self,表头文字: str) -> list:
        index = self.get_header_index(表头文字)
        all_list = self.table_div.locator("tbody").locator("tr").locator("visible ='true'").all()
        col_list = []
        for tr in all_list:
            col_list.append(tr.locator("td").nth(index).text_content())
        return col_list


