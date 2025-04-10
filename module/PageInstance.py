# from module import *
from playwright.sync_api import Page

from module import 登录页_类, 我的任务_类, 项目集_类
from module.BaiduPage import Baidu  # 显式导入Baidu类

class PageIns:
    def __init__(self,page:Page) -> None:
        self.page = page
        self.百度 = Baidu(self.page)
        self.登录页 = 登录页_类(self.page)
        self.我的任务 = 我的任务_类(self.page)
        self.项目集 = 项目集_类(self.page)