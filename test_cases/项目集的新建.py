"""
第五十七章_一个实例说明如何编写一个高稳定用例
"""
from playwright.sync_api import BrowserContext

from module.BasePage import 使用new_context登录并返回实例化的page
from test_cases import *

# def test_项目集的新建(page: Page,browser: Browser) -> None:
#     my_page = PageIns(page)
#     my_page.登录页.登陆方法("pidanxiaozi","weijuhong581")
#     my_page.page.context.storage_state(path="storage_state.json")#存储当前用户的登录状态
#     context = browser.new_context(storage_state="storage_state.json")  # 使用指定的存储状态创建一个新的浏览器上下文。
#     my_page.项目集.创建项目集()
#     my_page

def test_项目集的新建(new_context,删除项目集):
    my_page_测试员 =使用new_context登录并返回实例化的page(new_context, "测试员1")
    # aa =my_page_测试员.项目集.创建项目集()
    # print(aa)    这样可以打印项目集的返回值
    my_page_测试员.项目集.创建项目集()
@pytest.fixture
def 删除项目集(new_context):
    print("创建完成执行这一步")
    yield
    my_page_测试员 =使用new_context登录并返回实例化的page(new_context, "测试员1")
    my_page_测试员.项目集.删除项目集()

def test_删除项目集(new_context):
    # print("创建完成执行这一步")
    # yield
    my_page_测试员 =使用new_context登录并返回实例化的page(new_context, "测试员1")
    my_page_测试员.项目集.删除项目集()
