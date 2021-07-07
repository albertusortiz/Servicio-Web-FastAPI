from pydantic import validator
from pydantic import BaseModel

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