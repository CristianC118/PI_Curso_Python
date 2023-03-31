
"""
    Expresiones Regulares 4
      Funciones del módulo re
        Match y serch
"""

import re

nombre1= 'Sandra López'
nombre2= 'Antonio Gómez'
nombre3= 'María López'

# desabilita el case sensitive
# . sirve para buscar todo lo que viene a continuación
if re.match('Sandra', nombre1, re.IGNORECASE):
  print('He encontrado el nombre')

else:
  print('No lo he encontrado')