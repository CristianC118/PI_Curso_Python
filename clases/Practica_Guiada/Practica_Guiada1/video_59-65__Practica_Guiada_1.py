
"""
		Práctica Guiada

  Aplicación Gráfica CURD
    - BBDD: Conectar (Creará una BBDD), Salir
    - Borrar: Borrará todos los campos
    - CRUD: Crear, Leer, Actualizar, Borrar
    - Datos de los Usuarios: ID, Nombre, Apellido, Dirección, Password, Comentario.
    - Botónes CRUD
    - El campo password no deberá mostrar la contraseña escrita en la interfaz

    Nota: Documentación Importante sobre Tkinter, SQLite y Float vs Decimal en Python:
- Tkinter Interfaz: (https://medium.com/@fareedkhandev/modern-gui-using-tkinter-12da0b983e22)
- BBDD SQLite: (https://docs.python.org/es/3/library/sqlite3.html#sqlite3.Cursor.executemany)
- Float vs Decimal: (https://www.laac.dev/blog/float-vs-decimal-python/)
                    (https://0.30000000000000004.com/)
                    (https://docs.python.org/3/library/decimal.html)
                    (https://towardsdev.com/python-tips-decimal-vs-float-72fe72fb7086)
"""


# Importar Librerías
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import sqlite3
from tkinter import messagebox
import os
from os import remove
from os import path



# Crear la raíz
root= Tk()
root.config(bg= '#3D0875')
root.geometry('260x360') # Cambiar tamaño de la interfaz
root.resizable(width= False, height= False) # Congelar tamaño de la pantalla
miFrame= Frame(root, bg= '#3D0875')
miFrame.pack()



# Damos nombre a la ventana
root.title('BBDD Personal')


# Creación de Variables para la obtención de Datos
miID= StringVar()
miNombre= StringVar()
miApellido= StringVar()
miEmail= StringVar()
miPass= StringVar()



# Botón Salir con alerta
def salirApp():

  salir= messagebox.askquestion('Salir', '¿Desea salir de la aplicación?')

  if salir== 'yes':
    root.destroy()



# Creación de la Base de Datos
conexion= ''
def creaBBDD():

  # Ventana Emergente por sí ya existe la BBDD
  if os.path.isfile('clases/Practica_Guiada/Practica_Guiada1/Usuarios'):

    messagebox.showwarning('BBDD', 'Ya existe una BBDD')


  # Definimos que la variable sea global para que podamos llamarla desde otra función
  global conexion
  global llamada

  conexion= sqlite3.connect('clases/Practica_Guiada/Practica_Guiada1/Usuarios')

  llamada= conexion.cursor()

  llamada.execute('''create table Datos_Usuarios (
                  ID integer primary key autoincrement unique,
                  Nombre_Usuario varchar(50),
                  Apellido varchar(10),
                  Email varchar(50) unique,
                  Password varchar(50),
                  Comentario varchar(100))
  ''')

  messagebox.showinfo('BBDD', 'BBDD Creada Correctamente')

  # Verificación/Confirmación de los cambios
  conexion.commit()



# Añadir Registros
def aniadir():

  conexion= sqlite3.connect('clases/Practica_Guiada/Practica_Guiada1/Usuarios')
  llamada= conexion.cursor()

  datos= miNombre.get(), miApellido.get(), miEmail.get(), miPass.get(), cuadroTexto.get('1.0', END)
  """llamada.execute("insert into Datos_Usuarios values (null, '" + str(miNombre.get()) +
                                                      "','" + str(miApellido.get()) +
                                                      "','" + str(miEmail.get()) +
                                                      "','" + str(miPass.get()) +
                                                      "','" + str(cuadroTexto.get("1.0", END)) + "')")"""
  llamada.execute("insert into Datos_Usuarios values (null, ?, ?, ?, ?, ?)", (datos))
  conexion.commit()

  messagebox.showinfo('BBDD', 'El registro ha sido agregado correctamente.')



