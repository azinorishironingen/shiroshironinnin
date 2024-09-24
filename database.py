from peewee import *

db = SqliteDatabase('ajinoris.db')

class Ajinori(Model):
    name = CharField()

    class Meta:
        database = db # This model uses the "people.db" database.

db.create_tables([Ajinori])


