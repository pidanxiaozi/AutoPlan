import time

from playwright.sync_api import expect

from module import *
from  module.BasePage import PageObject
class 项目集_类(PageObject):
    def __init__(self, page):
        super().__init__(page)
        self.url = "/portfolio"
        self.项目集名称 = self.page.get_by_placeholder("-32个字符")
        self.请输入项目集名称 = self.page.get_by_placeholder("请输入项目集名称")
        self.设置齿轮 = self.page.get_by_role("cell", name="star setting").locator("span").nth(2)
        # self.设置齿轮 = self.page.get_by_role('//span[@aria-label="setting"]').locator("xpath=/..")
        self.运维操作 = self.page.get_by_role("link", name="运维操作")
        self.暂无数据 = self.page.get_by_text("暂无数据")
        self.开始时间 = self.page.get_by_placeholder("开始日期")
        self.结束日期 = self.page.get_by_placeholder("结束日期")

    @property
    def 主表格(self):
        return self.table(唯一文字:="项目集名称")

    def 创建项目集(self, 项目集名称="自动化创建项目集",是否需要纳秒时间戳=True,开始时间="1",结束日期="7") -> None:
        self.navigator()
        self.click_button("新建111",timeout=5_000)
        if 是否需要纳秒时间戳:
            项目集名称 = f"{项目集名称}_{time.time_ns()}"
        self.项目集名称.fill(项目集名称)
        self.开始时间.click()
        self.page.click('.ant-picker-cell-inner:has-text("28")')
        self.page.click('.ant-picker-cell-inner:has-text("28")')
        self.click_button("确定")
        self.请输入项目集名称.fill(项目集名称)
        self.page.wait_for_load_state('networkidle')
        # 修改断言，使用更精确的定位器
        expect(self.page.locator("tbody.ant-table-tbody").filter(has_text=项目集名称)).to_contain_text(项目集名称)
        return 项目集名称
    def 删除项目集(self, 项目集名称="自动化创建项目集") -> None:
        # while True:
        #     self.navigator()
        #     self.请输入项目集名称.fill(项目集名称)
        #     # self.search("自动化测试项目", "请输入项目集名称")
        #     self.page.wait_for_timeout(3_000)
        #     self.page.wait_for_load_state('networkidle')
        #     if self.暂无数据.count():
        #         break
        #     else:
        #         self.设置齿轮.last.click()
        #         self.运维操作.click()
        #         self.click_button("删除项目集")
        #         self.click_button("确定")
        self.navigator()
        self.请输入项目集名称.fill(项目集名称)
        # self.search("自动化测试项目", "请输入项目集名称")
        self.page.wait_for_timeout(3_000)
        self.page.wait_for_load_state('networkidle')
        if self.暂无数据.count():
            pass
        else:
            self.设置齿轮.last.click()
            self.运维操作.click()
            self.click_button("删除项目集")
            self.click_button("确定")






