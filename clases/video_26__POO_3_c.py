
"""
    POO 3

- Creación de clases
- Instancia/Objeto/Ejemplar
"""

# N° 1_c
# Creación de la clase
class Coche():

  # N° 2_c
  # Propiedades
  largoChasis= 250
  anchoChasis= 120
  ruedas= 4
  enmarcha= False

  # N° 3_c
  # Comportamiento - Métodos: No es más que una función especial que pertenece a la clase que se está creando. Una función normal no pertenece a nadie.
  def arrancar(self): # parámetro por defecto self: hace referencia al propio objeto perteneciente a la clase o instancia perteneciente a la clase.

    # N° 6_c
    # Cambiar valor de la propiedad (enmarcha)
    self.enmarcha= True

  # N° 7_c
  # Cambiamos el estado/comportamiento
  def estado(self):

    if (self.enmarcha):
      return 'El coche está en marcha'

    else:
      return 'El coche está parado'
    pass

# N° 4_c
# Objeto/Instancia o ejemplar perteneciente a la clase 'Coche'
miCoche= Coche() # Instanciar una clase

# N° 5_c
# Acceder a las propiedades - Nomenclatura del punto
print(f'El largo del coche es: {miCoche.largoChasis}')
print(f'El coche tiene {miCoche.ruedas} ruedas.')

# Activamos el estado del coche
miCoche.arrancar()
print(miCoche.estado())


"""
  La clase 'Coche' tiene 4 propiedades y 2 comportamientos.
"""

"""
    Nota: Documentación de Clases en Python
(https://www.geeksforgeeks.org/python-classes-and-objects/?ref=lbp)
"""