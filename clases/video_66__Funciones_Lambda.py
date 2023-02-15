
"""
    Funciones Lambda (= Función Anónima)
  Se utilizan en Python para abreviar para que la sintaxis sea más ligera y para ahorrar tiempo.

  En funciones que son complejas no se pueden resumir o transoformar en funciones Lambda (Bucles, Condicional)
"""

# Ejemplo Función Normal
def area_triangulo(base, altura):

  return (base * altura) / 2


# Ejemplo Función Lambda 1
triangulo= lambda base, altura: (base * altura) / 2
# los dos puntos equivalen a un return

print(triangulo(7, 5))


# Ejemplo Función Lambda 2
cubo= lambda numero:pow(numero, 3)
# Función pow() pide 2 argumentos

print(cubo(13))


# Ejemplo Función Lambda 3
destacarValor= lambda comision: '¡{}! $'.format(comision)

comision_Ana= 15585

print(destacarValor(comision_Ana))