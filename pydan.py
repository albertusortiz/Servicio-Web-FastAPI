from pydantic import validator
from pydantic import BaseModel
from pydantic import ValidationError

from typing import Optional


class User(BaseModel):
  username: str
  password: str
  repeat_password: str
  email: str
  age: Optional[int] = None

  @validator('username')
  def username_validation_length(cls, username):
    
    if len(username) < 3:
      raise ValueError('La longitud minima es de 4 caracteres.')

    if len(username) > 50:
      raise ValueError('La longitud máxima es de 50 caracteres.')

    return username

  @validator('repeat_password')
  def repeat_password_validation(cls, repeat_password, values):
    
    if 'password' in values and repeat_password != values['password']:
      raise ValidationError('Las contraseñas son diferentes.')

    return repeat_password

try:
  user1 = User(
    username='Cody',
    password='password123',
    repeat_password='password123',
    email='info@codigofacilito.com',
    age=27
  )

  print(user1)
except ValidationError as e:
  print(e.json())