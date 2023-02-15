
"""
    Módulos

  ¿Qué son?
. Un archivo con extensión .py .pyc (Python Compilado) o archivo escrito en C para CPython, que posee su propio espacio de nombres y que puede contener variables, funciones, clasezs e incluso otros Módulos.

  ¿Para qué sirven?
. Para organizar y reutilizar el código (modularización y reutilización)

    - Python por defecto busca el módulo que estamos importando al mismo directorio donde se encuentra el script que lo esta llamando. Y sí no lo encuentra pasa a buscarlo al syspath (un conjunto de directorios entre los que esta el directorio de instalción de python),
"""

# import funciones_matematicas

from ejemplo1_funciones_matematicas import * # El asterisco (*) llama todo el código dentro del módulo llamado pero reserva una gran cantidad de memoria.

suma(1, 1)
resta(1, 2)
multiplicacion(8, 5)


"""
    Nota: Documentación de los Módulos en Python
(https://docs.python.org/es/3/tutorial/modules.html)
(https://www.geeksforgeeks.org/python-collections-module/?ref=lbp)
"""