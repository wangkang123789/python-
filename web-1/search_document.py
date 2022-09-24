import os
import string

punctuation_string = string.punctuation

# 将目录下的文件名导入file_list列表
file_list = os.listdir("C:/Users/wangk/Desktop/web/doctxt")

# 记录需要检索的文件夹的目录
dir_name = "C:/Users/wangk/Desktop/web/doctxt"

# 输入关键字
key_word = input("Please input the keyword to search：")

flag = True
# 获取文件的完整路径并打开该文件

for file_name in file_list:
    # 路径拼接
    file_path = dir_name + '/' + file_name
    file = open(file_path, "r")
    line = file.readline()
    line = line.lower()

    # 除去标点符号
    for i in punctuation_string:
        line = line.replace(i, '')

    # 将读取的内容以空格进行分割，然后以单词为单位进行匹配
    split_list = line.split(" ")
    # 判断关键字是否在当前检索文件内
    for split_key in split_list:
        if key_word == split_key:
            flag = False
            print (os.path.basename(file_path))
            print(line)

    # 关闭文件
    file.close()

if flag :
    print("该关键字不在以上任何文本文件中")
