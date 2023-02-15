
"""
    Interfaces Gráficas

  Creación de interfaces gráficas
    Ventanas Emergentes. Abrir Archivos

    Documentación de filedialog en Python con Tkinter:
(https://www.geeksforgeeks.org/file-explorer-in-python-using-tkinter/)
(https://www.geeksforgeeks.org/python-askopenfile-function-in-tkinter/)
"""

from tkinter import *
from tkinter import filedialog


root= Tk()


# N° 1
# Función para ser ejecutuda al presionar botón
def abreFichero():

  # N° 2
  fichero= filedialog.askopenfilename(title= 'Abrir', initialdir= 'C:', filetypes= (('Ficheros de Excel', 'xlsx'), ('Ficheros de Texto', '*.txt'), ('Todos los ficheros', '*.*')))
  print(fichero)

# N° 3
Button(root, text= 'Abrir fichero', command= abreFichero).pack()






root.mainloop()