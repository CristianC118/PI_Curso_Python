
"""
  Operadores Lógicos'and' (y sí adémas) y 'or' (o sino)
  Operador 'in'
"""

distancia= int(input('Introduce la Distancia a la escuela en Km: '))
print(f'La Distancia es {distancia} km\n')

hermanos= int(input('Introduce el número de hermanos: '))
print(f'El número de hermanos es de {hermanos}\n')

salario= int(input('Introduce el salario total anual: '))
print(f'El salario neto anual es de {salario} Gs.\n')

if distancia > 40 and hermanos > 2 or salario <= 20000000:

  print('Tienes derecho a beca.')

else:

  print('No tienes derecho  a beca.')



print('\n')

# Forma N° 1
print('Asignaturas Optativas')
print('Informática Gráfica - Pruebas de Software - Usabilidad y Accesibilidad\n')

asignatura= input('Introduce la Asignatura escogida: ')

if asignatura in ('Informática Gráfica', 'Pruebas de Software', ' Usabilidad y Accesibilidad'):

  print(f'\nLa asignatura escogida es: {asignatura}.')

else:
  print(f'\nLa asignatura "{asignatura}" escogida no está contemplada.')


# Python es 'case sensitive': fuerte distinción entre mayúsculas y minúsculas.
# lower() transforma es minúsculas
# upper() transforma es mayúsculas


# Forma N° 2
print('Asignaturas Optativas')
print('Informática Gráfica - Pruebas de Software - Usabilidad y Accesibilidad\n')

opcion= input('Introduce la Asignatura escogida: ')

asignatura= opcion.lower()

if asignatura in ('informática gráfica', 'pruebas de software', ' usabilidad y accesibilidad'):

  print(f'\nLa asignatura escogida es: {asignatura}.')

else:
  print(f'\nLa asignatura "{asignatura}" escogida no está contemplada.')


print('\n')

# Forma N° 3
print('Asignaturas Optativas...\n')
print('1 - Informática Gráfica  \n2 - Pruebas de Software \n3 - Usabilidad y Accesibilidad\n')

asignaturas= {1: 'Informática Gráfica', 2: 'Pruebas de Software', 3: 'Usabilidad y Accesibilidad'}
eleccion= int(input(f'Digita el número de la asignatura que quieras elegir: '))

if eleccion in (1, 2, 3):
  print(f'\nLa asignatura escogida es {asignaturas[eleccion]}')

else:
  print('La asignatura no está Disponible')


print('\n')

print('Asignaturas Optativas...\n')
print('1 - Informática Gráfica  \n2 - Pruebas de Software \n3 - Usabilidad y Accesibilidad\n')

opcion= input('Introduce la Asignatura escogida: ').casefold()

asignatura= opcion

if asignatura in ('informática gráfica', 'pruebas de software', ' usabilidad y accesibilidad'):

  print(f'\nLa asignatura escogida es: {asignatura.capitalize()}.')

else:
  print(f'\nLa asignatura "{asignatura}" escogida no está contemplada.')


# .casefold() acepta mayúsculas y minúsculas
# .capitalize() duvuelve el contenido inicial con mayúscula