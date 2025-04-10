from playwright.sync_api import sync_playwright,Page,Browser,BrowserContext
# from module.BaiduPage import Baidu
# from module.登录页 import 登录页_类
import pytest
from filelock import FileLock
from utils.GetPath import get_path
from utils.globalMap import GlobalMap
from module.PageInstance import PageIns
from module.BasePage import PageObject
from playwright.sync_api import BrowserContext
from module import *
from data_module import my_data