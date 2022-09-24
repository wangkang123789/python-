# 循环计算1~100的数

# i = 1
# sum = 0
# while i <= 100:
#     sum += i
#     i += 1
# print("1~100的和是：%d" % sum)

# 循环计算0~100之间的偶数
i = 0
sum = 0
while i<= 100:
    if i % 2 == 0:
        sum += i
    i += 1
print("0~100之间的偶数之和是：%d" % sum)