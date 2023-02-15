
"""
    Condicional 'if' (sí)
"""

def evaluacion(nota):
  valoracion= 'aprovado'

  if nota < 5:
    valoracion= 'Suspenso'

  return valoracion

print(evaluacion(4))


print('------------------')


def examenValoracion():

  valoracion= 'Aprovado'

  nota_alumno= int(input('Introduce la Nota: '))

  if nota_alumno < 5:
    valoracion= 'Suspendido'

  return valoracion

print(examenValoracion())


"""
    Nota: Link directo a la documentación de 'if' en Python (En Español)
(https://docs.python.org/es/3/tutorial/controlflow.html#if-statements)
"""
