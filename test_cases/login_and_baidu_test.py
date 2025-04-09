
from playwright.sync_api import expect
from test_cases import *
from module.PageInstance import PageIns

def test_longin_and_baidu(page: Page,base_url) -> None:
    # baidu = Baidu(page)#初始化要验证的页面
    my_page = PageIns(page)
    # my_page.登录页.登陆方法("pidanxiaozi","weijuhong581")
    # my_page.百度.baidu_search("playwright", "playwright")


    print(base_url)
    print(GlobalMap().get("baseurl"))
