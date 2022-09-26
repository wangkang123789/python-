from operator import *

class Solution(object):
    def isPalindrome(self, x):

        str1 = str(x)
        list = []
        # 将字符串存入列表中
        for i in str1:
            list.append(i)

        # 将列表逆序
        list2 = list[::-1]
        # 这里的字符串以及元组都是不可修改的
        # while start < end:
        #     temp = str1[start]
        #     str1[start] = str1[end]
        #     str1[end] = temp
        #     start += 1
        #     end -= 1

        if list == list2:
            print("True")
        else:
            print("False")


if __name__ == "__main__":
    solution = Solution()
    solution.isPalindrome(121)