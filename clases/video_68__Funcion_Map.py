
"""
    Función Map
  Aplica una función a cada elemento de una lista iterable (listas, tuplas, etc) devolviendo una lista con los resultados.

  Links: (https://www.digitalocean.com/community/tutorials/how-to-use-the-python-map-function-es)
        (https://micro.recursospython.com/recursos/la-funcion-map.html)
"""
class Empleado:

  def __init__(self, nombre, cargo, salario):

    self.nombre= nombre
    self.cargo= cargo
    self.salario= salario

  def __str__(self):

    return "{} que trabaja como {}, tiene un salario de ${}".format(self.nombre, self.cargo, self.salario)

listaEmpleados= [

  Empleado("Juan", "Director", 7000000),
  Empleado("Ana", "Presidenta", 10000000),
  Empleado("Pedro", "Administrador", 5000000),
  Empleado("Manolo", "Limpiador", 2500000),
  Empleado("Pepito", "Botones", 2000000)
]

def calculo_comision(empleado):

  if (empleado.salario <= 5000000):

    empleado.salario= empleado.salario * 1.03

    return empleado

listaEmpleadosComision= map(calculo_comision, listaEmpleados)

for empleado in listaEmpleadosComision:

  print(empleado)

