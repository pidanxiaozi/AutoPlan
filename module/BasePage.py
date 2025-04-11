import os

from filelock import FileLock

from data_module.auth_data import MYData
from module import *
from utils.GetPath import get_path
from utils.globalMap import GlobalMap  # 添加这行导入
from module.table import Table


class PageObject:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.url = ""

    def navigator(self):
        self.page.goto(self.url)

    def table(self, 唯一文字, 表格序号=-1):
        return Table(self.page, 唯一文字, 表格序号)

    def click_button(self, button_name, timeout=30_000):
        # self.page.get_by_role("button").filter(has_text=button_name).click(timeout=timeout)
        button_loc = self.page.locator("button")
        for 单字符 in button_name:
            button_loc = button_loc.filter(has_text=单字符)
        button_loc.click(timeout=timeout)

    # 第五十八章_搜索的封装-页面和接口在这里融合
    # def search(self, 搜索内容: str, placeholder=None):
    #     if placeholder:
    #         self.page.locator(f"//span[@class='ant-input-affix-wrapper']//input[contains(@placeholder,'{placeholder}')]").fill(
    #             搜索内容)
    #     else:
    #         self.page.locator(".ant-input-affix-wrapper input").fill(搜索内容)
    #     self.page.wait_for_load_state("networkidle")  # 等待网络空闲状态


# 第五十四章_登录的封装 - 登录的伪代码
# def w使用new_context登录并返回实例化的page(new_context, 用户别名):
#     baseurl = "通过globalmap回去baseurl"
#     被测环境 = "通过对字符串截取或正则拿到环境,比如https://pidanxiaozi.ezone.work"
#     用户名 = "通过用户信息获取用户名"
#     密码 = "通过用户信息获取密码"
#     with f"这里使用filelock进行文件锁,锁的文件名为{被测环境}-{用户别名}.lock":
#         if f".temp/{被测环境}-{用户别名}.json存在,判断方法os.path.exists":
#             context = new_context(storage_state=f".temp/{被测环境}-{用户别名}.json")
#             page = context.new_page()
#             my_page = "PageIns实例化page,获得所有页面的控制方法"
#             # 需要新增一个首页的封装
#             my_page.首页.navigate()
#             登录成功 = "判断下是成功登录上了,还是登录失败"
#             if not 登录成功:
#                 my_page.登录页.navigate()
#                 my_page.登录页.登录(用户名, 密码)
#                 f"把storage_state保存为.temp/{被测环境}-{用户别名}.json"
#             else:
#                 context = new_context()
#                 page = context.new_page
#                 my_page = "PageIns实例化page,获得所有页面的控制方法"
#                 my_page.登录页.登录(用户名, 密码)
#                 f"把storage_state保存为.temp/{被测环境}-{用户别名}.json"
#
#     return page

# 第五十五章登录的封装 - 编写登录代码
def 使用new_context登录并返回实例化的page(new_context, 用户别名):
    from module.PageInstance import PageIns
    global_Map = GlobalMap()
    被测环境 = global_Map.get("env")
    # 用户名 = MYData().userinfo(被测环境, 用户别名)["username"]
    # 密码 = MYData().userinfo(被测环境, 用户别名)["password"]
    # 修改为正确的调用方式
    用户信息 = MYData().userinfo()  # 先获取全部用户信息
    用户名 = 用户信息["pidanxiaozi"][用户别名]["username"]  # 然后根据别名获取用户名
    密码 = 用户信息["pidanxiaozi"][用户别名]["password"]  # 同样方式获取密码
    with FileLock(get_path(f".temp/{被测环境}-{用户别名}.lock")):
        if os.path.exists(get_path(f".temp/{被测环境}-{用户别名}.json")):
            context: BrowserContext = new_context(storage_state=get_path(f".temp/{被测环境}-{用户别名}.json"))
            page = context.new_page()
            my_page = PageIns(page)
            my_page.我的任务.navigator()
            expect(my_page.登录页.用户名输入框.or_(my_page.登录页.通知铃铛)).to_be_visible()
            if my_page.登录页.用户名输入框.count():  # count()如果存在返回1,不存在返回0
                my_page.登录页.登陆方法(用户名, 密码)
                context.storage_state(path=get_path(f".temp/{被测环境}-{用户别名}.json"))

        else:
            context: BrowserContext = new_context()
            page = context.new_page()
            my_page = PageIns(page)
            my_page.登录页.登陆方法(用户名, 密码)
            my_page.page.context.storage_state(path=get_path(f".temp/{被测环境}-{用户别名}.json"))

    return my_page
