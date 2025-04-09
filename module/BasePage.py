from module import *

class PageObject:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.url = ""

    def navigator(self):
        self.page.goto(self.url)

    def click_button(self,button_name,timeout=30_000):
        # self.page.get_by_role("button").filter(has_text=button_name).click(timeout=timeout)
        button_loc = self.page.locator("button")
        for 单字符 in button_name:
            button_loc = button_loc.filter(has_text=单字符)
        button_loc.click(timeout=timeout)