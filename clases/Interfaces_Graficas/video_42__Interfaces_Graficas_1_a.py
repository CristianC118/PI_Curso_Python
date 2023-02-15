
"""
    Interfaces Gráficas

  - Libreria Tkinter
  - Manejo de Frames

También denominadas GUI, son intermediarios entre el programa y el usuario. Formadas por un conjunto de gráficos como ventanas, botones, menús, casillas de verificación, etc.

. Librerias con las que trabajar para crear GUI:
  - Tkinter
  - WxPython
  - PyQT
  - PyGTK

Tkinter es un puente entre Python y la libreria TCL/TK.

    Estructura de ventana con Tkinter
  . Raíz (tk)
    -  Frame: Organizador o aglutinador de elementos.
      Elementos: Widgets


    Nota: Documentación de Tkinter.
(https://docs.python.org/es/3/library/tk.html)
(https://www.geeksforgeeks.org/python-tkinter-tutorial/?ref=lbp)
"""

# N° 1_a
# Importar Libreria
from tkinter import *

# N° 2_a
# Llamamos a la Clase con la creación de una variable
raiz= Tk()

# N° 4_a
# Dar título a la ventana
raiz.title('Ventana de Pruebas')

# N° 5_a
# Impedir la redimensión de la ventana. Admite parámetros de tipo Booleanos (True, False o Uno y Cero)
raiz.resizable(1, 1) # With (Ancho), Height (Alto)

# N° 6_a
# Agregar Icono
raiz.iconbitmap('clases\Interfaces_Graficas\hoshi.ico')


# N° 7_a
# Cambiar tamaño de la interfaz
raiz.geometry('650x400')

# N° 8_a
# Método config() nos permite cambiar características
raiz.config(bg= 'black')

# N° 3_a
# Método mainloop() es necesaria porque una ventana para que pueda estar en ejecución debe estar en una especie de bucle infinito
raiz.mainloop() # El Método mainloop() siempre debe ir al final.
