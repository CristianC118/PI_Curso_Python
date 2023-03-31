
"""
    Decoradores

  ¿Qué son?
  Funciones que a su vez añaden funcionalidades a otras funciones.
  Les añaden funcionalidades

  Estructura de un decorador:
    3 funciones (A, B, C) donde A recibe como parámetro a B y devolver C.
    Un decorador devuelve una función.
"""

def funcion_decoradora(funcion_parametro):

  def funcion_interior():

    # Primer Mensaje
    print('Vamos a realizar un cálculo: ')
    funcion_parametro()

    # Segunda Mensaje
    print('Hemos terminado el cálculo.')

  return funcion_interior()



@funcion_decoradora
def sumaa():
  print(15 + 20)



def restaa():
  print(30 - 10)

sumaa()
restaa()


print('asdasdasd')