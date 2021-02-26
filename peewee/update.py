from user_model import PyUser

# 一旦模型有主键后，后续调用save()等同于update()
data = PyUser.get(PyUser.username == 'allen.zhang')
data.email = "jjjj@qq.com"
print("update result : {}".format(data.save()))  # 返回受影响(整儿八九有更新哦)的条目数，否则返回0


# 多条更新
# 注意多条更新的时候，update()方法里面的字段不需要用实例，直接填字段=xxx
re = PyUser.update(email="fff@qq.com").where(PyUser.id >= 16).execute()
print("batch update result : {}".format(re))    # 返回受影响的条目数








