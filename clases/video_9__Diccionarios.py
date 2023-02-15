
"""
    Diccionarios
	¿Qué son?
. Estructura de datos que nos permite almacenar valores de diferente tipo (enteros, cadenas de texto, decimales) e incluso listas y otros Diccionarios.
. La principal característica de los Diccionarios es que los datos se almacenan asociados a una clave de tal forma que se crea una asociación de tipo clave: valor para cada elemento almacenado.
. Los elementos almacenados no están ordenados. El orden es indiferente a la hora de almacenar información en un Diccionario.

- Los Diccionarios van entre Llaves
"""

miDiccionario= {'Alemania': 'Berlín', 'Francia': 'Paris', 'Inglaterra': 'Londres', 'España': 'Madrid'}

# Acceder a una clave:valor en concreto
print(miDiccionario['Francia'])

# Agregar elementos a un Diccionario
miDiccionario['Italia']= 'Lisboa'
print(miDiccionario)

# En un Diccionario se sobreescriben los datos
miDiccionario['Italia']= 'Roma'
print(miDiccionario)

# del: Eliminar elementos
del miDiccionario['Inglaterra']
print(miDiccionario)

# Utilizar Tupla para asignar clave a cada valor
tupla= ('España', 'Francia', 'Inglaterra', 'Alemania2')
diccionario=  {tupla[0]: 'Madrid',tupla[1]: 'Paris', tupla[2]: 'Londres', tupla[3]: 'Berlín'}
print(diccionario)

# Tupla y Diccionario dentro de un Diccionario
dicc= {23: 'Jordan', 'Nombre': 'Michael', 'Equipo': 'Chicago', 'Anillos': {'Temporadas': [1991, 1992, 1993, 1996, 1997, 1998]}}
print(dicc)

# .keys: devuelve la clave de un Diccionario
print(dicc.keys())

# .values: devuelve el valor de un Diccionario
print(dicc.values())

# len(): devuelve la longitud de un Diccionario
print(len(dicc))


"""
	Nota: Link directo a la documentación oficial de Diccionarios en Python (En español)
(https://docs.python.org/es/3/tutorial/datastructures.html#dictionaries)
"""
