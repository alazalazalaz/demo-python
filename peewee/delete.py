from user_model import PyUser

# 删除

# 单条删除
u = PyUser.get(PyUser.username == "allen.zhang2")
print("delete result:{}".format(u.delete_instance()))   # 删除成功返回受影响的条目数，
