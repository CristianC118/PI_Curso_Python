

"""
    POO Herencia 3

- super() donde la coloques en tu código llama al método de la clase padre
- isinstance() cuando tenemos Herencia, un objeto de la subClase siempre será un objeto de la SuperClase
"""

class Vehiculos():

  def __init__(self, marca, modelo):

    self.marca= marca
    self.modelo= modelo
    self.enmarcha= False
    self.acelera= False
    self.frena= False

  def arrancar(self):
    self.enmarcha= True

  def acelerar(self):
    self.acelera= True

  def frenar(self):
    self.frena= True

  def estado(self):
    print(f'Marca: {self.marca} \nModelo: {self.modelo} \nEn Marcha: {self.enmarcha} \nAcelerando: {self.acelera} \nFrenando: {self.frena}')

class Moto(Vehiculos):

  # N° 1_b
  hcaballito= ''

  # N° 2_b
  def caballito(self):
    self.hcaballito= 'Voy haciendo el caballito'

  # N° 3_b
  def estado(self):
    print(f'Marca: {self.marca} \nModelo: {self.modelo} \nEn Marcha: {self.enmarcha} \nAcelerando: {self.acelera} \nFrenando: {self.frena} \n{self.hcaballito}')

miMoto= Moto('Hona', 'CBR')

# N° 4_b
miMoto.caballito()

miMoto.estado()


print('\n*****************\n')


# N° 5_b
class Furgoneta(Vehiculos):

  # N° 6_b
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
miFurgoneta= Furgoneta('Renault', 'Kangoo')

# N° 11_b
miFurgoneta.arrancar()
miFurgoneta.estado()
miFurgoneta.carga(True)


print('\n*****************\n')


# N° 12_b
class VElectricos(Vehiculos):

  # N° 13_b
  def __init__(self, marca, modelo):

    # N° 1_c
    super().__init__(marca, modelo)

    self.autonomia= 100

  # N° 14_b
  def cargarEnergia(self):

    self.cargando= True

# N° 15_b
class BicicletaElectrica(VElectricos, Vehiculos):
  pass

miBici= BicicletaElectrica('Orbea', 'hp1500')



print('\nCódigo N° 2\n')


class Persona():

  def __init__(self, nombre, edad, LugarResidencia):

    self.nombre= nombre
    self.edad= edad
    self.LugarResidencia= LugarResidencia

  def descripcion(self):

    print(f'Nombre: {self.nombre} \nEdad: {self.edad} \nLugar de Residencia: {self.LugarResidencia}')


class Empleado(Persona):

  def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):

    super().__init__(nombre_empleado, edad_empleado, residencia_empleado)

    self.salario= salario
    self.antiguedad= antiguedad

  def descripcion(self):

    super().descripcion()

    print(f'Salario: {self.salario} \nAntiguedad: {self.antiguedad}')


Antonio= Persona('Marcoh', 55, 'España')

Antonio.descripcion()