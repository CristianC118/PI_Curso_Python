
"""
    Interfaces Gráficas

  Widget Label:
    - Utilizados para mostrar o imágenes.
    - Tienen como única finalidad mostrar texto, no se puede interactuar con él (borrar, arrastrar, etc).

  Sintaxis:

variableLabel= Label(contenedor, opciones)
"""

# N° 1_c
# Importamos Tkinter
from tkinter import *

# N° 2_c
# Creación de la raíz
root= Tk()

# N° 3_c
# Creación del Frame y especificamos en el constructor que este estará en la raíz
miFrame= Frame(root, width= 800, height= 800)

# # N° 4_c
# Empaquetamos
miFrame.pack()

# N° 8_c
miImagen= PhotoImage(file= 'clases\Interfaces_Graficas\mgl.png')

# N° 6_c
# Ubicar texto dentro de la interfaz gráfica
#miLabel= Label(miFrame, text= 'Hola Python! :)') # Debemos especificar el contenedor Padre

# N° 7_c
#miLabel.place(x= 200, y= 200) # Empaquetamos el Label
# Al utilizar el pack con el Label adapta lo que seria el contenedor a las dimensiones del Label. si queremos que respete el tamaño que le damos a la raíz y además ubicar el texto, debemos sustituir el pack por el método place() que nos permite ubicar el texto en cualquier lugar dentro de nuestra GUI mediante unas coordenas X e Y.
# Podemos abreviar código si más adelante no utilizaremos la variable Label de la siguiente forma con la nomenclatura del punto.
Label(miFrame, image= miImagen).place(x= 200, y= 200)
# text= 'Hello World :)', fg= 'red', font= ('Comic Sans MS',18)

# N° 5_c
root.mainloop() # Bucle para matenerlo abierto


"""
    Nota: Documentación de Label en Python:
(https://www.geeksforgeeks.org/python-tkinter-label/?ref=lbp)
(https://www.geeksforgeeks.org/python-place-method-in-tkinter/?ref=lbp)
"""