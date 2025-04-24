import time
"""
 第六十八章 表单的封装~数据类的创建
 一个用于将对象属性转换为字典的类，支持对特定属性值进行特殊处理。
 """
class As_dict:
    """
        将对象的属性转换为字典，并对特定属性值进行处理。

        返回值:
            dict: 包含对象属性的字典。空字符串的属性会被移除，包含"时间戳"的属性值会被替换为当前时间戳。
    """
    def as_dict(self):
        # # 获取对象的属性字典
        # return_dict = self.__dict__
        # # 创建属性字典的副本，用于遍历和修改
        # temp_dict = self.__dict__.copy()
        # # 遍历属性字典的副本
        # for key, value in temp_dict.items():
        #     # 如果属性值为空字符串，则从返回字典中移除该属性
        #     if value == "":
        #         return_dict.pop(key)
        #         continue
        #     # 如果属性值包含"时间戳"，则将其替换为当前时间戳
        #     if "时间戳" in value:
        #         value = str(value).replace("时间戳", str(time.time_ns()))
        #         return_dict.update({key: value})
        # # 返回处理后的属性字典
        # return return_dict

        # 获取对象的属性字典
        return_dict = self.__dict__
        # 创建属性字典的副本，用于遍历和修改
        temp_dict = self.__dict__.copy()
        # 遍历属性字典的副本
        for key, value in temp_dict.items():
            # 如果属性值包含"时间戳"，则将其替换为当前时间戳
            if "时间戳" in value:
                value = str(value).replace("时间戳", str(time.time_ns()))
                return_dict.update({key: value})
        # 返回处理后的属性字典
        return return_dict
