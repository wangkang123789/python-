import os
import string
punctuation_string = string.punctuation


def process():
    # 将目录下的文件名导入file_list列表
    file_list = os.listdir("C:/Users/wangk/Desktop/web2/data")
    dir_name = "C:/Users/wangk/Desktop/web2/data"
    dictionary_word = {}
    for file_name in file_list:
        file_path = dir_name + '/' + file_name
        file = open(file_path, "r")
        line = file.readline()

        # 对文件进行预处理
        line = line.lower()
        # 除去标点符号
        for i in punctuation_string:
            line = line.replace(i, '')
        # 将读取的内容以空格进行分割，然后以单词为单位进行匹配
        split_list = line.split(" ")

        # 删掉一个文档内重复的单词
        split_list = set(split_list)

        # 将单词存入字典
        for file_word in split_list:
            # 如果单词已在字典中
            if file_word not in dictionary_word:

                dictionary_word[file_word] = [file_name, ]
            # 如果单词不在字典中
            else:
                dictionary_word[file_word].append(file_name)
        # 关闭文件
        file.close()

    # 将字典写入offline.txt中
    offline = open("C:/Users/wangk/Desktop/web2/offline.txt", "w")
    offline.write(str(dictionary_word))
    offline.close()


process()
