
from playwright.sync_api import expect

from module import 登录页_类
from test_cases import *

def test_login(page: Page) -> None:
    # baidu = Baidu(page)#初始化要验证的页面
    login_page = 登录页_类(page)
    login_page.登陆方法("pidanxiaozi","weijuhong581")
    login_page.page.goto("https://pidanxiaozi.ezone.work/workbench/mytask")
    login_page
