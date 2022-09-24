# 函数的递归，计算累加结果

def sum_number(num):
    if num < 1:
        return 0
    sum = num + sum_number(num - 1)
    return sum

print(sum_number(3))