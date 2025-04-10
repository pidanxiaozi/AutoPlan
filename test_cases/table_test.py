from module.BasePage import 使用new_context登录并返回实例化的page
from module import *
from data_module.auth_data import MYData
"""
第六十二章_表格的封装--创建Table类并在POM中实例化
"""

def test_new_context(new_context):
    my_page_测试员1 = 使用new_context登录并返回实例化的page(new_context, "测试员1")
    my_page_测试员1.项目集.navigator()
    table_div = my_page_测试员1.项目集.主表格.table_div.highlight()
    print(table_div)
    my_page_测试员1

