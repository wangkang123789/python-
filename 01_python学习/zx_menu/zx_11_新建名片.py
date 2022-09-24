# 用列表来存储名片，用字典来记录各用户的信息

# my_list = []
my_dictionary = {}

def add_card(my_list1):
    """该函数是用来增加用户的
    :return:最后返回的是传进来的列表
    """
    # 先添加用户的姓名
    my_name = input("请输入要增加用户的姓名：")
    my_dictionary["姓名"] = my_name

    # 再添加用户的电话号码
    my_phonenum = input("请输入用户的电话号码：")
    my_dictionary["电话"] = my_phonenum

    # 添加用户的QQ
    my_qq = input("请输入用户的QQ：")
    my_dictionary["QQ"] = my_qq

    # 添加用户的邮件
    my_email = input("请输入用户的邮箱:")
    my_dictionary["邮箱"] = my_email

    # 最后将存有用户信息的字典存入列表中
    my_list1.append(my_dictionary)  # 明明可以插入你报错干嘛？

    return my_list1
