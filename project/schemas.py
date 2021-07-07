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
class UserResponseModel(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True
        getter_dict = PeweeGetterDict


class ReviewRequestModel(BaseModel):
    user_id: int
    movie_id: int
    review: str
    score: int

class ReviewResponseModel(BaseModel):
    id: int
    movie_id: int
    review: str
    score: int

    class Config:
        orm_mode = True
        getter_dict = PeweeGetterDict