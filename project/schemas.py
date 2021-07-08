from typing import Any

from pydantic import validator
from pydantic import BaseModel

from peewee import ModelSelect

from pydantic.utils import GetterDict

class PeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        
        res = getattr(self._obj, key, default)
        if isinstance(res, ModelSelect):
            return list(res)

        return res

class ResponseModel(BaseModel):
    
    class Config:
        orm_mode = True
        getter_dict = PeweeGetterDict

# ----------- User -----------

# Modelo para validar datos de entrada
class UserRequestModel(BaseModel):
    username: str
    password: str

    @validator('username')
    def username_validator(cls, username):
        if len(username) < 3 or len(username) > 50:
            raise ValueError('La longitud debe encontrarse entre 3 y 50 caracteres.')

        return username

# Modelo para validar datos de salida
class UserResponseModel(ResponseModel):
    id: int
    username: str

# ----------- Review -----------

class ReviewRequestModel(BaseModel):
    user_id: int
    movie_id: int
    review: str
    score: int

class ReviewResponseModel(ResponseModel):
    id: int
    movie_id: int
    review: str
    score: int