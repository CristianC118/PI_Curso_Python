
"""
    Excepciones

- Lanzamiento de excepciones.
  . Instrucción Raise.
  . Creación de excepciones propias.
"""

def codigoUNO():

  def evaluaEdad(edad):

    if edad < 0:
      raise MiPropioError('No se permiten edades negativas.')

    if edad < 20:
      return 'Eres muy joven'

    elif edad < 40:
      return 'Eres joven'

    elif edad < 65:
      return 'Eres maduro'

    elif edad < 100:
      return 'Cuidadte...'

  print(evaluaEdad(-25))

codigoUNO()


print('\n')


def codigoDOS():

  import math

  def calculaRaiz(num1):

    if num1 < 0:
      raise ValueError('El número no puede ser negativo.') # N° 1_c

    else:
      return math.sqrt(num1)

  op1= int(input('Introduce un número: '))

  try: # N° 2_c
    print(calculaRaiz(op1))

  except ValueError as ErrorDeNumeroNegativo: # N° 3_c
    print(ErrorDeNumeroNegativo)

  print('Finalizado.')

codigoDOS()


"""
    Link a la Documentación de Excepciones de Python (En Español).
- (https://www.geeksforgeeks.org/errors-and-exceptions-in-python/?ref=lbp)
- (https://www.geeksforgeeks.org/built-exceptions-python/?ref=lbp)
"""