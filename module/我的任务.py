from playwright.sync_api import expect

from module import *
from  module.BasePage import PageObject
class 我的任务_类(PageObject):
    def __init__(self, page):
        super().__init__(page)
        self.url = "/workbench/mytask"
        self.通知铃铛 = self.page.get_by_text("P", exact=True).first

