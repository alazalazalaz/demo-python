# for 语句

# 可以遍历任何有序数据，list set等, dict不是有序的哦
myList = ['china', 'japan', 'USA']
for i in myList:    # 这里的i是value不是下标key哦
    print(i)
    if i == 'japan':
        break


# 还可用来遍历普通范围，配合range使用
for i in range(5):
    print(i)

for i in range(1, 3):
    print(i)