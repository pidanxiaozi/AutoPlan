
from playwright.sync_api import expect
from test_cases import *
from module.PageInstance import PageIns
"""
46章
storage_state.json 存储的是用户的登录状态，
用法：page.context.storage_state(path="storage_state.json")存储当前用户的登录状态
      context = browser.new_context(storage_state="storage_state.json")使用存储的登录状态
"""
def test_storage_state(browser: Browser) -> None:
    # my_page = PageIns(page)
    # my_page.登录页.登陆方法("pidanxiaozi","weijuhong581")
    # my_page.page.context.storage_state(path="storage_state.json")#存储当前用户的登录状态
    # my_page.page.context = my_page.page.browser.new_context(storage_state="storage_state.json")#使用存储的登录状态
    context = browser.new_context(storage_state="storage_state.json")    # 使用指定的存储状态创建一个新的浏览器上下文。
    page = context.new_page()
    page.goto("https://pidanxiaozi.ezone.work/workbench")
    page


def test_storage_state(page: Page,browser: Browser) -> None:
    my_page = PageIns(page)
    my_page.登录页.登陆方法("pidanxiaozi","weijuhong581")
    my_page.page.context.storage_state(path="storage_state.json")#存储当前用户的登录状态
