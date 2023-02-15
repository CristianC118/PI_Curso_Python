
"""
    POO Herencia

  ¿Qué es?
- Se trata de trasladar el comportamiento de la herencia entre personas de la vida real a código de programción.

Se dividen entre jerarquias:

  Clase 1 - Clase Padre o Super Clase
    Clase 2 - SubClase y a su vez Clase Padre o Super Clase de las Clases venideras.
      Clase 3, 4, 5

    Sirve para:
- Para reutilizar código en caso de crear objetos similares.
"""

# N° 1_a
# Creación de Super Clase
class Vehiculos():

  # N° 2_a
  # Crear Constructor
  def __init__(self, marca, modelo):

    # N° 3_a
    self.marca= marca
    self.modelo= modelo
    self.enmarcha= False
    self.acelera= False
    self.frena= False

  # N° 4_a
  # Definiendo Comportamientos
  def arrancar(self):
    self.enmarcha= True

  def acelerar(self):
    self.acelera= True

  def frenar(self):
    self.frena= True

  # N° 5_a
  # Imprimiendo estados
  def estado(self):
    print(f'Marca: {self.marca} \nModelo: {self.modelo} \nEn Marcha: {self.enmarcha} \nAcelerando: {self.acelera} \nFrenando: {self.frena}')

# N° 6_a
# Creación de la Herencia
class Moto(Vehiculos):
  pass

# N° 7_a
# Creación de una Instancia - Se le debe pasar los parámetros
miMoto= Moto('Hona', 'CBR')

miMoto.estado()

"""
    Nota: Documentación a la Herencia en Python
(https://www.geeksforgeeks.org/inheritance-in-python/?ref=lbp)
"""