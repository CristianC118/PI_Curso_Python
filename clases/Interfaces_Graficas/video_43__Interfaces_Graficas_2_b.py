
"""
    Interfaces Gráficas

  - Creación de Frames
"""

# N° 1_a
from tkinter import *

# N° 2_a
raiz= Tk()

# N° 4_a
raiz.title('Ventana de Pruebas')

# N° 5_a
#raiz.resizable(1, 1)

# N° 6_a
raiz.iconbitmap('clases\Interfaces_Graficas\hoshi.ico')


# N° 7_a
#raiz.geometry('650x400')

# N° 8_a
raiz.config(bg= 'black')

# N° 1_b
# Crear Frame
miFrame= Frame() # Debemos empaquetarlo dentro de la raíz

# N° 2_b
# Método pack() para empaquetarlo
miFrame.pack(fill= 'both', expand= 'True') # Con esto expandimos todo el color hasta de la raíz

# N° 3_b
# Visualizar el Frame
miFrame.config(bg= 'pink') # A un Frame hay que darle tamaño, dado que la raíz siempre se adaptará al contenedor interno.

# N° 4_b
# Dar tamaño al frame
miFrame.config(width=640, height=400) # Un Frame tiene un tamaño fijo y por defecto no se adapta al tamaño de la raíz.

# N° 6_b
# Especificar que queremos un borde con un grueso diferente al que le da por defecto que es un grosor de Cero
miFrame.config(bd= 35)

# N° 5_b
# Cambiar Bordes
miFrame.config(relief= GROOVE)

# N° 7_b
# Cambiar tipo de cursor
miFrame.config(cursor= 'hand2')

# N° 3_a
raiz.mainloop()