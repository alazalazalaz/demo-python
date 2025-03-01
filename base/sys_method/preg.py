# preg 正则
import re

print("============= re.match() =================")
# re.match()
# 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none
# result = re.match(pattern, string, flags) # pattern表达式，string字符串，flags标志(是否大小写多行匹配这些)
# 与php不同，re.match()如果匹配成功，返回的是一个对象，失败返回None
# 如果匹配成功，可使用result.group(num)或result.groups()来获取结果
re1 = re.match("baidu", "www.baidu.com")
print(re1)  # None

re2 = re.match("www", "www.baidu.com")
if re2:
    print(re2)  # <re.Match object; span=(0, 3), match='www'>对象
    print(re2.group(0))  # www
    # print(re2.group(1))     # 这样会报IndexError错哟，因为只匹配到一个www


print("============= re.search() =================")
# re.search()
# 扫描整个字符串并返回第一个成功的匹配
# result = re.search(pattern, string, flags=0) 参数同上
# result返回同上，是一个对象，用group(index)来获取结果
rs1 = re.search("baidu", "www.baidu.com")
if rs1:
    print(rs1)
    print(rs1.group(0))     # baidu
    print(rs1.span())     # (4, 9) 这个应该是返回的位置左闭右开

# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符相当于\s\S
# (.*?) 表示"非贪婪"模式，只保存第一个匹配到的子串
rs2 = re.search(r'(.*) bb (.*?) (.*) .*', " aa bb cc dd ee ff", re.I)   # 注意那个r是后面的字符串不要转移的意思哦，详见variables/common_string.py
if rs2:
    print(rs2)
    print(rs2.group(0))     # aa bb cc dd ee ff
    print(rs2.group(1))     # aa 第一个(.*)匹配出来的
    print(rs2.group(2))     # cc (.*?)匹配出来的，.*?表示非贪婪，有就走
    print(rs2.group(3))     # dd ee 第二个(.*)匹配出来的，一直贪婪，直到最后一个ff被最后一个.*匹配到

# re.match()和re.search()的区别在于，match是从第一个字符开始匹配，search是整个字符串搜索


print("============= re.compile() =================")
# re.compile()
# 用于生产正则表达式，供re.search()和re.match()使用。
# re.compile(pattern, flags)
# 上面的例子可以修改为如下
sss = "aa bb cc dd ee ff"
preg = re.compile(r'(.*) bb (.*?) (.*) .*', re.I)
startIndex = 0
endIndex = len(sss)
rsc2 = preg.search(sss, startIndex, endIndex)    # 这个search函数和上面的一样，后两个参数可选
if rsc2:
    print(rs2)
    print(rs2.group(0))     # aa bb cc dd ee ff
    print(rs2.group(1))     # aa 第一个(.*)匹配出来的
    print(rs2.group(2))     # cc (.*?)匹配出来的，.*?表示非贪婪，有就走
    print(rs2.group(3))     # dd ee 第二个(.*)匹配出来的，一直贪婪，直到最后一个ff被最后一个.*匹配到


print("============= re.findall() =================")
# re.findall()
# 查找字符串中满足表达式的子串，并放到一个数组里，
# 注意match()和search()只是按照表达式查找一次，findall()是查找所有满足表达式的
string1 = "my num is 11,my phone is 22"
preg1 = re.compile("\d+")   #\d只是一个数字，\d+表示一个或者多个
reall1 = preg1.findall(string1)
print(reall1)   # ['11', '22']


print("============= re.sub() =================")
# re.sub()
# 检索和替换
# @param pattern模式， repl替换的内容可以为函数, string匹配的字符串， count替换的最大次数默认所有, flag
# res1 = re.sub(pattern, repl, string, count, flag)
res1 = re.sub("\D", "", "136 1234 5678")  # 替换非数字为空，\d是数字\D是非数字
print("sub替换结果：", res1)     # 13612345678




