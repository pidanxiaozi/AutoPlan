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
from data_module import auth_data
from allure import severity as 用例级别,step as 测试步骤,title as 用例名称,description as 用例描述
from allure_commons.types import Severity
阻塞=Severity.BLOCKER
严重=Severity.CRITICAL
普通=Severity.NORMAL
不重要=Severity.TRIVIAL
轻微=Severity.MINOR
