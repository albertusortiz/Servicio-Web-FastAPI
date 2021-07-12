from fastapi import APIRouter
from fastapi import HTTPException

from fastapi.security import HTTPBasicCredentials

from ..database import User

from ..schemas import UserRequestModel
from ..schemas import UserResponseModel

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
async def login(credentials: HTTPBasicCredentials):
    
    user = User.select().where(User.username == credentials.username).first()

    if user is None:
        raise HTTPException(status_code=404, detail='User Not Found.')

    if user.password != User.create_password(credentials.password):
        raise HTTPException(status_code=404, detail='Password Error.')

    return user