from user_model import PyUser

# 单条查询方法
# 其实有个get()方法，但是查询为空是会抛异常，所以不想用，get_or_none()查询为空返回None
data = PyUser.get_or_none(PyUser.username == 'allen.zha33ng')
if data:
    print("单条查询方法:{}".format(data.username))
else:
    print("单条查询方法:{}".format("None"))

# 多条查询
data_multi = PyUser.select().where(PyUser.email == "sf").order_by(PyUser.id.desc()).limit(3)
for data in data_multi:
    print("multi data:{}".format(data.username))

# in 查询
data_in = PyUser.select().where(PyUser.id.in_([1, 2]))
for data in data_in:
    print("in:{}".format(data.username))

# like 查询
data_in = PyUser.select().where(PyUser.username ** "%zhang5%")
for data in data_in:
    print("like:{}".format(data.username))

# 复合条件
# 注意复合中每个条件必须用()括起来，|表示or，&表示and
data_in = PyUser.select().where((PyUser.id == 1) | (PyUser.id == 2))
for data in data_in:
    print("复合:{}".format(data.username))