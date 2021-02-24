# 关于异常处理

# python和php类似一般有两种错误，一个是语法错误，一个是异常
# 语法错误很容易检测，编译的时候会失败并提示
# 异常就是运行的时候会报出来，并且中断程序

# print(10/0) 这样会触发一个异常()
# 解决方案
try:
    print(10/0)
except ZeroDivisionError:   # 注意这个ZeroDivisionError，此方法中只能用这个error，如果用其他error会捕获不到
    print("ZeroDivisionError捕获了除数不能为0的情况")

# try:
#     print(10/0)
# except NameError:
#     print("NameError没法捕获除数不能为0的情况")

# raise可以抛出exception
