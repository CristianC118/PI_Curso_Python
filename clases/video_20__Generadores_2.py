
"""
    Generadores

  yield from: simplificar el código de los generadores en el caso de utilizar bucles anidados.
"""

# cuando se coloca un * delante del parámetro, le índicamos al programa que recibirá un número indeterminado de elementos, y estos los recibirá en formad de tupla
def devuelve_ciudades(*ciudades):

  for elemento in ciudades:

    #for subElemento in elemento:
      yield from elemento

ciudades_devueltas= devuelve_ciudades('Madrid', 'Barcelona', 'Bilbao', 'Valencia')
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))