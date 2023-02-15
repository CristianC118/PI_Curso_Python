

"""
    Excepciones

  ¿Qué son?
    Las excepciones son errores que ocurren durante la ejecución del programa. La sintaxis del código es correcta pero durante la ejecución ha ocurrido 'algo inesperado'.

    Este tipo de errores de ejecución se pueden controlar para que la ejecución del programa continúe. Es lo que se conoce como manejo o control de excepciones.

try (intentar)
except (parecido a if/else)
"""

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

op1= int(input('Introduce el primer número: '))

op2= int(input('Introduce el segundo número: '))

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


"""
    Link a la Documentación de Excepciones de Python (En Español).
- (https://docs.python.org/es/3/tutorial/errors.html#exceptions)
- (https://docs.python.org/es/3/tutorial/errors.html#handling-exceptions)
"""