from peewee import *

database = MySQLDatabase(
    'albertus_servicio_fast_api',
    user='albertus_admin',
    password='servicio_fast_api',
    host='162.241.61.214',
    port=3306
)