# Lectura de Registros
def leer():
  conexion= sqlite3.connect('clases/Practica_Guiada/Practica_Guiada1/Usuarios')
  llamada= conexion.cursor()

  llamada.execute('select * from Datos_Usuarios where ID= ' + miID.get())

  elUsuario=llamada.fetchall()

  for usuario in elUsuario:

    miID.set(usuario[0])
    miNombre.set(usuario[1])
    miApellido.set(usuario[2])
    miEmail.set(usuario[3])
    miPass.set(usuario[4])
    cuadroTexto.insert(1.0, usuario[5])

  conexion.commit()



# Editar Registros
def actualizar():

  conexion= sqlite3.connect('clases/Practica_Guiada/Practica_Guiada1/Usuarios')
  llamada= conexion.cursor()

  datos= miNombre.get(), miApellido.get(), miEmail.get(), miPass.get(), cuadroTexto.get('1.0', END)
  """llamada.execute("update Datos_Usuarios set Nombre_Usuario= '" + miNombre.get() +
                  "', Apellido= '" + miPass.get() +
                  "', Email= '" + miEmail.get() +
                  "', Password= '" + miPass.get() +
                  "', Comentario= '" + cuadroTexto.get('1.0', END) +
                  "' where ID=" + miID.get())"""
  llamada.execute("update Datos_Usuarios set Nombre_Usuario= ?, Apellido= ?, Email= ?, Password= ?, Comentario= ? " +
                  "where ID= " + miID.get(), (datos))
  conexion.commit()

  messagebox.showinfo('BBDD', 'El registro ha sido actualizado correctamente.')



#
def eliminarRegistros():

  conexion= sqlite3.connect('clases/Practica_Guiada/Practica_Guiada1/Usuarios')
  llamada= conexion.cursor()

  llamada.execute("delete from Datos_Usuarios where ID= " + miID.get())

  conexion.commit()

  messagebox.showinfo('BBDD', 'Registro Borrado con Existo')



# Borrar BBDD
def borrarBBDD():

  conexion.close()

  if path.exists('clases/Practica_Guiada/Practica_Guiada1/Usuarios'):

    remove('clases/Practica_Guiada/Practica_Guiada1/Usuarios')

    messagebox.showinfo('BBDD', 'Se ha borrado la BBDD correctamente.')



# Mensaje Acerca de...
def acercaDe():

  messagebox.showinfo('Acerca de...', 'Programa de Base de Datos Personal')



# Texto en medio del ID
def btw(Widget):

  Widget== 'Grey'



# Vaciar Campos
def bCampos():

  cuadroNombre.delete(0, END)
  cuadroApellido.delete(0, END)
  cuadroDireccion.delete(0, END)
  cuadroPassword.delete(0, END)
  cuadroTexto.delete(1.0, END) # "1.0" y "end" se refieren al primer y último carácter del contenido del widget Text



# Creación de la barra de Menú
barraMenu= Menu(root)
root.config(menu= barraMenu)



# Establecer cuantos elementos tendrá el Menú y quitar lagrimas
bbdd= Menu(barraMenu, tearoff= 0)
dlt= Menu(barraMenu, tearoff= 0)
crd= Menu(barraMenu, tearoff= 0)
helpp= Menu(barraMenu, tearoff= 0)



# Creación de los Botónes interactuables del Menú
barraMenu.add_cascade(label= 'BBDD', menu= bbdd)
barraMenu.add_cascade(label= 'Borrar', menu= dlt)
barraMenu.add_cascade(label= 'CRUD', menu= crd)
barraMenu.add_cascade(label= 'Ayuda', menu= helpp)



# Creación de los sub-menús
bbdd.add_command(label= 'Conectar', command= creaBBDD)
bbdd.add_command(label= 'Borrar BBDD', command= borrarBBDD)
bbdd.add_separator() # Separador Horizontal
bbdd.add_command(label= 'Salir', command= salirApp)

crd.add_command(label= 'Create', command= aniadir)
crd.add_command(label= 'Read', command= leer)
crd.add_command(label= 'Update', command= actualizar)
crd.add_command(label= 'Delete', command= eliminarRegistros)

dlt.add_command(label= 'Borrar campos', command= bCampos)

