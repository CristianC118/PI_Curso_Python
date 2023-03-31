
"""
    Interfaces Gráficas

  Creación de Interfaces Gráficas
    - Funcionalidad Calculadora
"""

from tkinter import * # Importar

raiz= Tk() # Crear Raíz
miFrame= Frame(raiz) # Crear Frame
miFrame.pack() # Empaquetar



operacion= ''
reset_pantalla= False
resultado= 0


#----------------------------Pantalla----------------------------------

numeroPantalla= StringVar()


pantalla= Entry(miFrame, textvariable= numeroPantalla)
pantalla.grid(row= 1, column= 1, padx= 7, pady= 7, ipady= 10, columnspan= 4)
pantalla.config(background= '#4c007d', fg= 'yellow', justify= 'right', width= 45, font= ('Arial', 12))


#---------------------------Pulsaciones Teclado-------------------------

def numeroPulsado(num):

  global operacion
  global reset_pantalla

  if reset_pantalla != False:
    numeroPantalla.set(num)
    reset_pantalla= False

  else:
    numeroPantalla.set(numeroPantalla.get() + num)


#---------------------------Función Suma--------------------------------

def suma(num):

  global operacion
  global resultado
  global reset_pantalla

  resultado += int(num)
  operacion= 'suma'
  reset_pantalla= True
  numeroPantalla.set(resultado)


#---------------------------Función Resta--------------------------------

num1= 0
contador_resta= 0

def resta(num):

  global operacion
  global resultado
  global num1
  global contador_resta
  global reset_pantalla

  if contador_resta== 0:

    num1= int(num)
    resultado= num1

  else:
    if contador_resta== 1:

      resultado= num1 - int(num)

    else:
      resultado= int(resultado) - int(num)

    numeroPantalla.set(resultado)
    resultado= numeroPantalla.get()

  contador_resta= contador_resta + 1
  operacion= 'resta'
  reset_pantalla= True

#---------------------------Función Multiplicaión------------------------

contador_multi= 0

def multiplica(num):

  global operacion
  global resultado
  global num1
  global contador_multi
  global reset_pantalla

  if contador_multi== 0:

    num1= int(num)
    resultado= num1

  else:
    if contador_multi== 1:
      resultado= int(resultado) * int(num)

    else:
      resultado= int(resultado) * int(num)

    numeroPantalla.set(resultado)
    resultado= numeroPantalla.get()

  contador_multi= contador_multi + 1
  operacion= 'multiplica'
  reset_pantalla= True


#---------------------------Función División-----------------------------

contador_divi= 0

def divide(num):

  global operacion
  global resultado
  global num1
  global contador_divi
  global reset_pantalla

  if contador_divi== 0:

    num1= float(num)
    resultado= num1

  else:
    if contador_divi== 1:
      resultado= num1 / float(num)

    else:
      resultado= float(resultado) / float(num)

    numeroPantalla.set(resultado)
    resultado= numeroPantalla.get()

  contador_divi= contador_divi + 1
  operacion= 'divide'
  reset_pantalla= True


#---------------------------Funcion Resultado Final----------------------

def elResultado():

  global resultado
  global operacion
  global contador_resta
  global contador_multi
  global contador_divi

  if operacion== 'suma':

    numeroPantalla.set(resultado + int(numeroPantalla.get()))
    resultado= 0

  elif operacion== 'resta':

    numeroPantalla.set(int(resultado) - int(numeroPantalla.get()))
    resultado= 0
    contador_resta= 0

  elif operacion== 'multiplica':
    numeroPantalla.set(int(resultado) * int(numeroPantalla.get()))
    resultado= 0
    contador_multi= 0

  elif operacion== 'divide':

    numeroPantalla.set(int(resultado) / int(numeroPantalla.get()))
    resultado= 0
    contador_divi= 0


#---------------------------Función Limpiado de Pantalla----------------

def limpiarPantalla():
  pantalla.delete(0, END)


#--------------------------Función Borrar Números-----------------------

def borrarNumber():
  estadoPantalla= pantalla.get()

  if len(estadoPantalla):
    nuevoEstadoPantalla= estadoPantalla[:-1]
    limpiarPantalla()
    pantalla.insert(0, nuevoEstadoPantalla)

  else:
    limpiarPantalla()
    pantalla.insert(0, '')


#----------------------------Fila 2-------------------------------------


