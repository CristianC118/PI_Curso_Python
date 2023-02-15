
"""
    Interfaces Gráficas

  Creación de Interfaces Gráficas
    - Interfaz gráfica calculadora.

  'columnspan' hace que una celda ocupe uno o varias casillas
"""

# N° 1_f
from tkinter import * # Importar

raiz= Tk() # Crear Raíz
miFrame= Frame(raiz) # Crear Frame
miFrame.pack() # Empaquetar


#----------------------------Pantalla----------------------------------


# N° 3_f
pantalla= Entry(miFrame)
pantalla.grid(row= 1, column= 1, padx= 7, pady= 7, columnspan= 4)
pantalla.config(background= '#4c007d', fg= 'yellow', justify= 'right', width= 38, font= ('Comic Sans MS', 12))


#----------------------------Fila 1-------------------------------------


# N° 4_f
boton7= Button(miFrame, text= '7', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow')
boton7.grid(row= 2, column= 1)

boton8= Button(miFrame, text= '8', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow')
boton8.grid(row=2, column= 2)

boton9= Button(miFrame, text= '9', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow')
boton9.grid(row= 2, column= 3)

botonDiv= Button(miFrame, text= '/', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow')
botonDiv.grid(row= 2, column= 4)


#----------------------------Fila 2-------------------------------------


boton4= Button(miFrame, text= '4', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow')
boton4.grid(row= 3, column= 1)

boton5= Button(miFrame, text= '5', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow')
boton5.grid(row=3, column= 2)

boton6= Button(miFrame, text= '6', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow')
boton6.grid(row= 3, column= 3)

botonMult= Button(miFrame, text= 'X', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow')
botonMult.grid(row= 3, column= 4)


#----------------------------Fila 3-------------------------------------


boton1= Button(miFrame, text= '1', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow')
boton1.grid(row= 4, column= 1)

boton2= Button(miFrame, text= '2', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow')
boton2.grid(row=4, column= 2)

boton3= Button(miFrame, text= '3', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow')
boton3.grid(row= 4, column= 3)

botonResta= Button(miFrame, text= '-', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow')
botonResta.grid(row= 4, column= 4)


#----------------------------Fila 4------------------------------------


botonComa= Button(miFrame, text= ',', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow')
botonComa.grid(row= 5, column= 1)

botonCero= Button(miFrame, text= '0', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow')
botonCero.grid(row=5, column= 2)

botonSuma= Button(miFrame, text= '+', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow')
botonSuma.grid(row= 5, column= 3)

botonIgual= Button(miFrame, text= '=', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow')
botonIgual.grid(row= 5, column= 4)



# N° 2_f
raiz.mainloop() # Crear Bucle para ejecución constante