import pytest
from playwright.sync_api import Page, sync_playwright


# pytest启动的方式
def test_baidu(page: Page):
    page.goto("https://www.baidu.com")
    page.get_by_role("link", name="新闻").click()
    page
@pytest.fixture()
def hello1():
    print("hello")#运行test_baidu1前会优先  print("hello")
    yield
    print("\n'bye'")#用例结束后会运行 print("\n'bye'")
# 执行命令：pytest -m only pw_layer.py,仅会执行@pytest.mark.only  fixture的方法
@pytest.mark.only
def test_baidu1(page: Page,hello1):
    page.goto("https://www.baidu.com")
    page.get_by_role("link", name="新闻").click()
    page
# 非pytest运行的方式
def pw1_baidu():
    # pw = sync_playwright().start()
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False,slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.baidu.com")
        page.get_by_role("link", name="新闻").click()
        # pw.stop()#如果用pw.stop()，pw2_baidu()运行会报错
def pw2_baidu():
    pw = sync_playwright().start()
    browser = pw.chromium.launch(headless=False,slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.baidu.com")
    page.get_by_role("link", name="新闻").click()
    page
# pw1_baidu()
# pw2_baidu()