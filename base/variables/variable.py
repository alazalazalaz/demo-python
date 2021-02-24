# 变量
# python中变量就是变量，没有具体的类型，直接使用=赋值

num = 100   # int
miles = 100.0 # float
name = "xiao.ming" #string

print(num)
print(miles)
print(name)

a, b, c = 1, 2, "bird"
print(a, b, c)

# 将一个变量转为整数
v1 = 1.23
v2 = '0xa'

print(int(v1), int(v2, 16))     # 1 10 (因为0xa是十六进制，所以int()函数第二个参数填16)

