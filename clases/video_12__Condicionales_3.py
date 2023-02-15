
"""
    Concatenación de operadores de comparación
    Operadores Lógicos'and' (y sí adémas) y 'or' (o sino)
    Operador 'in'
"""

edad= -7

if  0 < edad < 100:
  print('Edad Correcta')

else:
  print('Edad Incorrecta')


print(' ')


presidente= int(input('Introduce el salario del presidente: '))
print(f'Salario del Presidente: {presidente}')

director= int(input('Introduce el salario del Director: '))
print(f'Salario del Presidente: {director}')

jefe_area= int(input('Introduce el salario del Jefe de Área: '))
print(f'Salario del Presidente: {jefe_area}')

administrativo= int(input('Introduce el salario del Administrativo: '))
print(f'Salario del Presidente: {administrativo}')

if administrativo < jefe_area < director < presidente:
  print('Todo funciona correctamente')

else:
  print('Algo falla en esta empresa')


"""
    Nota: Más acerca de condiciones:
(https://docs.python.org/es/3/tutorial/datastructures.html#more-on-conditions)
"""
