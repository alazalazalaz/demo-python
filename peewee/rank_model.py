import peewee
from connect import BaseModel
from connect import db


class PyRank(BaseModel):
    class Meta:
        database = db
        table_name = "py_rank"
        print("connect instance from PyRank: {}".format(database))

    uid = peewee.IntegerField()
    rank = peewee.IntegerField()
    created_at = peewee.IntegerField()

