# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         end = len(nums)-1
#         i = 0
#         j = 0
#         while i < end+1:
#             j = i+1
#             while j < end+1:
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#                 j += 1
#             i += 1


# # 算法改进
# # 使用python中的字典数据结构来进行写
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         # 首先创建一个返回的列表和一个用来存储的字典
#         result_list = []
#         dict_nums = {}
#
#         # 将形参列表的元素全部存入字典当中，其中的key是原列表的值，value是对应的索引，但是用字典的话会导致key值相同的时候会覆盖前面的键值对
#         # 所以这里要使用enumerate
#         for i, num in enumerate(nums):
#             dict_nums[num] = i
#
#         # 然后使用遍历判断两数之和,ps:只有字典才有count的方法
#         for i, temp in enumerate(nums):
#             if dict_nums.get(target-temp) != i:
#                 # if nums.index(target-temp) != nums.index(temp):，首先这行代码不会执行，因为你index是向左边开始搜寻的，所以搜到第一个就直接停止了，不会继续搜寻
#                 # print(nums.count(target - temp))
#                 result_list.append(nums.index(temp))
#                 result_list.append(dict_nums.get(target-temp))
#                 return result_list
#
#         else:
#             return


# 自己代码优化
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 首先创建一个返回的列表和一个用来存储的字典
        result_list = []
        dict_nums = {}

        # 将形参列表的元素全部存入字典当中，其中的key是原列表的值，value是对应的索引
        for i, num in enumerate(nums):
            dict_nums[num] = i

        # 然后使用遍历判断两数之和,ps:只有字典才有count的方法
        for dict_temp in dict_nums:
            if dict_nums.get(target - dict_temp) > 0 and dict_nums[target - dict_temp] != nums.index(dict_temp):
                result_list.append(nums.index(dict_temp))
                result_list.append(dict_nums[target - dict_temp])
                return result_list

        else:
            return


if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([3, 4, 8], 11))
