
"""
    Archivos Externos 2

  Trabajar con ficheros externos de texto con el módulo io.
Punteros en texto.
"""

from io import open

archivo_texto= open('video_38__archivo2.txt', 'r+') # lectura y escritura

"""# N° 1
# método seek() pide un parámetro el cuál indicará al cursor donde se posionará. Posiciona el puntero en el lugar donde se lo especifíca.
archivo_texto.seek(11)

print(archivo_texto.read(11)) # read() hace una lectura hasta la posición del puntero donde se le especifíca."""

#archivo_texto.seek(len(archivo_texto.read())/2)

#archivo_texto.seek(len(archivo_texto.readline()))
#print(archivo_texto.readlines())

lista_texto= archivo_texto.readlines()

lista_texto[1]= 'Esta línea ha sido incluida desde el exterior\n'

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close()