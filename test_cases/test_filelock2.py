
from playwright.sync_api import expect
from test_cases import *
from module.PageInstance import PageIns
"""
49章
with FileLock("lock.loc") - 使用文件锁机制：
创建一个名为"lock.loc"的锁文件
确保同一时间只有一个测试进程能执行with块内的代码
执行完成后自动释放锁
"""
def test_filelock2(page: Page) -> None:
    # baidu = Baidu(page)#初始化要验证的页面
    my_page = PageIns(page)
    with FileLock(get_path("/./.temp/"
                           "lock.loc")):
        my_page.百度.baidu_search("playwright", "playwright")
        # page.wait_for_timeout(3000)
        global_map = GlobalMap()
        global_map.set("b", "456")
        # assert global_map.get("a") == "123"
        assert global_map.get("b") == "456"
