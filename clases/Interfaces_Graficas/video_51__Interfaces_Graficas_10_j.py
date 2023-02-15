

"""
    Interfaces Gráficas

  Botones de Selección. Checkbuttons

    Documentación de los Checkbuttons en Python:
(https://www.geeksforgeeks.org/python-tkinter-checkbutton-widget/)
"""

from tkinter import *

root= Tk()

# N° 1
root.title('Ejemplo')

# N° 6
playa= IntVar()
montania= IntVar()
turismoRutal= IntVar()


# N° 7
def opcionesViaje():

  # N° 7.1
  opcionEscogida= ''

  # N° 7.2
  if (playa.get()== 1):
    opcionEscogida += 'Playa'

  if (montania.get()== 1):
    opcionEscogida += ' Montaña'

  if (turismoRutal.get()== 1):
    opcionEscogida+= ' Turismo Rural'


  # N° 8.1
  textoFinal.config(text= opcionEscogida)


# N° 3
foto= PhotoImage(file= 'clases\Interfaces_Graficas\qwerty.png')
Label(root, image= foto).pack()

# N° 4
frame= Frame(root)
frame.pack()

# N° 5
Label(frame, text= 'Elige tu Destino:', width= 35).pack()

# N° 2
Checkbutton(frame, text= 'Playa', variable= playa, onvalue= 1, offvalue= 0, command= opcionesViaje).pack()
Checkbutton(frame, text= 'Montaña', variable= montania, onvalue= 1, offvalue= 0, command= opcionesViaje).pack()
Checkbutton(frame, text= 'Turismo Rural', variable= turismoRutal, onvalue= 1, offvalue= 0, command= opcionesViaje).pack()


# N° 8
textoFinal= Label(frame)
textoFinal.pack()




root.mainloop()