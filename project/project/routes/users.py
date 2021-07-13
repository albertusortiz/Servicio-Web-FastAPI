from typing import List

from fastapi import Cookie
from fastapi import Response

from fastapi import APIRouter
from fastapi import HTTPException

from fastapi.security import HTTPBasicCredentials

from ..database import User

from ..schemas import UserRequestModel
from ..schemas import UserResponseModel

from ..schemas import ReviewResponseModel

router = APIRouter(prefix='/users')

@router.post('', response_model=UserResponseModel)
async def create_user(user: UserRequestModel):

    if User.select().where(User.username == user.username).first():
        raise HTTPException(status_code=409, detail='El username ya se encuentra en uso.')

    hash_password = User.create_password(user.password)
    
    user = User.create(
        username = user.username,
        password = hash_password
    )

    return user


@router.post('/login', response_model=UserResponseModel)
async def login(credentials: HTTPBasicCredentials, response: Response):
    
    user = User.select().where(User.username == credentials.username).first()

    if user is None:
        raise HTTPException(status_code=404, detail='User Not Found.')

    if user.password != User.create_password(credentials.password):
        raise HTTPException(status_code=404, detail='Password Error.')

    response.set_cookie(key='user_id', value=user.id) # TOKEN
    return user


@router.get('/reviews', response_model=List[ReviewResponseModel])
async def get_reviews(user_id: int = Cookie(None)):
    
    user = User.select().where(User.id == user_id).first()

    if user is None:
        raise HTTPException(status_code=404, detail='User Not Found.')

    return [ user_review for user_review in user.reviews ]