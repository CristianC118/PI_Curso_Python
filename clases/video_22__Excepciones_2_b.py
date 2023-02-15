
"""
    Excepciones

  - Capturas de varias excepciones
  - Cláusula 'finally'
"""

def codigoUno():

  def suma(num1, num2):
    return num1 + num2

  def resta(num1, num2):
    return num1 - num2

  def multiplica(num1, num2):
    return num1 * num2

  def divide(num1, num2):

    try: # N° 1_a
      return num1 / num2

    except ZeroDivisionError: # N° 2_a
      print('No se puede dividir entre Cero') # N° 3_a

      return 'Operación Errónea' # N° 4_a


  while True: # N° 3_b
    try: # N° 1_b
      op1= int(input('Introduce el primer número: '))

      op2= int(input('Introduce el segundo número: '))
      break

    except ValueError: # N° 2_b
      print('Los valores introducidos no son correctos. \nInténtalo de nuevo...')

  operacion= input('Introduce la operación a realizar (suma, resta, multiplica, divide): ')

  if operacion== 'suma':
    print(suma(op1, op2))

  elif operacion== 'resta':
    print(resta(op1, op2))

  elif operacion== 'multiplica':
    print(multiplica(op1, op2))

  elif operacion== 'divide':
    print(divide(op1, op2))

  else:
    print('Operación no contemplada')

  print('Operación ejecutada. Continuación de ejecución del programa.')

#codigoUno()


print('\n')


def codigoDOS():

  def dividir():

    try: # N° 1_b

      op1= float(input('Introduce el primer número: '))
      op2= float(input('Introduce el segundo número: '))

      print(f'La división es {op1/op2}')

    except ValueError: # N° 2_b
      print('El valor introducido es erróneo.')

    except ZeroDivisionError:# N° 3_b
      print('No se puede dividir entre Cero.')

    finally: # Sirve para ejecutar el código siempre / Se ejecuta Sí o Sí

      print('Cálculo finalizado')

  dividir()

codigoDOS()


"""
    Capturar una excepción ganeral.

except:
  print('Ha ocurrido un error!')
"""


"""
    Link a la Documentación de Excepciones de Python (En Español).
- (https://docs.python.org/es/3/tutorial/errors.html#exception-chaining)
- (https://docs.python.org/es/3/tutorial/errors.html#user-defined-exceptions)
- (https://docs.python.org/es/3/reference/compound_stmts.html#finally)
- (https://www.geeksforgeeks.org/python-exception-handling/?ref=lbp)
"""