# 列表
# 列表关于切片截取和string类似，也是左闭右开，0头下标-1尾下标

myList = ['abc', 123, 2.3, "allen.zhang"]
tinyList = [123, "allen.zhang"]

print(myList)       # ['abc', 123, 2.3, "allen.zhang"]
print(myList[0])    # abc
print(myList[1:3])  # [123, 2.3]
print(myList + tinyList)    # ['abc', 123, 2.3, 'allen.zhang', 123, 'allen.zhang']

# 新增元素
myList.append("appendString")
print(myList)   # ['abc', 123, 2.3, 'allen.zhang', 'appendString']
myList.pop()
print(myList)   # ['abc', 123, 2.3, 'allen.zhang']

# 删除元素
del myList[0]
print(myList)   # [123, 2.3, 'allen.zhang']

# 嵌套列表
c = [myList, tinyList]
print(c)        # [[123, 2.3, 'allen.zhang'], [123, 'allen.zhang']] 二维啦

# 系统函数
calList = [1, 5, 2, 9]
print(len(calList))     # 4
print(max(calList))     # 9 返回列表最大值，注意如果有元素是非int会报错哦
print(min(calList))     # 1

calList.reverse()
print(calList)      # [9, 2, 5, 1] 反转
calList.sort()
print(calList)      # [1, 2, 5, 9] 正序 (正序后再反转即可实现逆序)

# for 循环获取索引
# for key, arg in enumerate(sys.argv):
    # print(key, arg)
for key, v in  enumerate(calList): #使用enumerate()函数来循环数组
    print(key, v)


# 其他函数
# 1	list.append(obj)
# 在列表末尾添加新的对象
# 2	list.count(obj)
# 统计某个元素在列表中出现的次数
# 3	list.extend(seq)
# 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# 4	list.index(obj)
# 从列表中找出某个值第一个匹配项的索引位置
# 5	list.insert(index, obj)
# 将对象插入列表
# 6	list.pop([index=-1])
# 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
# 7	list.remove(obj)
# 移除列表中某个值的第一个匹配项
# 8	list.reverse()
# 反向列表中元素
# 9	list.sort( key=None, reverse=False)
# 对原列表进行排序 Sort the list in ascending order and return None.
# 10	list.clear()
# 清空列表
# 11	list.copy()
# 复制列表
