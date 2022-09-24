# 类


# class Cat:
#
#     def eat(self):
#         print("小猫爱吃鱼")
#
#     def drink(self):
#         print("小猫爱喝水")
#
#
# jerry = Cat()
# jerry.eat()
# jerry.drink()
# print(jerry)


# 封装

class Person:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "%s的体重是%.2f" % (self.name, self.weight)

    def run(self):
        self.weight -= 0.5

    def eat(self):
        self.weight += 1.0


# xiaoming = Person("小明", 75)
# xiaohong = Person("小红", 55)
#
# print(xiaoming)
# print(xiaohong)
#
# xiaoming.run()
# xiaohong.eat()
#
# print(xiaoming)
# print(xiaohong)


# 摆放家具
class HouseItem:   # 类名得是大驼峰

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "%s占地%.1f平米" % (self.name, self.area)


class House:

    def __init__(self, style, square):
        self.style = style
        self.square = square
        self.item_list = []  # 创建一个家具名称列表，ps：是一个空的列表
        self.free_area = square

    def add_item(self, item):

        # 要先判断添加的家具是否大于房子的剩余面积
        if self.free_area < item.area:
            print("家具太大，房子放不下了")
            return
        
        self.item_list.append(item.name)
        # 这里的item可以是一个对象吧，就是一个家具的对象。漏，大漏特漏！
        # //过来人告诉你！这里只是添加了对象的名字，如果是添加整对象的话，最后print是无法正常打印的，只能打印对象是谁创建的，以及对象的地址！
        self.free_area -= item.area

    def __str__(self):
        return "户型是%s、总面积是%.1f、剩余面积是%.1f、家具名称列表有%s" \
               % (self.style, self.square, self.free_area,
                  self.item_list)


# 创建家具对象
bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)

# 创建房子
my_house = House("小别墅", 180)

# 将家具放入房子
my_house.add_item(bed)
my_house.add_item(chest)
my_house.add_item(table)

# 打印房子
print(my_house)