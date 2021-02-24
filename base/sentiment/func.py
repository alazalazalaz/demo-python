# 函数

# def 函数名(参数列表):
#     函数体

def hello():
    print("hello")


hello()


def plus(a, b=4):
    print(a + b)


plus(1)


# 不定长参数,使用*，表示以元祖的形式加入，不同于go的省略号func test(arg1 string, argMore ...string)
def func_param(arg1, *var_tuple):
    print(arg1)
    print(var_tuple)


func_param(1, 2, 3, 4)


# 匿名函数
# 使用关键字lambda来创建，而不使用def，lambda只是一个表达式，不是代码块，只能封装有限的逻辑进去
# func_name = lambda [arg1 [,arg2,.....argn]]:expression

sum_func = lambda a, b: a + b
print(sum_func(10, 20))

