"""
第五十一章_登录的封装-一个临时的数据库-GlobalMap
"""
class GlobalMap:
    my_dict = {}
    def set(self,key,value):
        self.my_dict[key] = value
    def get(self,key):
        return self.my_dict.get(key)
    def delete(self,key):
        self.my_dict.pop(key)