from playwright.sync_api import expect

from module import Baidu
from test_cases import *

def test_baidu(page: Page) -> None:
    baidu = Baidu(page)
    # baidu.navigator()
    # baidu.search_input.fill("playwright")
    # baidu.click_button("百度一下", timeout=3000)
    # expect(baidu.page.get_by_text("https://github.com/microsoft/playwright").last).to_be_visible()
    baidu.baidu_search("playwright", "playwright")

    baidu