import peewee
from connect import MySQLModel


class Py_User(MySQLModel):
    username = peewee.CharField()
    email = peewee.CharField()
    created_at = peewee.IntegerField()

