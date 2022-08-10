from peewee import *

database = SqliteDatabase('kappadata.db')

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class KappaData(BaseModel):
    channel_id = IntegerField(null=True)
    counter = IntegerField(null=True)
    guild_id = IntegerField(null=True)
    num_messages = IntegerField(null=True)

    class Meta:
        table_name = 'KappaData'
        primary_key = False

