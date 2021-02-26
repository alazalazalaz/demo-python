import peewee
import random

db_name = "test"
db = peewee.MySQLDatabase(db_name, host='127.0.0.1', port=3306, user='root', passwd='123456', charset='utf8')
if db.is_closed():
    db.connect()


class BaseModel(peewee.Model):
    print("x")
    # class Meta:
    #     database = get_db()
    #     database.connect()
    #     print("connect instance : {}".format(database))


if __name__ == '__main__':
    print("is closed:{}".format(db.is_closed()))
    print("connect1 result : {} instance : {}".format(db.connect(), db))
    print("is closed:{}".format(db.is_closed()))
    print("connect2 result : {} instance : {}".format(db.connect(), db))





