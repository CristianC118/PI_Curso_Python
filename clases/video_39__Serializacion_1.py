
"""
    Serialización (Colecciones):

  ¿Qué es?
- Consiste en guardar en un fichero externo, por ejemplo, una colección, diccionario, un objeto. Pero estas se guardan en un fichero codificado en código binario, es decir, en decir una sucesión de bites (Unos y Ceros).

  Bibliotecas necesarias
Pickle
  . Método dump(): volcado de datos al fichero binario externo.
  . Método load(): caerga de los datos del fichero binario externo.
"""

# N° 1
import pickle

"""# N° 2
video_39_lista_nombre= ['Pedro', 'Ana', 'María', 'Isabel']

# N° 3
# Crear fichero externo
fichero_binario= open('video_39_lista_nombre', 'wb') # Escritura binaria

# N° 4
# Volcado de la lista al fichero externo
pickle.dump(video_39_lista_nombre, fichero_binario)

# N° 5
fichero_binario.close()

# N° 6
# Incluso podemos eliminarlo de la memoria
del (fichero_binario)"""

# *********************************************
# Rescatar y leer la información en el interior
# *********************************************

# N° 1
# Abrir archivo
fichero= open('video_39_lista_nombre', 'rb') # Lectura binaria

# N° 2
# guardar y cargar archivo
lista= pickle.load(fichero)

print(lista)


"""
    Nota: Documentación de la Serialización con pickle en Python
(https://pyspanishdoc.sourceforge.net/lib/module-pickle.html)
  Extra
(https://pyspanishdoc.sourceforge.net/lib/module-marshal.html)
  """