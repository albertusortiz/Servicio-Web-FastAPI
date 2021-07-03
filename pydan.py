from pydantic import BaseModel

from typing import Optional

class User(BaseModel):
  username: str
  password: str
  email: str
  age: Optional[int] = None

user1 = User(
  username=10,
  password='password123',
  email='info@codigofacilito.com',
  age=27
)

print(user1)