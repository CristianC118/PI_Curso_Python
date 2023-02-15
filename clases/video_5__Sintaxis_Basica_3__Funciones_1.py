
"""
  Funciones
    . Conjunto de líneas de código agrupadas (bloque de código) que funcionan como una unidad realizando una tarea específica.
    . Las funciones en Python pueden o no devolver valores.
    . Las funciones en Python tener parámetros/argumentos.
    . A las funciones también se las denomina "métodos" cuando se encuentran definidas dentro de una clase.

- Utilidad:
  Reutilización de código (cuando sea necesario o sí es necesario)

- Sintaxis:

def nombre_función():
  . Instrucciones de la función
  . return (opcional)

def nombre_función(parámetros):
  . Instrucciones de la función
  . return (opcional)

- Ejecución:

. nombre_función()

. nombre_función(parámetros)
"""

def mensaje(): # Declaración de la función

  # Cuerpo de la función
  print('Mensaje 1')
  print('Mensaje 2')
  print('Mensaje 3')

mensaje() # Llamada de la función

# El flujo de ejecución de un programa siempre va de arriba hacía abajo, excepto cuando se encuentre con funciones y bucles.

print('Ejecutando código fuera de función')
mensaje()

"""
  Nota: Link directo a la documentación oficial de funciones en Python (En español)
(https://docs.python.org/es/3/tutorial/controlflow.html#defining-functions)
"""
