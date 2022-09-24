# Dog类
class Dog:
    def __init__(self, name):
        self.name = name

    def shout(self):
        print("%s 在乱吠" % self.name)


class XiaoTianQuan:
    def __init__(self, name):
        self.name = name

    def shout(self):
        print("%s 在神吠" % self.name)


class Person:
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s 在与 %s 一起玩呢" % (self.name, dog.name))
        dog.shout()


xiao_ming = Person("小明")
xiao_tian_quan = XiaoTianQuan("哮天犬")
xiao_ming.game_with_dog(xiao_tian_quan)