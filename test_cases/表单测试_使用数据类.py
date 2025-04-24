from data_module.项目集数据类模块 import *
from module.BasePage import 使用new_context登录并返回实例化的page
from module import *
from data_module.auth_data import MYData
from data_module import *
"""
第七十六章"表单的封装--数据类的使用
"""

def test_表单测试_使用数据类(new_context):
    my_page_测试员1 = 使用new_context登录并返回实例化的page(new_context, "测试员1")
    my_page_测试员1.项目集.navigator()
    my_page_测试员1.page.wait_for_timeout(3_000)
    my_page_测试员1.项目集.click_button("新建")
    新建项目=项目集数据类_新建项目集(项目集名称="test123",项目集周期="2025-04-04,2025-04-27",父项目集="333")
    # 新建项目.as_dict()#可以使用:新建项目.as_dict()查看dict中存放的值
    my_page_测试员1.项目集.快捷操作_填写表单(**新建项目.as_dict())

    my_page_测试员1.项目集







    # print(完成时间)
    my_page_测试员1

