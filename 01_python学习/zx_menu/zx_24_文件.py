# # 打开文件
# file = open("hello.txt", encoding='utf-8')  # 如果要读取中文的话后面要加encoding='utf-8'
#
# # 读取文件内容
# text = file.read()
# print(text)
#
# print("%" * 50)
#
# text = file.read()
# print(text)
#
# # 关闭文件
# file.close()


# 文件复制
# file_sour = open("hello.txt", "r", encoding='utf-8')
# file_dest = open("dest.txt", "w", encoding='utf-8')  # 这里的读写都需要加enconding=utf-8
#
# text = file_sour.read()
# file_dest.write(text)
#
# file_dest.close()
# file_sour.close()


# 大文件复制
file_sour = open("hello.txt", "r", encoding='utf-8')
file_dest = open("dest.txt", "w", encoding='utf-8')

text = file_sour.readline()
while True:
    if not text:
        break
    file_dest.write(text)
    text = file_sour.readline()

file_dest.close()
file_sour.close()