botonBorrar= Button(miFrame, text= '⌫', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow', command= lambda: borrarNumber())
botonBorrar.grid(row= 2, column= 4)

botonBorradoComp= Button(miFrame, text= 'Vaciar Pantalla', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow', command= lambda: limpiarPantalla())
botonBorradoComp.grid(row= 2, column= 1, columnspan= 3)
botonBorradoComp.config(width= 33)


#----------------------------Fila 3-------------------------------------



boton7= Button(miFrame, text= '7', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow', command= lambda: numeroPulsado('7'))
boton7.grid(row= 3, column= 1)

boton8= Button(miFrame, text= '8', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow', command= lambda: numeroPulsado('8'))
boton8.grid(row=3, column= 2)

boton9= Button(miFrame, text= '9', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow', command= lambda: numeroPulsado('9'))
boton9.grid(row= 3, column= 3)

botonDiv= Button(miFrame, text= '/', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow', command= lambda: divide(numeroPantalla.get()))
botonDiv.grid(row= 3, column= 4)


#----------------------------Fila 4-------------------------------------


boton4= Button(miFrame, text= '4', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow', command= lambda: numeroPulsado('4'))
boton4.grid(row= 4, column= 1)

boton5= Button(miFrame, text= '5', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow', command= lambda: numeroPulsado('5'))
boton5.grid(row=4, column= 2)

boton6= Button(miFrame, text= '6', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow', command= lambda: numeroPulsado('6'))
boton6.grid(row= 4, column= 3)

botonMult= Button(miFrame, text= '*', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow', command= lambda: multiplica(numeroPantalla.get()))
botonMult.grid(row= 4, column= 4)


#----------------------------Fila 5-------------------------------------


boton1= Button(miFrame, text= '1', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow', command= lambda: numeroPulsado('1'))
boton1.grid(row= 5, column= 1)

boton2= Button(miFrame, text= '2', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow', command= lambda: numeroPulsado('2'))
boton2.grid(row=5, column= 2)

boton3= Button(miFrame, text= '3', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow', command= lambda: numeroPulsado('3'))
boton3.grid(row= 5, column= 3)

botonResta= Button(miFrame, text= '-', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow', command= lambda: resta(numeroPantalla.get()))
botonResta.grid(row= 5, column= 4)



#----------------------------Fila 6-------------------------------------


botonComa= Button(miFrame, text= ',', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow', command= lambda: numeroPulsado(','))
botonComa.grid(row= 6, column= 2)

botonCero= Button(miFrame, text= '0', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow', command= lambda: numeroPulsado('0'))
botonCero.grid(row=6, column= 1)

botonIgual= Button(miFrame, text= '=', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow', command= lambda: elResultado())
botonIgual.grid(row= 6, column= 3)

botonSuma= Button(miFrame, text= '+', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow', command= lambda: suma(numeroPantalla.get()))
botonSuma.grid(row= 6, column= 4)




raiz.mainloop()



"""# N° 1_h
# Creación de una variable global para que pueda ser llamada desde cualquiera lado
operacion= ''

# N° 4_h
# Variable para almacenar los valores
resultado= 0

#----------------------------Pantalla----------------------------------


numeroPantalla= StringVar()


pantalla= Entry(miFrame, textvariable= numeroPantalla)
pantalla.grid(row= 1, column= 1, padx= 7, pady= 7, ipady= 10 ,columnspan= 4)
pantalla.config(background= '#4c007d', fg= 'yellow', justify= 'right', width= 45, font= ('Arial', 12))


#---------------------------Pulsaciones Teclado-------------------------

def numeroPulsado(num):

  # N° 3_h
  global operacion

  # N° 3.1_h
  # Vaciar Pantalla
  if operacion != '':
    numeroPantalla.set(num)
    operacion= ''

  else:
    numeroPantalla.set(numeroPantalla.get() + num)


#---------------------------Función Suma--------------------------------

# N° 2_h
# Creación de la función suma
def suma(num):

  global operacion

  # N° 4.1_h
  global resultado

  # N° 4.2_h
  resultado += int(num)
  operacion= suma

  # N° 4.3_h
  numeroPantalla.set(resultado)


#---------------------------Función Resta--------------------------------

def resta(num):

  global operacion
  global resultado

  resultado -= int(num)
  operacion= resta

  numeroPantalla.set(resultado)


#---------------------------Función Multiplicaión------------------------

def multi(num):

  global operacion
  global resultado
  breakpoint()


#---------------------------Función División-----------------------------

def divi(num):

  global operacion
  global resultado
  breakpoint()


#---------------------------Funcion Resultado Final----------------------

# N° 5_h
# Creación de la función para el botón de igual
def elResultado():

  global resultado

  # N° 6_h
  # Sumar incluido el valor actual de la pantalla
  numeroPantalla.set(resultado + int(numeroPantalla.get()))

  # N° 7_h
  resultado= 0


#---------------------------Función Limpiado de Pantalla----------------

def limpiarPantalla():
  pantalla.delete(0, END)


#--------------------------Función Borrar Números-----------------------

def borrarNumber():
  estadoPantalla= pantalla.get()

  if len(estadoPantalla):
    nuevoEstadoPantalla= estadoPantalla[:-1]
    limpiarPantalla()
    pantalla.insert(0, nuevoEstadoPantalla)

  else:
    limpiarPantalla()
    pantalla.insert(0, '')


#----------------------------Fila 2-------------------------------------


botonBorrar= Button(miFrame, text= '⌫', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow', command= lambda: borrarNumber())
botonBorrar.grid(row= 2, column= 4)

botonBorradoComp= Button(miFrame, text= 'Vaciar Pantalla', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow', command= lambda: limpiarPantalla())
botonBorradoComp.grid(row= 2, column= 1, columnspan= 3)
botonBorradoComp.config(width= 33)


#----------------------------Fila 3-------------------------------------



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

botonResta= Button(miFrame, text= '-', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow', command= lambda: resta(numeroPantalla.get()))
botonResta.grid(row= 5, column= 4)



#----------------------------Fila 6-------------------------------------


botonComa= Button(miFrame, text= ',', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow', command= lambda: numeroPulsado(','))
botonComa.grid(row= 6, column= 2)

botonCero= Button(miFrame, text= '0', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow', command= lambda: numeroPulsado('0'))
botonCero.grid(row=6, column= 1)

# N° 6.1_h
# Llamar a la función elResultado
botonIgual= Button(miFrame, text= '=', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow', command= lambda: elResultado())
botonIgual.grid(row= 6, column= 3)

# N° 2.1_h
# Llamada de la función
botonSuma= Button(miFrame, text= '+', width= 10, height=3, font= (9), bg= '#4c007d', fg= 'yellow', command= lambda: suma(numeroPantalla.get()))
botonSuma.grid(row= 6, column= 4)




raiz.mainloop()"""