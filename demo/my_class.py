class Human:
    def __init__(self, name, sex, age):
        self.name = name
        self.age = age
        self.sex = sex
        self.bbirthday = 2025 - age

    def run(self):
        print(f"{self.name} is running")

    def job(self):
        if self.age > 35:
            print(f"{self.name} 不好找工作了")
        elif self.age < 35:
            print(f"{self.name} 还能找到工作")
        else:
            print(f"{self.name} 你有无限可能")


class Tester(Human):
    def __init__(self, name, sex, age, tech):#Tester自己的属性
        super().__init__(name, sex, age)#Human的属性
        self.tech = tech

if __name__ == '__main__':
    zhang3 = Human(name="张三", sex="男", age=35)
    zhang3.run()
    zhang3.job()

    lisi=Tester(name="李四", sex="男", age=35, tech="python")
    lisi.run()
    lisi.job()
    print(lisi.tech)
    print(lisi.bbirthday)
