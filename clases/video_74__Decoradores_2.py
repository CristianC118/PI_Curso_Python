
"""
    Decoradores 2
      Decoradores con parámetros
"""

def funcion_decoradora(funcion_parametro):

  # nomenclatura del asterísco (*) puede recibir un número indeterminado de parámetros
  def funcion_interior(*args, **kwargs):

    # Primer Mensaje
    print('Vamos a realizar un cálculo: ')

    funcion_parametro(*args, **kwargs)

    # Segunda Mensaje
    print('Hemos terminado el cálculo.')

  return funcion_interior


@funcion_decoradora
def sumaa(num1, num2):
  print(num1 + num2)


@funcion_decoradora
def restaa(num1, num2):
  print(num1 - num2)


@funcion_decoradora
def potencia(base, exponente):
  print(pow(base, exponente))


sumaa(7, 5)
restaa(12, 10)
potencia(base= 5, exponente= 3)