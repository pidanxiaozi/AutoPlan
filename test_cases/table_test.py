from module.BasePage import 使用new_context登录并返回实例化的page
from module import *
from data_module.auth_data import MYData
"""
第六十二章_表格的封装--创建Table类并在POM中实例化
"""

def test_new_context(new_context):
    my_page_测试员1 = 使用new_context登录并返回实例化的page(new_context, "测试员1")
    my_page_测试员1.项目集.navigator()
    # table_div = my_page_测试员1.项目集.主表格.table_div.highlight()
    my_page_测试员1.page.wait_for_timeout(3_000)
    # index = my_page_测试员1.项目集.主表格.get_header_index("开始时间")
    # loc =my_page_测试员1.项目集.主表格.get_row_locator(my_page_测试员1.page.get_by_text("自动化创建项目集_1744289519273708700")).highlight()
    # 完成时间=my_page_测试员1.项目集.主表格.get_cell_locator(1,16).text_content()
    # my_page_测试员1.项目集.主表格.get_row_dict()
    # my_page_测试员1.项目集.主表格.get_row_dict(-1)
    # my_page_测试员1.项目集.主表格.get_row_dict(my_page_测试员1.page.get_by_text("自动化创建项目集_1744597235125746200"))
    # my_page_测试员1.项目集.主表格.get_row_dict(my_page_测试员1.page.get_by_text("2025-04-27"))
    # my_page_测试员1.项目集.主表格.get_col_list("开始时间")
    # my_page_测试员1.项目集.主表格.get_col_list("项目集名称")
    # my_page_测试员1.项目集.主表格.get_col_list("完成时间")
    # my_page_测试员1.项目集.主表格.get_col_list("项目数")
    # my_page_测试员1.项目集.表单_文本框填写("项目集名称","123")

    # my_page_测试员1.page.wait_for_selector("label:has-text('项目集名称')")  # 添加等待
    my_page_测试员1.项目集.表单_文本框填写("项目集名称", "123")
    my_page_测试员1.项目集.表单_文本框填写("项目集名称1", "123", timeout=3000)
    my_page_测试员1.项目集.表单_文本框填写("项目集名称", "123123456", my_page_测试员1.page.locator(
        '//*[@class="ant-form ant-form-horizontal"]'))# 定位最外层表单



    # print(完成时间)
    my_page_测试员1

