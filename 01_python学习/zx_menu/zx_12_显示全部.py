# my_list = []


def printall(my_list):
    """打印全部"""

    # 先打印标题栏
    print("姓名\t\t电话\t\tQQ\t\t邮箱")
    print("*" * 50)
    for temp in my_list:
        print("%s\t\t" % temp["姓名"], end="")
        print("%s\t\t" % temp["电话"], end="")
        print("%s\t" % temp["QQ"], end="")
        print("\t%s" % temp["邮箱"])
        print("*" * 50)