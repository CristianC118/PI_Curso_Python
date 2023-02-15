
"""
    Listas
  ¿Qué son?:
. Estructura de datos que nos permite almacenar gran cantidad de valores (equivalente a los arrays en otros lenguajes de programación).
. En Python las Listas pueden guardar diferente tipo de valores (en otros lenguajes no ocurre esto con los array).
. Se pueden expandir dinámicamente añadiendo nuevos elementos (otra novedad respecto a los array).

- Las Listas van entre corchetes.
- Los elementos comienzan desde el número/índice 0
"""

# La Lista contiene 4 elementos pero se cuentan desde el 0 hasta 3
miLista= ['María', 5, True, 'Antonio']
print(miLista)

# Acceder a un elemento en concreto (Marta) con el índice
print(miLista[1])

# Al acceder desde la última posición con números negativos se cuenta desde el elemento/índice 1
print(miLista[-1])

# Acceder a una porción de la Lista (accede a los tres primeros elementos)
# Se puede omitir el primer índice sí se quiere acceder desde el primer elemento
print(miLista[0:3])

# Accede al segundo elemento
print(miLista[1:2])

# Accede desde el índice dos hasta el final de la Lista
print(miLista[2:])

# .append: agregar elementos a la Lista (lo agrega al final)
miLista.append('Sandra')

# .insert: sirve para agregar elementos a la Lista en la posición deseada
miLista.insert(2, 'Sandra')

# .extend: agregar varios elementos a la Lista (los agrega al final)
miLista.extend([78.3, 'Ana', 'Lucía'])
print(miLista)

# .index: nos devuelve el índice de un elemento (pero sí hay más de un mismo elemento devolerá el primero)
print(miLista.index('Antonio'))

# in: comprueba sí un elemento se encuentra o no dentro de una Lista
print('Pepe'in miLista)

# remove: sirve para eliminar elementos
miLista.remove('Ana')
print(miLista)

# .pop: sirve para eliminar el último elemento de una Lista
miLista.pop()
print(miLista)


miLista2= ['Sandra', 'Lucia']

# Sumar/Unir Listas (en total hay tres Listas)
miLista3= miLista + miLista2
print(miLista3)

# Multiplicar Listas con *, se coloca al final de una de estas fuera del corchete.

"""
  Nota: Link directo a la documentación oficial de Listas en Python (En español)
(https://docs.python.org/es/3/tutorial/introduction.html#lists)
(https://docs.python.org/es/3/tutorial/datastructures.html#more-on-lists)
"""
