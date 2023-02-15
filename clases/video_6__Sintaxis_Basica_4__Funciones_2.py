
"""
  Funciones: Paso de Parámetros
"""

def suma(num1, num2):

  print(num1 + num2)

suma(5, 7)
suma(2, 3)
suma(35, 358)

print('__________________')

def suma1(num1, num2):

  resultado= num1 + num2
  return resultado

# Para que return devuelva valores estos tienen que ser llamados pero aun así el programa funciona y almacena valores en memoria
print(suma1(123, 121))
print(suma1(7, 8))
print(suma1(21, 2))

# return puede servir para almacenar valores en una variable lo que te devuelva una función
almacena_resutaldo= suma1(5, 8)


"""
  Nota: Link directo a la documentación oficial de funciones en Python (En español)
(https://docs.python.org/es/3/tutorial/controlflow.html#defining-functions)
"""
