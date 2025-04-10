from module import *

"""
第六十二章_表格的封装--创建Table类并在POM中实例化

"""


class Table:
    def __init__(self, page: Page, 唯一文字: str, 表格序号: int = -1):
        self.page = page
        self.table_div = self.page.locator(".ant-table-wrapper").filter(has_text=唯一文字).nth(表格序号)
# .ant-table-container