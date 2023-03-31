
"""
    Expresiones Regulares 3
      Rangos
"""

import re

lista_nombres= ['Ana',
                'Pedro',
                'María',
                'Rosa',
                'Sandra',
                'Celia']

for elemento in lista_nombres:

  if re.findall('^[o-t]', elemento):

    print(elemento)