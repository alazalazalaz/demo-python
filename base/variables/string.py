# 字符串截取(左闭右开)
# 正序截取从下标0开始(0,1,2...)，倒序截取从下标-1开始(...-3, -2, -1)
str = "allen.zhang"

print("1:" + str)          # allen.zhang
print("2:" + str[0:-1])    # allen.zhan (因为是左闭右开所以最后一个字母'g'没有被截取到)
print("3:" + str[0])       # a
print("4:" + str[2:5])     # len.
print("5:" + str[-5:])     # zhang
print("6:" + str * 2)      # allen.zhangallen.zhang
print("7:" + str + "test")  # allen.zhangtest

# 反斜杠转义，如果想用原始字符串，需要在前面加上r
print("alle\n.zhang")
print(r"allen\n.zhang")

# python的字符串内容不能被改变，比如str[0] = 'm'会报错，这点和c不同

# python的三引号可以跨多行写字符串
multStr = """这是一个
多行
的
实例"""
print(multStr)

