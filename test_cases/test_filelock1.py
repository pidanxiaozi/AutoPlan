from playwright.sync_api import expect
from test_cases import *
from module.PageInstance import PageIns

"""
49章
"/./temp/lock.loc"   指定执行lock文件时生成的lock文件的路径
"""


def test_filelock1(page: Page) -> None:
    # baidu = Baidu(page)#初始化要验证的页面
    my_page = PageIns(page)
    with FileLock(get_path("/./.temp/"
                           "lock.loc")):
        my_page.百度.baidu_search("playwright", "playwright")
        # page.wait_for_timeout(3000)
        global_map = GlobalMap()
        global_map.set("a","123")
