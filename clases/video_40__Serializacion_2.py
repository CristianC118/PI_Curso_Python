
"""
    Serialización (Objetos)
"""

# N° 1
import pickle

class Vehiculo():

  def __init__(self, marca, modelo):

    self.marca= marca
    self.modelo= modelo
    self.enmarcha= False
    self.acelera= False
    self.frena= False

  def arrancar(self):
    self.enmarcha= True

  def acelera(self):
    self.acelera= True

  def frenar(self):
    self.frena= True

  def estado(self):
    print(f'Marca: {self.marca} \nModelo: {self.modelo} \nEn Marcha: {self.enmarcha} \nAcelerando: {self.acelera} \nFrenando: {self.frena}')

coche1= Vehiculo('Mazda', 'MX5')

coche2= Vehiculo('Seat', 'Leon')

coche3= Vehiculo('Renault', 'Megane')

# N° 2
coches= [coche1, coche2, coche3]

# N° 3
fichero2= open('video_40_losCoches', 'wb')

# N° 4
pickle.dump(coches, fichero2)

# N° 5
fichero2.close()

del (fichero2)


# N° 6
# Abrimos el fichero de nuevo
ficheroApertura= open('video_40_losCoches', 'rb')

# N° 7
misChoches= pickle.load(ficheroApertura)

# N° 8
ficheroApertura.close()

# N° 9
# Recorremos la info dentro de miCoches
for c in misChoches:

  print(c.estado())

"""
    Nota: Documentación de la Serialización con pickle en Python
(https://pyspanishdoc.sourceforge.net/lib/module-pickle.html)
"""