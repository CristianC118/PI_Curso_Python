

"""
    Generadores:

  ¿Qué son?
- Son estructuras que extraen valore de una función y se almacenan en objetos iterables (que se pueden recorrer).
- Estos valores se almacenan de uno en uno.
- Cada vez que un generador almacena un valor, esta permanentemente en un estado de pausa hasta que se solicita el siguiente. Esta característica es conocida 'suspención de estado'.

  ¿Para qué sirven?
- Son más eficientes que las funciones tradicionales.
- Muy útiles con listas de valores infinitos.
- Bajo determinados escenarios, será muy útil eque un generador devuelva los valores de uno en uno.

  Función 'Tradicional' (Genera números pares):

def generaNumeros():
  'líneas de código'
  return numeros

generaNumeros()

************************

  Generador (Genera números pares):

def generaNumeros():
  'líneas de código'
  yield numeros

generaNumeros()
"""

# Generar Números Pares: Ejemplo 1 (Con función tradicional)

def generaPares(limite): # Si no se le coloca un parámetro generará una lista infinita.

  num= 1
  miLista= []

  while num < limite:

    miLista.append(num * 2)
    num += 1

  return miLista

print(generaPares(10))


# Generar Números Pares: Ejemplo 2 (con Generador)

def generaPares(limite): # Si no se le coloca un parámetro generará una lista infinita.

  num= 1

  while num < limite:

    yield num * 2
    num += 1

devuelvePares= generaPares(10)

print(next(devuelvePares))

print('Aqui podría ir más código...')

print(next(devuelvePares))

print('Aqui podría ir más código...')

print(next(devuelvePares))

"""
  Link Documentación Generadores Python (En Español).
(https://docs.python.org/es/3/tutorial/classes.html#generators)
"""