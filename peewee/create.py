import peewee
from user_model import PyUser

# 单条插入
u = PyUser()
u.username = "allen.zhang16"
u.email = "ss@qq.com"
print("save result : {}".format(u.save()))     # 1 返回插入的条目数

# 批量插入
data = []
for i in range(10):
    tmp_user = {
        "username": "allen.zhang{}".format(i),
        "email": "batch"
    }
    data.append(tmp_user)

print(u.insert_many(data).execute())    # 10 返回插入的总条目数




