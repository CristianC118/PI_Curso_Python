
"""
    Tuplas
  ¿Qué son?
. Las Tuplas son listas inmutables, es decir, no se pueden modificar después de su creación.
  - No permiten añadir, eliminar mover elementos, etc (no append, extend, remove).
  - Si permiten extraer porciones, pero el resultado de la extracción es una Tupla nueva.
  - Si permiten comprobar si un elemento se encuentra en la Tupla.

  ¿Qué utilidad o ventaja tienen respecto a las Listas?
. Más rápidas
. Menos espacio (mayor optimización)
. Formatean strings
. Pueden utilizarce como claves en un diccionario. Las Listas no.

- Las Tuplas van entre paréntesis
- Las Tuplas pueden ir sin paréntesis pero es recomendable usarlas
"""

# Acceder a un elemento en concreto
miTupla= ('Juan', 13, 1, 1995)
print(miTupla[2])

print('----------------------------')

# list(): Convertir una Tupla en Lista
miLista= list(miTupla)
print(f'Esto es una Lista {miLista}')
print(f'Esto es una Tupla {miTupla}')

# tuple(): Convertir una Lista en Tupla
ejemLista= ['Lalo', 'Roberto', 'Juan']
ejemTupla= tuple(ejemLista)
print(f'Esto es una Tupla {ejemTupla}')

# in: Saber sí un elemento se encuentra o no dentro de una Tupla
print('Juan' in miTupla)

# .count: cuenta la cantidad de elementos que hay repetidos
print(miTupla.count(13))

# len(): permite averiguar la longitud/cantidad de elementos de una Tupla
print(len(miTupla))

# crear Tupla Unitaria, se coloca una coma al final
tupla= ('Ramiro',)

# Desempaquetado de Tupla
nombre, dia, mes, anio= miTupla
print(nombre)
print(dia)
print(anio)
print(mes)


"""
  Nota: Link directo a la documentación oficial de Tupla en Python (En español)
(https://docs.python.org/es/3/tutorial/datastructures.html#tuples-and-sequences)
"""
