# 导入随机数的工具包
import random

# 输入要出的拳
player = int(input("请出拳：石头（1）、剪刀（2）、布（3）"))

# 电脑随机出拳
computer = random.randint(1,3)

print("电脑出的%d" % computer)
# # 当玩家出石头时
# if player == 1:
#     if computer == 1:
#         print("平局")
#     elif computer == 2:
#         print("电脑输了")
#     elif computer == 3:
#         print("我输了")
#     else:
#         print("程序出错")
#
# # 当玩家出剪刀时
# elif player == 2:
#     if computer == 1:
#         print("我输了")
#     elif computer == 2:
#         print("平局")
#     elif computer == 3:
#         print("电脑输了")
#     else:
#         print("程序出错")
#
# # 当玩家出布时
# elif player == 3:
#     if computer == 1:
#         print("电脑输了")
#     elif computer == 2:
#         print("我输了")
#     elif computer == 3:
#         print("平局")
#     else:
#         print("程序出错")
#
# else:
#     print("出拳错误，请重新出拳")

# 还可以使用
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 2)):
    print("玩家赢了。")