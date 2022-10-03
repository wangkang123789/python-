# 每次比较两个列表，然后返回比较后的结果
def compare_two(list_one, list_two):
    answer_list1 = []
    len_list1 = len(list_one)
    len_list2 = len(list_two)

    l1 = 0
    l2 = 0

    while l1 < len_list1 and l2 < len_list2:
        if list_one[l1] == list_two[l2]:
            answer_list1.append(list_one[l1])
            l1 += 1
            l2 += 1

        else:
            if list_one[l1] < list_two[l2]:
                l1 += 1
            else:
                l2 += 1

    return answer_list1


class WebIndex:
    def __init__(self, dir_txt):
        file = open(dir_txt, "r")

        # 输入两个单词，并使用列表保存
        list_keyword = input('please input the keyword to search:').split()

        # key_word = input("please input the keyword to search:")
        dict_online = eval(file.read())
        file.close()

        # 先把字典中的多个单词的列表单独找出来
        list_temp = []
        for key_word in list_keyword:
            # 用map_temp来接收所查询单词的列表
            list_temp.append(dict_online[key_word])

        # 用来记录最后的输出列表
        answer_list = []



        # 然后遍历多个单词所在的列表，查找出相同的
        list_result = compare_two(list_temp[0], list_temp[1])

        for i in range(2, len(list_temp)):
            list_result = compare_two(list_result, list_temp[i])

        print(list_result)


if __name__ == "__main__":
    web_index = WebIndex("C:/Users/wangk/Desktop/web3/offline.txt")


        # 查询两个单词的方法
        # list1 = map_temp[list_keyword[0]]
        # list2 = map_temp[list_keyword[1]]
        #
        # len_list1 = len(list1)
        # len_list2 = len(list2)
        #
        # l1 = 0
        # l2 = 0
        #
        # while l1 < len_list1 and l2 < len_list2:
        #     if list1[l1] == list2[l2]:
        #         answer_list.append(list1[l1])
        #         l1 += 1
        #         l2 += 1
        #
        #     else:
        #         if list1[l1] < list2[l2]:
        #             l1 += 1
        #         else:
        #             l2 += 1
        #
        # print(answer_list)



# 文件默认是按照从大到小来的


