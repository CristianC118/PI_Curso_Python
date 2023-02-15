
"""
  Bucles (while y for):
    continue: salta a la siguiente interacción de Bucle.
    pass: duvuelve null en cuanto se lee en el interior de un Bucle.
    else: funciona de forma similar a como lo hace dentro un condicional.
"""

# continuie: sirve para omitir algo

def continuar():

  # N° 1
  for letra in 'Python':

    # N° 2
    if letra== 'h':
      # N° 3
      continue

    # N° 4
    print(f'Viendo la letra {letra}')
continuar()

print('\n')

def longitud():

  nombre= 'Pildoras Informáticas'

  contador= 0

  for i in nombre:

    if i== ' ':
      continue
    contador += 1

  print(contador)

longitud()

print('\n')

# pass: sirve para pausar un paquete de código

class MiClase:
  pass # Para implementar más tarde


print('\n')

# else: la intrucción else dentro de un bucle se ejecuta solo si un bucle está vacio

email= input('Introduce tu email: ')

for i in email:

  if i == '@':

    arroba= True
    break

else:
  arroba= False

print(arroba)


"""
  Documentación break, continue, else (En Español).
(https://docs.python.org/es/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)
"""