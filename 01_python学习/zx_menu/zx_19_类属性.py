class Tools:
    # 添加一个类属性，记录使用该类创建的对象数
    count = 0

    @classmethod
    def func(cls):
        pass

    def __init__(self, name):
        self.name = name
        Tools.count += 1


tools1 = Tools("锤子")
tools2 = Tools("水桶")
tools3 = Tools("斧头")

tools3.count = 99
print(Tools.count)
print(tools2.count)
print(tools3.count)