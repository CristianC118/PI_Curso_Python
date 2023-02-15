
"""
    Bases de Datos

  Creación de BBDD
    - Conexión con BBDD
    - Inserción de registros en BBDD

      Pasos a seguir para conectar con BBD
        1- Abrir/Crear conexión
        2- Crear puntero:
          Objeto que nos permite ejecutar querys y manejar los resultados.
        3- Ejecutar query SQL
        4- Manejar los resultados de la query:
          Insertar, Leer, Actualizar, Borrar (Create, Read, Update, Delete)
        5- Cerrar Puntero
        6- Cerrar conexión
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
miCursor.execute('insert into Productos values ("Balón", 15, "Deportes")')

# Vericación/Confirmación del cambio
miConexion.commit()







# Cerrar BBDD
miConexion.close()