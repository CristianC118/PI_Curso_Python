
"""
    Archivos Externos

- Objetivo: Persistencia de Datos

  . Alternativas:
- Manejo de archivos externos
- Trabajo con BBDD

  Fases necesarias para guardar información en archivos externos.

. Creación
  . Apertura
    . Manipulación
      . Cierre

    Documentación de la libreria io en Python:
(https://docs.python.org/es/3/library/io.html)
"""

# N° 1
# Llamamos a la libreria
from io import open

"""# N° 2
# Creamos el archivo externo el cual pide dos argumentos: el nombre del archivo y el modo en el que lo vamos a abrir (lectura, escritura, append(agregar info a archivo existente))
archivo_texto= open('video_37__archivo.txt', 'w')

# N° 3
# Creamos la info para el archivo
frase= 'Estupendo día para estudiar Python. \nHello World.'

# N° 4
# Incluimos los datos al archivo
archivo_texto.write(frase)

# # N° 5
# Cerramos el archivo (Cerramos el archivo que esta abierto en memoria)
archivo_texto.close()"""

"""# N° 6
# Abrir el archivo en modo lectura
archivo_texto= open('video_37__archivo.txt', 'r')

# N° 7
# Para leer la info que haya en el archivo
texto= archivo_texto.read() # readlines() sirve para leer la info línea por línea y lo almacena en una lista

# N° 8
# Cerramos nuevamente
archivo_texto.close()

print(texto)"""

"""# N° 9
archivo_texto= open('video_37__archivo.txt', 'r')

lineas_texto=archivo_texto.readlines()

archivo_texto.close()

print(lineas_texto)"""


# N° 10
# Abrir archivo para agregar información
archivo_texto= open('video_37__archivo.txt', 'a')

# N° 11
# Añadir la nueva info a agregar en el archivo
archivo_texto.write('\nSiempre es una buena ocasión para estudiar Python')

# N° 12
# Cerramos de vuelta :v
archivo_texto.close()