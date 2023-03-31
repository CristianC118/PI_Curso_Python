
"""
    Función Filter
	Verifica que los elementos de una secuencia cumplen una condición, devolviendo un iterador con los elementos que cumplen dicha condición.

  Links: (https://www.digitalocean.com/community/tutorials/how-to-use-the-python-filter-function-es)
        (https://morioh.com/p/106a03d5720b)
        (https://www.codigopiton.com/como-filtrar-una-lista-en-python/)
"""

"""def numero_par(num):

  if num % 2== 0:

    return True"""

numeros= [17, 24, 7, 39, 8, 51, 92]

print(list(filter(lambda numero_par: numero_par % 2== 0, numeros)))


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

salario_altos= filter(lambda empleado: empleado.salario>= 5000000, listaEmpleados)

for empleado_salario in salario_altos:

  print(empleado_salario)