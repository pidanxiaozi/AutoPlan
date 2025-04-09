from playwright.sync_api import sync_playwright,Page,Browser,BrowserContext
# from module.BaiduPage import Baidu
# from module.登录页 import 登录页_类
import pytest
from filelock import FileLock
from utils.GetPath import get_path
from utils.globalMap import GlobalMap