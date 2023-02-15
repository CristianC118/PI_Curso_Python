
"""
    POO Herencia 2

- Sobree scritura de Métodos
- Herencia Multiple
"""

# N° 1_a
class Vehiculos():

  # N° 2_a
  def __init__(self, marca, modelo):

    # N° 3_a
    self.marca= marca
    self.modelo= modelo
    self.enmarcha= False
    self.acelera= False
    self.frena= False

  # N° 4_a
  def arrancar(self):
    self.enmarcha= True

  def acelerar(self):
    self.acelera= True

  def frenar(self):
    self.frena= True

  # N° 5_a
  def estado(self):
    print(f'Marca: {self.marca} \nModelo: {self.modelo} \nEn Marcha: {self.enmarcha} \nAcelerando: {self.acelera} \nFrenando: {self.frena}')

# N° 6_a
class Moto(Vehiculos):

  # N° 1_b
  # Creando Comportamiento/propipedad
  hcaballito= ''

  # N° 2_b
  # Creación de método que da un valor diferente al creado anteriormente
  def caballito(self):
    self.hcaballito= 'Voy haciendo el caballito'

  # N° 3_b
  # Sobre escribiendo el método estado
  def estado(self):
    print(f'Marca: {self.marca} \nModelo: {self.modelo} \nEn Marcha: {self.enmarcha} \nAcelerando: {self.acelera} \nFrenando: {self.frena} \n{self.hcaballito}')

# N° 7_a
miMoto= Moto('Hona', 'CBR')

# N° 4_b
miMoto.caballito()

miMoto.estado()


print('\n*****************\n')

# N° 5_b
class Furgoneta(Vehiculos):

  # N° 6_b
  # Creando comportamiento
  def carga(self, cargar):

    # N° 7_b
    self.cargado= cargar

    # N° 8_b
    if self.cargado== True:
      return 'La furgoneta esta cargada'

    # N° 9_b
    else:
      return 'La furgoneta no esta cargada'

# N° 10_b
# Creando Instancia
miFurgoneta= Furgoneta('Renault', 'Kangoo')

# N° 11_b
miFurgoneta.arrancar()
miFurgoneta.estado()
miFurgoneta.carga(True)


print('\n*****************\n')


# N° 12_b
class VElectricos():

  # N° 13_b
  # Creando Constructor
  def __init__(self):

    self.autonomia= 100

  # N° 14_b
  # Comportamiento
  def cargarEnergia(self):

    self.cargando= True

# N° 15_b
# Herencia Multiple
class BicicletaElectrica(Vehiculos, VElectricos):
  pass

# Cuando hay Herencia multiple se le da preferencia siempre a la primera clase que índiques en la herencia multiple
miBici= BicicletaElectrica()


"""
    Nota: Documentación sobre la Herencia y Multiple Herencia en Python
(https://www.geeksforgeeks.org/types-of-inheritance-python/?ref=lbp)
"""