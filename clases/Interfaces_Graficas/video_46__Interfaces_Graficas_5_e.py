
"""
    Interfaces Gráficas

  Text: Widgets utilizados para introducir texto largo.
  Button: Botones para interactuar con la interfaz.

  Nota 1:
- Podemos simplemente llamar el módulo de Scrollbar y este creará un scroll en el texto ya adecuado al widget.

    Ejemplo:
  from tkinter.scrolledtext import ScrolledText
  textoComentario= ScrolledText(miFrame, width= 15, height= 5)

  Nota 2: Documentación de Text en Python
(https://www.geeksforgeeks.org/python-tkinter-text-widget/?ref=lbp)
"""

from tkinter import *

raiz= Tk()
miFrame= Frame(raiz, width= 1200, height= 600)
miFrame.pack()

# N° 7_e
minombre= StringVar()

cuadroNombre= Entry(miFrame, textvariable= minombre)
cuadroNombre.grid(row= 0, column= 1)
cuadroNombre.config(fg= 'red', justify= 'center')

nombreLabel= Label(miFrame, text= 'Nombre:')
nombreLabel.grid(row= 0, column= 0, sticky= 'e', padx= 5, pady= 5)


cuadroPass= Entry(miFrame)
cuadroPass.grid(row= 1, column= 1, padx= 5, pady= 5)
cuadroPass.config(show= '*')

passLabel= Label(miFrame, text= 'Password:')
passLabel.grid(row= 1, column= 0, sticky= 'e', padx= 5, pady= 5)

cuadroApellido= Entry(miFrame)
cuadroApellido.grid(row= 2, column= 1, padx= 5, pady= 5)

apellidoLabel= Label(miFrame, text= 'Apellido:')
apellidoLabel.grid(row= 2, column= 0, sticky= 'e', padx= 5, pady= 5)


cuadroDireccion= Entry(miFrame)
cuadroDireccion.grid(row= 3, column= 1, padx= 5, pady= 5)

direccionLabel= Label(miFrame, text= 'Dirección:')
direccionLabel.grid(row= 3, column= 0, padx= 5, pady= 5)


# N° 1_e
textoComentario= Text(miFrame, width= 15, height= 5)
textoComentario.grid( row= 4, column= 1, padx= 5, pady= 5)

# N° 3_e
scrollVert= Scrollbar(miFrame, command= textoComentario.yview)
scrollVert.grid(row= 4, column= 2, sticky= 'nsew') # 'nsew' sirve para adaptar el scroll al tamaño del widget al que pertenece.

# N° 4_e
# Configura de manera correcta el indicar del scroll
textoComentario.config(yscrollcommand= scrollVert.set)

# N° 2_e
comentariosLabel= Label(miFrame, text= 'Comentario:')
comentariosLabel.grid(row= 4, column= 0, sticky= 'e', padx= 5, pady= 5)


# N° 6_e
def codigoBoton():

  minombre.set('Cristian') # La función .set establece valor a una variable y .get sirve para obtener información de un Entry (cuadro de texto).

# N° 5_e
# Creación de un botón
botonEnvio= Button(raiz, text= 'Enviar', command= codigoBoton)
botonEnvio.pack() # Empaquetación


raiz.mainloop()