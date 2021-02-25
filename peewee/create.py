import peewee
from user_model import Py_User

# 单条插入
u = Py_User()
u.username = "allen.zhang"
u.email = "ss@qq.com"
print(u.save())     # 1 返回插入的条目数

# 批量插入
# @todo

