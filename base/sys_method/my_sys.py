import sys
import os


# 接受main函数的参数
# python3.8 my_sys.py -airline=xiangpeng -date=2021-01-01
# my_sys.py     # 第一个参数是该执行文件名哦
# -airline=xiangpeng
# -date=2021-01-01
from second.my_sys2 import file_path

for arg in sys.argv:
    print(arg)


# 获取文件路径
# sys.argv[0]和__file__都能获取当前文件的相对路径，区别是前者获取的是入口文件的路径，后者是当前执行代码文件的路径。
print(os.path.realpath(sys.argv[0]))  # 获取文件路径绝对地址
print(os.path.realpath(__file__))

file_path()

print(os.path.dirname(os.path.realpath(__file__)))  # 文件夹目录
