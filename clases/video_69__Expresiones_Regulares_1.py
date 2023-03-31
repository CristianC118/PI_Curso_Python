
"""
    Expresiones Regulares o regex

    ¿Qué son?
      Son una secuencia de caracteres que forman un patrón de búsqueda.

    ¿Para qué sirven?
			Para el trabajo y procesamiento de texto.

		Ejemplos:
			Buscar un texto que se ajusta a un formato determinado (correo electrónico)
			Buscar si existe o no una cadena de caracteres dentro de un texto.
      Contar el número de coincidencias dentro de un texto.
      Etc.

    Links: (https://www.geeksforgeeks.org/regular-expression-python-examples-set-1/?ref=lbp)
          (https://www.geeksforgeeks.org/regular-expressions-python-set-1-search-match-find/?ref=lbp)
          (https://www.geeksforgeeks.org/python-regex-re-search-vs-re-findall/?ref=lbp)
"""

import re

cadena= 'Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla'

print(re.search('aprender', cadena))

textoBuscar= 'aprender'
textoBuscar1= 'Python'

if re.search(textoBuscar, cadena) is not None:

  print("He encontrado el texto")

else:
  print('No he encontrado el texto')


textoEncontrado= re.search(textoBuscar, cadena)
print(textoEncontrado.start())
print(textoEncontrado.end())
print(textoEncontrado.span())

print(len(re.findall(textoBuscar1, cadena)))