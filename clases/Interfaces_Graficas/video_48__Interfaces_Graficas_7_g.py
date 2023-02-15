
"""
    Intefaces Gráficas

  Creación de Interfaces Gráficas
    - Funcionalidad calculadora
  """



from tkinter import * # Importar

raiz= Tk() # Crear Raíz
miFrame= Frame(raiz) # Crear Frame
miFrame.pack() # Empaquetar


#----------------------------Pantalla----------------------------------


# N° 1_g
# Llamamos a la función
numeroPantalla= StringVar()


# N° 2_g | Asociamos la variable recién creada
pantalla= Entry(miFrame, textvariable= numeroPantalla)
pantalla.grid(row= 1, column= 1, padx= 7, pady= 7, ipady= 10 ,columnspan= 4)
pantalla.config(background= '#4c007d', fg= 'yellow', justify= 'right', width= 45, font= ('Arial', 12))



#---------------------------Pulsaciones Teclado-------------------------
# N° 3_g
# Definiendo la función
def numeroPulsado(num):

  numeroPantalla.set(numeroPantalla.get() + num) # Con set() establecemos el texto y con get() hacemos que este reciba siempre las pulsaciones y las agregue a continuación

def limpiarPantalla():
  pantalla.delete(0, END)


def borrarNumber():
  estadoPantalla= pantalla.get()

  if len(estadoPantalla):
    nuevoEstadoPantalla= estadoPantalla[:-1]
    limpiarPantalla()
    pantalla.insert(0, nuevoEstadoPantalla)

  else:
    limpiarPantalla()
    pantalla.insert(0, 0)

#----------------------------Fila 2-------------------------------------


botonBorrar= Button(miFrame, text= 'Borrar', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow', command= lambda: borrarNumber())
botonBorrar.grid(row= 2, column= 4)

botonBorradoComp= Button(miFrame, text= 'Vaciar Pantalla', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow', command= lambda: limpiarPantalla())
botonBorradoComp.grid(row= 2, column= 1, columnspan= 3)
botonBorradoComp.config(width= 33)


#----------------------------Fila 3-------------------------------------


# N° 4_g
# Llamamos a la función cuando este sea pulsado con command=
boton7= Button(miFrame, text= '7', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow', command= lambda: numeroPulsado('7'))
boton7.grid(row= 3, column= 1)

boton8= Button(miFrame, text= '8', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow', command= lambda: numeroPulsado('8'))
boton8.grid(row=3, column= 2)

boton9= Button(miFrame, text= '9', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow', command= lambda: numeroPulsado('9'))
boton9.grid(row= 3, column= 3)

botonDiv= Button(miFrame, text= '/', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow')
botonDiv.grid(row= 3, column= 4)


#----------------------------Fila 4-------------------------------------


boton4= Button(miFrame, text= '4', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow', command= lambda: numeroPulsado('4'))
boton4.grid(row= 4, column= 1)

boton5= Button(miFrame, text= '5', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow', command= lambda: numeroPulsado('5'))
boton5.grid(row=4, column= 2)

boton6= Button(miFrame, text= '6', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow', command= lambda: numeroPulsado('6'))
boton6.grid(row= 4, column= 3)

botonMult= Button(miFrame, text= '*', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow')
botonMult.grid(row= 4, column= 4)


#----------------------------Fila 5-------------------------------------


boton1= Button(miFrame, text= '1', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow', command= lambda: numeroPulsado('1'))
boton1.grid(row= 5, column= 1)

boton2= Button(miFrame, text= '2', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow', command= lambda: numeroPulsado('2'))
boton2.grid(row=5, column= 2)

boton3= Button(miFrame, text= '3', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow', command= lambda: numeroPulsado('3'))
boton3.grid(row= 5, column= 3)

botonResta= Button(miFrame, text= '-', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow')
botonResta.grid(row= 5, column= 4)



#----------------------------Fila 6-------------------------------------


botonComa= Button(miFrame, text= ',', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow', command= lambda: numeroPulsado(','))
botonComa.grid(row= 6, column= 2)

botonCero= Button(miFrame, text= '0', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow', command= lambda: numeroPulsado('0'))
botonCero.grid(row=6, column= 1)

botonIgual= Button(miFrame, text= '=', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow')
botonIgual.grid(row= 6, column= 3)

botonSuma= Button(miFrame, text= '+', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow')
botonSuma.grid(row= 6, column= 4)




raiz.mainloop() # Crear Bucle para ejecución constante