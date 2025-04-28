import re

import allure
import pytest

from utils.globalMap import GlobalMap


# @pytest.fixture()
# def hello1():
#     print("hello")
#     yield
#     print("\n'bye'")
@pytest.fixture(scope="session",autouse=True)
def test_init(base_url):
    global_map=GlobalMap()
    global_map.set("baseurl",base_url)
    env = re.search("(https://)(.*)(.ezone.work)",base_url).group(2)
    global_map.set("env",env)

# 第八十章_日志和报告---allure的失败截图附加
@pytest.hookimpl(tryfirst=True,hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    if report.failed:
        try:
            for context in item.funcargs['browser'].contexts:
                for page in context.pages:
                    if page.is_closed():
                        continue
                    bytes_png=page.screenshot(timeout=5000, full_page=True)
                    allure.attach(bytes_png,f"失败截图---{page.title()}")
        except:
            ...

# conftest.py配置浏览器窗口大小,配置录制视频的窗口大小,   pytest.init文件中 --video=on
# #启用视频录制功能，测试运行时会录制视频
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,# 保留原有配置
        "viewport": {# 设置浏览器视口大小
            "width": 1920,
            "height": 1080,
        },
        "record_video_size": {# 设置视频录制尺寸
            "width": 1920,
            "height": 1080,
        }
    }