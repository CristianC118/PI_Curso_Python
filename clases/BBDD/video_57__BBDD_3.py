
"""
    Bases de Datos

  Claves Principales de BBDD
"""

# Importar Librería
import sqlite3

# Crear y Abrir BBDD
miconexion= sqlite3.connect('clases\BBDD\GestionProductos')

# Creación y llamada del puntero
micursor= miconexion.cursor()

# Creación de la Tabla
micursor.execute('''
  create table PRODUCTOS_2 (
  ID integer primary key autoincrement,
  Nombre_Articulo varchar(50),
  Precio interger,
  Seccion varchar(20))
''')

# Agregación de los registros
productos= [

  ('Pelota', 20, 'Juguetes'),
  ('Pantalón', 15, 'Confección'),
  ('Destornillador', 25, 'Ferretería'),
  ('Jarrón', 45, 'Cerámica')

]

# Creación de la BBDD con la Tabla
micursor.executemany('insert into PRODUCTOS_2 values (null, ?, ?, ?)', productos)




# Vericación/Confirmación del cambio
miconexion.commit()


# Cerrar BBDD
miconexion.close()