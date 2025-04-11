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
            行定位 = self.table_div.locator("tbody").locator("tr").nth(行元素定位or行序号or行文字)

        return 行定位.locator("td").nth(列序号)
