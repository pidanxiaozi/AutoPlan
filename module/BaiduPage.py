from playwright.sync_api import expect

from module import *
from  module.BasePage import PageObject
class Baidu(PageObject):
    def __init__(self, page):
        super().__init__(page)
        self.url = "https://www.baidu.com"
        self.search_input = page.locator("#kw")
        self.百度一下 = page.locator("#su")

    def baidu_search(self,search_key,search_result) -> None:
        self.navigator()
        self.search_input.fill(search_key)
        self.百度一下.click()
        expect(self.page.get_by_text(search_result).last).to_be_visible()