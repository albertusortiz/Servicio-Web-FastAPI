from collections import defaultdict
from peewee import *
from datetime import datetime

database = MySQLDatabase(
    'albertus_servicio_fast_api',
    user='albertus_admin',
    password='servicio_fast_api',
    host='162.241.61.214',
    port=3306
)

class User(Model):
    username = CharField(max_length=50, unique=True)
    password = CharField(max_length=50)
    created_at = DateTimeField(default=datetime.now)

    def __str__(self):
        return self.username

    class Meta:
        database = database
        table_name = 'users'

class Movie(Model):
    title = CharField(max_length=50)
    created_at = DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

    class Meta:
        database=database
        table_name = 'movies'

class UserReviuew(Model):
    user = ForeignKeyField(User, backref='reviews')
    movie = ForeignKeyField(Movie, backref)