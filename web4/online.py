class WebIndex:
    def __init__(self, dir_txt):
        file = open(dir_txt, "r")
        # 输入多个单词，并使用列表保存
        list_keyword = input('please input the keyword to search:').split()
        dict_online = eval(file.read())
        file.close()

        # 遍历单词，并从二维字典中找到对应的列
        ans={}
        for dw in list_keyword:
            if dw in dict_online:
                for txt_name in dict_online[dw]:
                    if txt_name in ans:
                        ans[txt_name] += dict_online[dw][txt_name]
                    else:
                        ans[txt_name] = dict_online[dw][txt_name]

        ans = sorted(ans.items(),key=lambda x: x[1],reverse = True)
        print(ans)




# 文件默认是按照从大到小来的


if __name__ == "__main__":
    web_index = WebIndex("C:/Users/wangk/Desktop/web3/offline.txt")

