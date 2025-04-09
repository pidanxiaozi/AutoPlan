import page
from playwright.sync_api import expect,Page
from test_cases import *
import pytest
from module.PageInstance import PageIns
"""
47章
使用new_context()方法创建新的上下文
"""
# def test_new_context(new_context) -> None:
#     # 使用new_context()    方法创建新的上下文
#     context1 :BrowserContext = new_context(storage_state="storage_state.json")
#     context1.new_page().goto("/workbench/myapproval")
#     context2: BrowserContext = new_context()
#     context2.new_page().goto("/workbench/myapproval")
#     context1
@pytest.mark.browser_context_args(storage_state="storage_state.json")
def test_new_context(page:Page):
    page.goto("/workbench/myapproval")
    page
