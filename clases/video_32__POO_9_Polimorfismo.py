

"""
    Polimorfismo:

  ¿Qué es?
- Un objeto puede cambiar de forma dependiendo del contexto en el que se utilice.
- Sí se da Polimorfismo un mismo objeto puede cambiar de forma. Por lo tanto ese mismo objeto cambiaría su comportamiento dependiendo del contexto en que el que se utilice.
"""

class Coche():

  def desplazamiento(self):
    print('Me desplazo utilizando cuatro ruedas')


class Moto():

  def desplazamiento(self):
    print('Me desplazo utilizando dos ruedas.')


class Camion():

  def desplazamiento(self):
    print('Me desplazo utilizando seis ruedas.')


# N° 1
def desplazamientoVehiculo(vehiculo): # En vehiculo ocurre el polimorfismo
  vehiculo.desplazamiento()

# N° 2
miVehiculo= Coche()
# N° 3
desplazamientoVehiculo(miVehiculo)


"""
    Nota: Documentación del Polimorfismo en Python
(https://www.geeksforgeeks.org/polymorphism-in-python/?ref=lbp)
"""