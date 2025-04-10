"""
  53章
  登录的封装 - 你的测试数据应该放在哪?
"""
class MYData:

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
            user = { "pidanxiaozi":{
                        "测试员1":{"username": "pidanxiaozi","password": "weijuhong581"},
                        "项目经理1":{"username": "winni","password": "playwright001"}}
                    }

        return user
