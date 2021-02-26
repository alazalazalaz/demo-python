import peewee
from user_model import PyUser   # 此处引用的时候，pyuser类就会被执行
from rank_model import PyRank
from connect import db
import traceback

# 事物，
# peewee的事物成功后会自动commit，失败后会自动rollback
# 同一个事务里面，必须使用同一个db连接，可以把connect_db()做成单例

u = PyUser()
u.username = "allen.zhang26"

u1 = PyUser()
u1.username = "allen.zhang23"

print("connect instance from db:{}".format(db))


try:
    with db.atomic() as trx:
        u.save()  # 由于db,u和u1用的都是同一个db实例，所以事务ok
        u1.save()  # 这句会异常
except peewee.PeeweeException as ex:
    print("已捕获异常：{} ".format(ex))
    # print("trace route:{} ".format(traceback.print_exc()))    # 打印trace


# 这个事务是ok的
# db = get_db()
# db.connect()
# with db.transaction():
#     print(db.execute_sql("insert into py_user  (username) values ('allen.zhang17')"))  # 这句会异常
#     print(db.execute_sql("insert into py_user  (username) values ('allen.zhang')"))
# 这个事务是ok的
