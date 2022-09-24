# # 列表，对应cpp中的数组
# my_list = ["刘明", "张华", "笑死"]
# print(my_list)
# print(my_list[0])
#
# my_list.remove("刘明")
# my_list.pop(0)
# print(my_list)
#
# # 元组，即无法修改的列表，且内部的数据无法修改，只能做的就是遍历和统计个数
# my_tuple = (1, 2, 5, "liuming", 8)
#
# for i in my_tuple:
#     print(i)
#
# print("元素2放在第%d位" % (my_tuple.index(2)+1))


# 字典，与cpp中的map很像，有键值的观念，key值是不可以重复的！！
# my_dictionary = {"姓名": "小芳",
#                  "年龄": 18,
#                  "性别": "女"}
#
# print(my_dictionary)
#
# print(my_dictionary["姓名"])
# my_dictionary["年龄"] = 20
# my_dictionary["婚否"] = "未婚"
# # my_dictionary.pop("姓名")
# print(my_dictionary)
# print(my_dictionary.keys())
# print(my_dictionary.values())
# print(my_dictionary.items())


# 字符串的定义

# my_str = "我的外号是\"大帅哥\"嘻嘻"
#
# for char in my_str:
#     print(char)

# my_str = "   \t \n \r "
# print(my_str.isspace())
#
#
# my_str1 = "wang kangshuai"
# print(my_str1)
# print(my_str1.rfind("shuai", 0, 8))
# print(my_str1.find("shuai", 0, 15))
# print(my_str1.replace("g", "m", 1))  # 注意replace替换后会生成一个新的字符串，而且不会更改原来的字符串，后面的1是指只替换一次的意思。默认是全部替换。
# print(my_str1)

# 关于字符串的居中对齐的设置
poem = ["I feel good",
        "I feel sad",
        "I feel bad",
        "I feel nice"]

poem2 = ["\t打发大水\n",
        "阿梵蒂冈",
        "爱的噶的",
        "阿萨德刚第三"]

# for poem_str in poem:
#     print("|%s|" % poem_str.center(15, "*"))

# str3 = "nimeshiba meishijichi liuliumei"
# mylist2 = str3.split()
# print(mylist2)
#
# str4 =  "\r".join(mylist2)
# print(str4)


# for poem_str in poem2:
#     print("|%s|" % poem_str.strip().center(15, "　"))


# 字符串的逆序
# str = "0123456789"
# result_str = ""
# j = len(str)
# print(str[-1::-2])
# print(str[0::3])


