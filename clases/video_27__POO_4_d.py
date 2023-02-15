
"""
    POO 4

- Crear segundo objeto que pertenezca a la misma clase.
- 'Constructor' es un método especial que le da estado inicial a los objetos.
- Encapsulación: proteger una propiedad para que no se modifique desde fuera de la clase.
"""

# <-N° 1_c
class Coche():

  # N° 6_d
  # Creación de un constructor para dar estado inicial a los objetos de una clase.
  def __init__(self):

    # <-N° 2_c
    # N° 7_d
    # Colocamos la palabra self en las propiedades
    # Con dos guines bajos encapsulamos las variables desde el exterior de la clase pero si será accesible desde dentro de la clase.
    self.__largoChasis= 250
    self.__anchoChasis= 120
    self.__ruedas= 4
    self.__enmarcha= False

  # <-N° 3_c
  # N° 2_d
  # Introdicir un parámetro para que informe el estado
  def arrancar(self, arrancamos):

    # N° 3_d
    self.__enmarcha= arrancamos

    # N° 4_d
    if self.__enmarcha== True:
      return 'El coche está en marcha'

    else:
      return 'El coche está parado'

    # <-N° 6_c
    #self.enmarcha= True

  # <-N° 7_c
  # N° 4.1_d
  def estado(self):
    # Si encapsulamos la variable el nombre también deberá ser cambiado.
    print(f'El coche tiene {self.__ruedas} ruedas. \nUn ancho de {self.__anchoChasis} y un largo de {self.__largoChasis}.')


# <-N° 4_c
miCoche= Coche() # Instanciar una clase

"""# <-N° 5_c
print(f'El largo del coche es: {miCoche.largoChasis}')
print(f'El coche tiene {miCoche.ruedas} ruedas.')"""

# N° 5_d
# Pasamos argumento y esta vez imprimimos el estado
print(miCoche.arrancar(True))
miCoche.estado()


print('\n------------- Creación del segundo objeto --------------\n')


# N° 1_d
# Creación segunda instancia
miCoche2= Coche()

# N° 5_d
# Pasamos argumento y esta vez imprimimos el estado
print(miCoche2.arrancar(False))

# Aunque se cambie el nombre este ya no podrá acceder a los parámetros desde fuera de la clase.
miCoche2.__ruedas= 2

miCoche2.estado()


"""
    Nota: Documentación sobre POO Constructor y Encapsulación en Python
(https://www.geeksforgeeks.org/constructors-in-python/?ref=lbp)
(https://www.geeksforgeeks.org/encapsulation-in-python/?ref=lbp)
"""