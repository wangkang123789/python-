# 枪类
class Gun:

    def __init__(self, model):
        self.model = model
        self.bullet = 10

    def shoot(self):
        self.bullet -= 1

    def add_bullet(self, count):
        # 子弹的上限是50颗
        self.bullet += count
        if self.bullet > 50:
            print("子弹已经装满了")
            self.bullet = 50
            return

    def __str__(self):
        return "%s还有%d颗子弹" % (self.model, self.bullet)


class Soldier:

    def __init__(self, name):
        self.name = name
        self.gun = None  # None可以赋值给任何变量

    def fire(self):

        # 先判断是不是有枪
        if self.gun is None:
            print("我还没枪呢")
            return

        if self.gun.bullet < 1:
            print("枪里没子弹啦，请及时补充弹药哟")
            self.gun.add_bullet(int(input("请输入要补充的弹药数量，最多补充50颗>>")))
        self.gun.shoot()
        print("射击成功")

    def __str__(self):
        return "士兵 %s 有一把 %s 子弹数为 %d" % (self.name, self.gun.model, self.gun.bullet)


# 创建枪
gun_AK47 = Gun("AK47")

# 创建士兵
my_soldier = Soldier("许三多")
my_soldier.gun = gun_AK47
i = 1
while i < 12:
    my_soldier.fire()
    i += 1
