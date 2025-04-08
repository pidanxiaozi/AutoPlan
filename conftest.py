import pytest


# @pytest.fixture()
# def hello1():
#     print("hello")
#     yield
#     print("\n'bye'")

# conftest.py配置浏览器窗口大小,配置录制视频的窗口大小,   pytest.init文件中 --video=on
# #启用视频录制功能，测试运行时会录制视频
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 800,
            "height": 800,
        },
        "record_video_size": {
            "width": 800,
            "height": 800,
        }
    }