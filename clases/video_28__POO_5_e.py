
"""
    POO 5

- Encapsulando Métodos
"""

class Coche():

  # <-N° 6_d
  def __init__(self):

    # <-N° 7_d
    self.__largoChasis= 250
    self.__anchoChasis= 120
    self.__ruedas= 4
    self.__enmarcha= False

  # <-N° 2_d
  def arrancar(self, arrancamos):

    # <-N° 3_d
    self.__enmarcha= arrancamos

    # N° 4_e
    # Llamada al Chequeo Interno
    if self.__enmarcha== True:
      chequeo= self.__chequeo_interno()

    # <-N° 4_d
    # N° 5_e
    # Agregar parámetro para saber si se arranco y sí el chequeo dio True
    if self.__enmarcha and chequeo== True:
      return 'El coche está en marcha'

    # N° 6_e
    # Comprabar si el coche está en marcha
    elif self.__enmarcha and chequeo== False:
      return 'Algo ha ido mal en el chequeo. No podemos arrancar.'

    else:
      return 'El coche está parado'


  def estado(self):
    # <-N° 4.1_d
    print(f'El coche tiene {self.__ruedas} ruedas. \nUn ancho de {self.__anchoChasis} y un largo de {self.__largoChasis}.')

  # N° 1_e
  # Empezando a Encapsular Métodos
  def __chequeo_interno(self):
    print('Realizando Chequeo Interno...')

    # N° 2_e
    # Creación de estados/variables
    self.gasolina= 'Ok'
    self.aceite= 'Ok'
    self.puertas= 'Cerradas'

    # N° 3_e
    if self.gasolina== 'Ok' and self.aceite== 'Ok' and self.puertas== 'Cerradas':
      return True

    else:
      return False


miCoche= Coche()

# <-N° 5_d
print(miCoche.arrancar(True))
miCoche.estado()


print('\n------------- Creación del segundo objeto --------------\n')


# <-N° 1_d
miCoche2= Coche()

# <-N° 5_d
print(miCoche2.arrancar(False))
miCoche2.estado()


"""
  Para Encapsular variables o métodos cuando tu objeto así lo necesito y dependerá del comportamiento de la clase.
"""