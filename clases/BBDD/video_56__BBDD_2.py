
"""
    Bases de Datos

  Inserción de varios registros
  Lectura de varios registros
"""

# Importar Librería
import sqlite3

# Crear y Abrir BBDD
miConexion= sqlite3.connect('clases\BBDD\PrimeraBBDD')

# Creación y llamada del puntero
miCursor= miConexion.cursor()

# Ejecutar la consulta
#miCursor.execute('create table Productos (Nombre_Articulo varchar(50), Precio integer, Seccion varchar(20))')

# Agregar datos a la BBDD
#miCursor.execute('insert into Productos values ("Balón", 15, "Deportes")')

"""# Inserción de registros
variosProductos= [

  ('Camiseta', 10, 'Deportes'),
  ('Jarrón', 90, 'Cerámica'),
  ('Camión', 20, 'Juguetes')

]

# Método para agregar varios registros
miCursor.executemany('insert into Productos values (?, ?, ?)', variosProductos)"""

# Lectura de datos
miCursor.execute('select * from Productos')

# Ver la información
listaProductos= miCursor.fetchall()

# Recorrer BBDD elemento x elemento
for producto in listaProductos:
  print(f'Nombre del Articulo: {producto[0]} | Sección: {producto[2]}')



# Vericación/Confirmación del cambio
miConexion.commit()







# Cerrar BBDD
miConexion.close()