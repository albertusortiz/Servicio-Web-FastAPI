from typing import List

from fastapi import FastAPI

from .database import User
from .database import Movie
from .database import UserReview

from .routes import user_router
from .routes import review_router

from .database import database as connection


app = FastAPI(title='Proyecto para reseñar peliculas',
            description='En este proyecto seremos capaces de reseñar peliculas.',
            version='1')

app.include_router(user_router)
app.include_router(review_router)

@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()

    connection.create_tables([User, Movie, UserReview])

@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()