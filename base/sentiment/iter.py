# 迭代器
# 迭代器可以访问python的集合元素
# 迭代器有两个基本方法，iter()和next()

myList = [1, 2, 3, 4]
it = iter(myList)     # 创建迭代器对象
for x in it:
    print(x, myList.index(x))   # 输出元素和索引

myDict = {}
myDict["one"] = "china"
myDict["two"] = "japan"
for x in iter(myDict):
    print(x, myDict[x])     # 输出索引和元素
