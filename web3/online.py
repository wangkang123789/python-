class WebIndex:
    def __init__(self, dir_txt):
        file = open(dir_txt, "r")
        key_word = input("please input the keyword to search:")
        dict_online = eval(file.read())
        file.close()
        list_len = len(dict_online[key_word])
        if key_word in dict_online:
            i = 0
            while i < list_len:
                print(dict_online[key_word][i])
                i += 1


# 文件默认是按照从大到小来的


if __name__ == "__main__":
    web_index = WebIndex("C:/Users/wangk/Desktop/web3/offline.txt")

