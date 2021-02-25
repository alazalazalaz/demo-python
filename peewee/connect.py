import peewee


def connect_db():
    db_name = "test"
    mysql_db = peewee.MySQLDatabase(db_name, host='127.0.0.1', port=3306, user='root', passwd='123456', charset='utf8')
    print(mysql_db.connect())   # True or peewee.OperationalError
    return mysql_db


class MySQLModel(peewee.Model):
    class Meta:
        database = connect_db()


connect_db()



