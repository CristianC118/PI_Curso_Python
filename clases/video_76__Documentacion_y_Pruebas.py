
"""
    Documentación y Pruebas
  Utilizar la documentación para realizar pruebas.
    Módulo doctest
"""

import doctest
doctest.testmod()

def areaTriangulo(base, altura):

  """
    Calcula el área de un triángulo dado.

    >>> areaTriangulo(3, 6)
    'El área del triángulo es: 9.0'

  """

  return (f'El área del triángulo es: {(base * altura) / 2}')

print('******************************************************')

def compruebaMail(mailUsuario):

  """
  La función compruebaMail evalúa un mail recibido en busca
  de la @. Si tiene una @ es correcto, si tiene más de una @
  es incorrecto. Si la @ está al final es incorrecto.

  >>> compruebaMail('juan@cursos.es')
  True

  >>> compruebaMail('juancursos.es@')
  False

  >>> compruebaMail('juancursos.es')
  False

  >>> compruebaMail('juan@cursos@.es')
  False

  """

  arroba= mailUsuario.count('@')

  if (arroba!= 1 or mailUsuario.rfind('@')==(len(mailUsuario)-1) or mailUsuario.find('@')== 0):

    return False

  else:
    return True