from fastapi import FastAPI

from database import User
from database import Movie
from database import UserReview

from database import database as connection

from schemas import UserBaseModel

app = FastAPI(title='Proyecto para reseñar peliculas',
            description='En este proyecto seremos capaces de reseñar peliculas.',
            version='1')

@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()

    connection.create_tables([User, Movie, UserReview])

@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()

@app.get('/')
async def index():
    return 'Hola mundo, desde un servidor en FastAPI.'


@app.post('/users')
async def create_user(user: UserBaseModel):

    hash_password = User.create_password(user.password)
    
    user = User.create(
        username = user.username,
        password = hash_password
    )

    return user.id