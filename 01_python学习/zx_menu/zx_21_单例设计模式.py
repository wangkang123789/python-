# 单例设计模式就是使该类实例的对象永远只有一个
class Music(object):
    # 使用一个类属性来记录当前的对象
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance

    def __init__(self, name):
        self.name = name

    @staticmethod
    def print_yes():
        print("hahahaha")


# 创建对象
wang = Music("网易云")
print(wang.name)
print(wang)

QQ = Music("QQ音乐")
print(QQ.name)
print(wang.name)
print(QQ)
print(wang)
wang.print_yes()

# 总结：单例的本质就是内存地址不变，即只存在一个对象，但是对象的实例属性其实是可以更改的，所以就是单例
