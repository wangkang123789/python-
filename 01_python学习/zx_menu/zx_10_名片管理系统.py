import zx_11_新建名片
import zx_12_显示全部
import zx_13_查询名片
# 开头的菜单
print("*" * 50)
print("欢迎使用【名片管理系统】V1.0\n")
print("1.新建名片")
print("2.显示全部")
print("3.查询名片\n")

print("0.退出系统")
print("*" * 50)

# 新建一个列表来存储用户的名片
card_list = []

# 让用户根据提示输入自己需要的功能
info = 1

while info == 1:
    temp = int(input("请输入需要使用的功能：")) # 我他么醉了，真是无语住了
    if temp == 0:
        print("退出系统")
        info = 0
        break
    elif temp == 1:
        print("新建名片ing....")
        zx_11_新建名片.add_card(card_list)
    elif temp == 2:
        print("显示全部ing...")
        zx_12_显示全部.printall(card_list)
    elif temp == 3:
        print("查询名片ing...")
        name = input("请输入要查找的姓名：")
        zx_13_查询名片.my_find(card_list, name)
        zx_12_显示全部.printall(card_list)
    else:
        print("输入的功能错误，请重新输入功能")