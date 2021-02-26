import peewee
from connect import BaseModel
from connect import db


class PyUser(BaseModel):
    class Meta:
        database = db
        table_name = "py_user"
        print("connect instance from PyUser: {}".format(database))

    username = peewee.CharField()
    email = peewee.CharField()
    created_at = peewee.IntegerField()

