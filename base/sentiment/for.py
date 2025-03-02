# for 语句

# 可以遍历任何有序数据，list set等, dict不是有序的哦
myList = ['china', 'japan', 'USA']
for i in myList:    # 这里的i是value不是下标key哦
    print(i)
    if i == 'japan':
        break


# 还可用来遍历普通范围，配合range使用
print("=======range=======")
for i in range(5):
    print(i)    # 0到5

print("=======range=======")
for i in range(1, 3):
    print(i)    # 1到2，左闭右开

print("=======range=======")
for i in range(1, 100, 10):
    print(i)    # 1开始，每次循环i=i+10，所以结果是1 11 21 ...91