helpp.add_command(label= 'Acerca de...', command= acercaDe)




# Creación de los cuadros
cuadroID= Entry(miFrame, textvariable= miID)
cuadroID.grid(row= 0, column= 1, padx= 7, pady= 7)
cuadroID.config(justify= 'center', font= ('Arial', 10, 'bold'))

cuadroNombre= Entry(miFrame, textvariable= miNombre)
cuadroNombre.grid(row=1, column= 1, padx= 7, pady= 7)
cuadroNombre.config(justify= 'center', font= ('Arial', 10, 'bold'))

cuadroApellido= Entry(miFrame, textvariable= miApellido)
cuadroApellido.grid(row=2, column= 1, padx= 7, pady= 7)
cuadroApellido.config(justify= 'center', font= ('Arial', 10, 'bold'))

cuadroDireccion= Entry(miFrame, textvariable= miEmail)
cuadroDireccion.grid(row=3, column= 1, padx= 7, pady= 7)
cuadroDireccion.config(justify= 'center', font= ('Arial', 10, 'bold'))

cuadroPassword= Entry(miFrame, textvariable= miPass)
cuadroPassword.grid(row=4, column= 1, padx= 7, pady= 7)
cuadroPassword.config(show= '?',justify= 'center', font= ('Arial', 10, 'bold'))

cuadroTexto= ScrolledText(miFrame)
cuadroTexto.grid(row= 5, column= 1, padx= 7, pady= 7)
cuadroTexto.config(width= 14, height= 6, font= ('bold'))



# Creación de los nombres de cuadros
nombreID= Label(miFrame, text= 'ID:', bg= '#3D0875', font= ('Arial', 10, 'bold'))
nombreID.grid(row= 0, column= 0, sticky= 'e', padx= 7, pady= 7)
nombreID.config(fg= 'white')

nombreName= Label(miFrame, text= 'Nombre:', bg= '#3D0875', font= ('Arial', 10, 'bold'))
nombreName.grid(row= 1, column= 0, sticky= 'e', padx= 7, pady= 7)
nombreName.config(fg= 'white')

nombreApellido= Label(miFrame, text= 'Apellido:', bg= '#3D0875', font= ('Arial', 10, 'bold'))
nombreApellido.grid(row= 2, column= 0, sticky= 'e', padx= 7, pady= 7)
nombreApellido.config(fg= 'white')

nombreDireccion= Label(miFrame, text= 'Email:', bg= '#3D0875', font= ('Arial', 10, 'bold'))
nombreDireccion.grid(row= 3, column= 0, sticky= 'e', padx= 7, pady= 7)
nombreDireccion.config(fg= 'white')

nombrePass= Label(miFrame, text= 'Contraseña:', bg= '#3D0875', font= ('Arial', 10, 'bold'))
nombrePass.grid(row= 4, column= 0, sticky= 'e', padx= 7, pady= 7)
nombrePass.config(fg= 'white')

nombreComent= Label(miFrame, text= 'Comentario:', bg= '#3D0875', font= ('Arial', 10, 'bold'))
nombreComent.grid(row= 5, column= 0, sticky= 'e', padx= 7, pady= 7)
nombreComent.config(fg= 'white')



# Creación de los botónes CRUD
botonCreate= Button(root, text= 'Crear', font= ('Arial', 10, 'bold'), command= aniadir)
botonCreate.pack(padx= 5, pady= 7, side= LEFT)

botonRead= Button(root, text= 'Leer', font= ('Arial', 10, 'bold'), command= leer)
botonRead.pack(padx= 5, pady= 7, side= LEFT)

botonUp= Button(root, text= 'Actualizar', font= ('Arial', 10, 'bold'), command= actualizar)
botonUp.pack(padx= 5, pady= 7, side= LEFT)

botonDLT= Button(root, text= 'Borrar', font= ('Arial', 10, 'bold'), command= eliminarRegistros)
botonDLT.pack(padx= 5, pady= 7, side= LEFT)






















# Crear bucle para mantener abierta la GUI
root.mainloop()