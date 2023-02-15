
"""
    Interfaces Gráficas

  Creación de interfaces gráficas:
    Menús:
      - Barra en la parte superior con opciones de sub-menú.

    Documentación de los Menú's en Python:
(https://www.geeksforgeeks.org/python-menu-widget-in-tkinter/?ref=lbp)
"""

from tkinter import *


root= Tk()


# N° 1
# Creación de la variable donde se almacerá el Menú
barraMenu= Menu(root)
root.config(menu= barraMenu, width= 250, height= 250)




# N° 2
# Establecer cuantos elementos tendrá el menú con sus respectivos nombres
archivoMenu= Menu(barraMenu, tearoff= 0) # "tearoff" sirve para eliminar la lagrima

# N° 3
# Creación de los subs-menu
barraMenu.add_cascade(label= 'Arhivo', menu= archivoMenu)
archivoMenu.add_command(label= 'Nuevo')
archivoMenu.add_command(label= 'Guardar')
archivoMenu.add_command(label= 'Guardar Como')
archivoMenu.add_command(label= 'Cerrar')
archivoMenu.add_separator() # Sirve para colocar un separador horizontal
archivoMenu.add_command(label= 'Salir')

archivoEdicion= Menu(barraMenu, tearoff= 0)
barraMenu.add_cascade(label= 'Edición', menu= archivoEdicion)
archivoEdicion.add_command(label= 'Copiar')
archivoEdicion.add_command(label= 'Cortar')
archivoEdicion.add_command(label= 'Pegar')

archivoHerramientas= Menu(barraMenu, tearoff= 0)
barraMenu.add_cascade(label= 'Herramientas', menu= archivoHerramientas)


archivoAyuda= Menu(barraMenu, tearoff= 0)
barraMenu.add_cascade(label= 'Ayuda', menu= archivoAyuda)
archivoAyuda.add_command(label= 'Licencia')
archivoAyuda.add_command(label= 'Acerca de')










root.mainloop()