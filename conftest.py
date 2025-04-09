import pytest

from utils.globalMap import GlobalMap


# @pytest.fixture()
# def hello1():
#     print("hello")
#     yield
#     print("\n'bye'")
@pytest.fixture(autouse=True,scope="session")
def test_init(base_url):
    global_map=GlobalMap()
    global_map.set("baseurl",base_url)




# conftest.py配置浏览器窗口大小,配置录制视频的窗口大小,   pytest.init文件中 --video=on
# #启用视频录制功能，测试运行时会录制视频
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
        "record_video_size": {
            "width": 1920,
            "height": 1080,
        }
    }