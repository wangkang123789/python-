# my_list = []
# string = ""


# 对用户的信息进行修改


def modifyinfo(mydictionary):
    """修改用户的信息"""

    # 每次修改之前都判断是否需要修改厚
    print("1.确认修改\n2.不修改")
    if int(input("请根据提示是否修改姓名：")) == 1:
        mydictionary["姓名"] = input("请对用户的姓名进行修改，并输入新的姓名:")
    if int(input("请根据提示是否修改电话：")) == 1:
        mydictionary["电话"] = input("请对用户的电话进行修改，并输入新的电话:")
    if int(input("请根据提示是否修改QQ：")) == 1:
        mydictionary["QQ"] = input("请对用户的QQ进行修改，并输入新的QQ:")
    if int(input("请根据提示是否修改邮箱：")) == 1:
        mydictionary["邮箱"] = input("请对用户的邮箱进行修改，并输入新的邮箱:")



def my_find(my_list, string):
    """查询名片

    :param my_list: 需要查询的数据库
    :param string: 需要查询的姓名
    """
    for temp in my_list:
        if temp["姓名"] == string:
            print("找到了")
            print("*" * 50)
            print("%s\t\t" % temp["姓名"], end="")
            print("%s\t\t" % temp["电话"], end="")
            print("%s\t" % temp["QQ"], end="")
            print("\t%s" % temp["邮箱"])
            print("*" * 50)
            # 判断是否对该用户的信息进行修改

            # 修改的提示信息
            print("1.对该用户的信息进行修改\n2.对该用户的信息进行删除\n0.不处理，仅显示")
            info = int(input("请输入操作信息："))
            if info == 1:
                modifyinfo(temp)
                print("修改成功")
            elif info == 2:
                my_list.remove(temp)
                print("删除成功")
            else:
                print("只是查询，不做处理呐")
            break
    else:
        print("所找的姓名不在名片管理系统中")