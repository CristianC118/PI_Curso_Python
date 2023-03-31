
"""
    Expresiones Regulares 2

  Metacaracteres
    Anclas y clases de caracteres

  Links: (https://www.geeksforgeeks.org/password-validation-in-python/?ref=lbp)
"""

import re

lista_nombres= ['Ana Gómez',
                'María Martín',
                'Sandra López',
                'Santiago Martín',
                'Sandra Fernández']

for elemento in lista_nombres:

  # ^ sirve para buscar las palabras de inicio. $ sirve para buscar las palabras de final
  #if re.findall('^Sandra', elemento):
  if re.findall('[anm]', elemento):

    print(elemento)