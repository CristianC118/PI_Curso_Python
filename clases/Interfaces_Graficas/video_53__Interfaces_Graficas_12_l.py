
"""
    Interfaces Gráficas

  Creación de interfaces gráficas
    Ventanas Emergentes:
      - Ventas modales para informar, avisar o permitir realizar tarear al usuario.

    Documentación de ventanas emergentes en Python con Tkinter:
(https://www.geeksforgeeks.org/popup-menu-in-tkinter/)
(https://www.geeksforgeeks.org/python-panedwindow-widget-in-tkinter/)
"""

from tkinter import *
from tkinter import messagebox


root= Tk()


# N° 1
# Función a ser llamada para la ventana emergente
def infoAdicional():
  messagebox.showinfo('Procesador', 'Procesador de Textos 2022')

# Modificar estructuras de ventana
def avisoLicencia():
  messagebox.showwarning('Licencia', 'Producto bajo licencia GNU')

def salirApp():
  # valor= messagebox.askquestion('Salir', '¿Deseas salir de la aplicación?') # Devuelve 'yes' o 'no'
  valor= messagebox.askokcancel('Salir', '¿Deseas salir de la aplicación?') # Devuelve 'True' o 'False'

  if valor== True:
    root.destroy() # Cierra el bucle


def cerrarDocu():
  valor= messagebox.askretrycancel('Reintentar', 'No es posible cerrar el documento. Esta bloqueado.')

  if valor== False:
    root.destroy()


barraMenu= Menu(root)
root.config(menu= barraMenu, width= 250, height= 250)


archivoMenu= Menu(barraMenu, tearoff= 0)

barraMenu.add_cascade(label= 'Arhivo', menu= archivoMenu)
archivoMenu.add_command(label= 'Nuevo')
archivoMenu.add_command(label= 'Guardar')
archivoMenu.add_command(label= 'Guardar Como')
archivoMenu.add_command(label= 'Cerrar', command= cerrarDocu)
archivoMenu.add_separator()
archivoMenu.add_command(label= 'Salir', command= salirApp)

archivoEdicion= Menu(barraMenu, tearoff= 0)
barraMenu.add_cascade(label= 'Edición', menu= archivoEdicion)
archivoEdicion.add_command(label= 'Copiar')
archivoEdicion.add_command(label= 'Cortar')
archivoEdicion.add_command(label= 'Pegar')

archivoHerramientas= Menu(barraMenu, tearoff= 0)
barraMenu.add_cascade(label= 'Herramientas', menu= archivoHerramientas)


archivoAyuda= Menu(barraMenu, tearoff= 0)
barraMenu.add_cascade(label= 'Ayuda', menu= archivoAyuda)
archivoAyuda.add_command(label= 'Licencia', command= avisoLicencia)
archivoAyuda.add_command(label= 'Acerca de...', command= infoAdicional)










root.mainloop()