
"""
    Interfaces Gráficas

  Widget Entry

- grid: Construye una grilla dentro de la interfaz gráfica
- sticky: Permite especificar el lugar de un widget usando puntos cardinales.
- padx/y: Separa los widget

  Documentación de Entry y grid() en Python:
(https://www.geeksforgeeks.org/python-tkinter-entry-widget/?ref=lbp)
(https://www.geeksforgeeks.org/python-grid-method-in-tkinter/?ref=lbp)
"""

# N° 1_d
# Importamos Librería
from tkinter import *

# N° 2_d
# Creación de la raíz
raiz= Tk()

# N° 6_d
miFrame= Frame(raiz, width= 1200, height= 600)

# N° 7_d
# Empaquetamos el Frame
miFrame.pack()

# N° 4_d
# Llamar a la clase y asignarle a quien pertenece
cuadroNombre= Entry(miFrame)
# N° 5.1_d
cuadroNombre.grid(row= 0, column= 1)
# N° 5_d
# Empaquetamos
#cuadroTexto.place(x= 600, y= 300) # Usamos el Método place() para ubicar donde nosotros quisieramos un Label

# N° 14_d
cuadroNombre.config(fg= 'red', justify= 'center')

# N° 15_d
cuadroPass= Entry(miFrame)
cuadroPass.grid(row= 1, column= 1, padx= 5, pady= 5)
cuadroPass.config(show= '*') # Coloca asteriscos en vez de mostrar los caractéres añadidos

# N° 10_d
cuadroApellido= Entry(miFrame)
cuadroApellido.grid(row= 2, column= 1, padx= 5, pady= 5)

# N° 11_d
cuadroDireccion= Entry(miFrame)
cuadroDireccion.grid(row= 3, column= 1, padx= 5, pady= 5)

# N° 8_d
# Creación del Widget Nombre
nombreLabel= Label(miFrame, text= 'Nombre:')
# N° 9.1_d
nombreLabel.grid(row= 0, column= 0, sticky= 'e', padx= 5, pady= 5)
# N° 9_d
# Indica el lugar donde estará el Widget de Nombre
#nombreLabel.place(x= 543, y= 300)

# N° 12_d
apellidoLabel= Label(miFrame, text= 'Apellido:')
apellidoLabel.grid(row= 2, column= 0, sticky= 'e', padx= 5, pady= 5)

# N° 13_d
direccionLabel= Label(miFrame, text= 'Dirección de Casa:')
direccionLabel.grid(row= 3, column= 0, padx= 5, pady= 5)

# N° 16_d
passLabel= Label(miFrame, text= 'Password:')
passLabel.grid(row= 1, column= 0, sticky= 'e', padx= 5, pady= 5)

# N° 3_d
# Abrimos Bucle
raiz.mainloop()