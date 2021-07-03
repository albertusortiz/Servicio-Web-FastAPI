# Variables
# Funciones
# Clases
# Colecciones



"""
Anotaciones en variables
"""
""" a: str = 'Hola, esta es una variable'
b: int = 30
c: float = 3.1415
d: bool = True

print(a)
print(type(a))

print(b)
print(type(b))

print(c)
print(type(c))

print(d)
print(type(d)) """



"""
Anotaciones en Funciones
"""
""" def suma(numero1: int, numero2: int) -> int:
  return numero1 + numero2


valor1: int = 10
valor2: int = 20
valor3: int

resultado: int = suma(valor1, valor2)

print(resultado)
print(type(resultado)) """



""" 
Anotaciones en Slases
"""
""" class User():

  def __init__(self, username:str, password:str) -> None:
    self.username = username
    self.password = password


  def saluda(self) -> str:
    return f'Hola {self.username}'

  def contra(self) -> int:
    return f'Tu contraseña es: {self.password}'

  
cody = User('Cody', 12345)
print(
  cody.saluda(),
  cody.contra()
) """



""" 
Anotaciones en Colecciones de tipo Lista
"""
"""
from typing import List


calificaciones: List[int] = [10, 9, 5, 5, 7, 9, 9]

def promedio(calificaciones: List[int]) -> float:
  return sum(calificaciones) / len(calificaciones)

print(
  promedio(calificaciones)
)
"""


""" 
Anotaciones en Colecciones de tipo Tupla
"""
"""
from typing import Tuple
from typing import Union

# configuraciones: Tuple[str] = ('localhost', '3306', 'root')
configuraciones: Tuple[Union[str, str, bool, int]] = ('root', 'localhost', 3306, True)

print(configuraciones)
"""

""" 
Anotaciones en Colecciones de tipo Diccionario
"""
from typing import Dict

usuarios: Dict[str, int] = {
  'eduardo': 10,
  'cody': 20
}

print(usuarios)