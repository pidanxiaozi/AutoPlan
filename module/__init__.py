from playwright.sync_api import sync_playwright,Page,expect,BrowserContext
from module.BaiduPage import Baidu
from module.登录页 import 登录页_类
from module.我的任务 import 我的任务_类
from module.项目集 import 项目集_类
from  module.BasePage import PageObject
from data_module.auth_data import MYData
from utils.globalMap import GlobalMap
from utils.GetPath import get_path
from module.PageInstance import PageIns
import os
from module.table import Table