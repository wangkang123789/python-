# 打印小星星，方法一
# star = "*"
# i = 0
# while i < 5:
#     print(star)
#     star += "*"  # 这里也可以直接使用print("*" * i),然后将i的初值设为1
#     i += 1

# # # 打印小星星，方法二
# i = 0
# j = 0
# while i < 5:
#     j = 0
#     while j <= i:
#         print("*", end="")
#         j += 1
#     print("")   # 我救命，直接一个print就是一个换行，不需要加\n
#     i += 1


def multiple_table():
    """九九乘法表的打印"""

    row = 1
    col = 1
    while row <= 9:
        col = 1
        while col <= row:
            print("%d * %d = %d\t" % (col, row, col * row), end="")
            col += 1
        print("")
        row += 1


multiple_table()

# # 显示倒计时
# import time
# for i in range(10):
#     print("\r离程序退出还剩%s秒" % (9-i), end="")  # \r的功能就是将光标的位置回退到本行的开头位置
#     time.sleep(1)
