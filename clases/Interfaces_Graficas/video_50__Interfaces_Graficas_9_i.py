
"""
    Interfaces Gráficas

  Botones de radio. Radiobuttons

    Documentación de Radiobuttons en Python:
(https://www.geeksforgeeks.org/radiobutton-in-tkinter-python/)
"""

# N° 1
from tkinter import *

# N° 2
root= Tk()

# N° 4
varOpcion= IntVar()

# N° 7
def imprimir():

  #print(varOpcion.get())

  # N° 8.1
  if varOpcion.get()== 1:
    etiqueta.config(text= 'Has elegido masculino')

  elif varOpcion.get()== 2:
    etiqueta.config(text= 'Has elegido femenino')

  else:
    etiqueta.config(text= 'Otros')


# N° 6
Label(root, text= 'Género:').pack()


# N° 5
Radiobutton(root, text= 'Masculino', variable= varOpcion, value= 1, command= imprimir).pack()
Radiobutton(root, text= 'Femenino', variable= varOpcion, value= 2, command= imprimir).pack()
Radiobutton(root, text= 'Otras Opciones', variable= varOpcion, value= 3, command= imprimir).pack()


# N° 8
etiqueta= Label(root)
etiqueta.pack()





# N° 3
root.mainloop()