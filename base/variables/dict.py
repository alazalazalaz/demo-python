# dictionary 字典
# 和其他语言一样，是一个无序的key value集合， key必须唯一哦

# 定义
nameDict = {}
nameDict['one'] = "allen.zhang"
nameDict[2] = "xiaoming"
nameDict[2] = "xiaoming2"   # 会覆盖之前的key

tinyDict = {'name': 'allen.zhang', 'age': 18}   # 注意冒号后面有空格

print(nameDict)
print(tinyDict)
print(nameDict[2])      # xiaoming2
print(nameDict.keys())  # dict_keys(['one', 2])
print(nameDict.values())    # dict_values(['allen.zhang', 'xiaoming2'])

for key, value in tinyDict.items(): # 使用 dic.items()来进行循环
    print(key, value)
