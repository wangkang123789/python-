# 关于二维字典，以及如何根据输出结果来解决问题

今天有学到了心得数据结构，就是二维字典，以及如何根据输出结果来解决问题。
## 1、首先是二维字典
二维字典创建新的元素以及如何修改二维字典的数值，需要注意的是在判断元素是否在二维数组时，是需要判断的。
### 1.1 其中关于二维字典的插入数据，如何遍历
``` 
            # 如果单词不在二维字典中
            if file_word not in dictionary_word:
                dictionary_word[file_word] = {file_name: tf}
            # 如果单词在字典中，则把文件名追加到单词后面跟的列表中
            # 对每个单词字典的数据结构进行更改，加上一个该单词在某个文档中出现的频率。
            else:
                dictionary_word[file_word][file_name] = tf
```

## 2、关于如何把二维字典的纵向数据相加的方法
```
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
```
通过字典，用字典的关键字来相加纵向的数据，如果是横向的数据，则可以直接使用一个temp变量来求解。这里是用了根据结果来得出要求的字典的格式。

***扩展：这里如果求横向的和的话，也可以使用字典来相加，结果直接存到  字典[关键词] = 和  中，***
其意图就是将二维字典的某列值相加存到一个结果字典中，并且值得注意的是，中间判断了**文件名是否在字典中** 这个操作在字典的插入过程会一直出现，**务必牢记**

