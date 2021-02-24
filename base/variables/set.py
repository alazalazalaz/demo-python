# set集合
# 类似数组，基本功能是成员测试(判断元素是否存在集合)和删除重复元素

# 两种定义方式
websites = {"google", "baidu", "sina", "sina"}
print(websites)     # {'baidu', 'google', 'sina'} 重复的元素被自动过滤掉了
car = set("abccdeff")   # {'e', 'f', 'b', 'd', 'a', 'c'}
print(car)

# 判断
if 'baidu' in websites:
    print("baidu在集合中")  # baidu在集合中
else:
    print("baidu不在集合中")

# 两个集合运算
overseaWebsites = {"google", 'facebook'}
print(websites - overseaWebsites)   # {'baidu', 'sina'} 差集
print(websites | overseaWebsites)   # {'facebook', 'baidu', 'sina', 'google'} 并集
print(websites & overseaWebsites)   # {'google'} 交集
print(websites ^ overseaWebsites)   # {'sina', 'baidu', 'facebook'} 不同时存在于两者的成员

