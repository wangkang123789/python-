class WebIndex:
    def __init__(self, dir_txt):
        file = open(dir_txt, "r")
        key_word = input("please input the keyword to search:")
        dict_online = eval(file.read())
        file.close()
        if key_word in dict_online:
            i = 0
            list_len = len(dict_online[key_word])
            while i < list_len:
                print(dict_online[key_word][i])
                i += 1


if __name__ == "__main__":
    web_index = WebIndex("C:/Users/wangk/Desktop/web2/offline.txt")
