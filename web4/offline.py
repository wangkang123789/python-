import os
import string
import math
punctuation_string = string.punctuation


def process():
    # 将目录下的文件名导入file_list列表
    file_list = os.listdir("C:/Users/wangk/Desktop/web3/data")
    dir_name = "C:/Users/wangk/Desktop/web3/data"
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

        # 可以用一个列表记录以前分隔完，但是没去重的单词列表，然后用去重完后的列表来统计单词在该文档中出现的次数
        total_list = split_list
        # 删掉一个文档内重复的单词
        split_list = set(split_list)

        # 将单词存入字典
        for file_word in split_list:
            # 首先计算该单词在该文档中的tf
            tf = math.log10(total_list.count(file_word)*100/len(total_list)+1)

            # 如果单词不在字典中
            if file_word not in dictionary_word:
                dictionary_word[file_word] = {file_name: tf}
            # 如果单词在字典中，则把文件名追加到单词后面跟的列表中
            # 对每个单词字典的数据结构进行更改，加上一个该单词在某个文档中出现的频率。
            else:
                dictionary_word[file_word][file_name] = tf

        # 关闭文件
        file.close()

    n = len(file_list)
    # 计算idf，即将写好的字典遍历一遍
    for dw in dictionary_word:
        # 计算每个单词的idf
        idf = math.log10((1+n)/len(dictionary_word[dw]))
        # 修改每个单词的对应文档的权值
        for dic_txt in dictionary_word[dw]:
            dictionary_word[dw][dic_txt] *= idf




    # 将字典写入offline.txt中
    offline = open("C:/Users/wangk/Desktop/web3/offline.txt", "w")
    offline.write(str(dictionary_word))
    offline.close()


process()
