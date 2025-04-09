class MYData:
    """
    53章
    登录的封装 - 你的测试数据应该放在哪?
    """
    def __init__(self, local=True, excel=None, yaml=None, feishu=None):
        self.local = local
        self.excel = excel
        self.yaml = yaml
        self.feishu = feishu

    def userinfo(self):
        user = ""
        if self.excel:
            pass
            # todo 把excel转换成字典的方法
        elif self.yaml:
            pass
            # todo 把yaml转换成字典的方法
        elif self.feishu:
            pass
            # todo 把feishu转换成字典的方法
        else:
            user = {"playwright": {"测试员": {
                        "username": "admin",
                        "password": "123456",
                        "email": "admin@163.com",
                        "phone": "12345678901",
                        "address": "北京",
                    }
                }
            }
        return user
