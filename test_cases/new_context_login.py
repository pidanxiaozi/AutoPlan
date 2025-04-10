"""
47章
使用new_context()方法创建新的上下文
"""

from module.BasePage import 使用new_context登录并返回实例化的page
from module import *
from data_module.my_data import MYData

# def test_new_context(new_context) -> None:
#     # 使用new_context()    方法创建新的上下文
#     context1 :BrowserContext = new_context(storage_state="storage_state.json")
#     context1.new_page().goto("/workbench/myapproval")
#     context2: BrowserContext = new_context()
#     context2.new_page().goto("/workbench/myapproval")
#     context1
# @pytest.mark.browser_context_args(storage_state="storage_state.json")
# def test_new_context(page:Page):
#     page.goto("/workbench/myapproval")
#     page

# 第五十五章 登录的封装-编写登录代码的用例
def test_new_context(new_context):
    my_page_测试员1 = 使用new_context登录并返回实例化的page(new_context, "测试员1")
    # my_page_测试员= 使用new_context登录并返回实例化的page(new_context, "测试员")
    my_page_测试员1
