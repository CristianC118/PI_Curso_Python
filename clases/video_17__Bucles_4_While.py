
"""
    Bucle: while (mientras)

  Ejemplo de Bucle Infinito:

i= 1

while i <= 10:
  print (f'Ejecución N° {i}')
"""

i= 0

while i <= 10:
  i += 1
  print(f'Ejecución N° {i}')

print('\nFin de la Ejecución\n')


print('\n')


# Ejemplo N° 1 (Podría ser Bucle Infinito)

edad= int(input('Introduce la edad: ')) # N° 1

while edad < 0: # N° 2

  print('Has introduce una edad negativa. Vuelve a intentarlo.') # N° 3
  edad= int(input('Introduce la edad: ')) # N° 4

print('Gracias por colaborar. Puedes Pasar.') # N° 5
print(f'La edad del aspirante es {edad}.') # N° 6


print('\n')


# Ejemplo N° 2 (Podría ser Bucle Infinito)

edad= int(input('Introduce la edad: ')) # N° 1

while edad < 5 or edad > 100: # N° 2

  print('Has introduce una edad incorrecta. Vuelve a intentarlo.') # N° 3
  edad= int(input('Introduce la edad: ')) # N° 4

print('Gracias por colaborar. Puedes Pasar.') # N° 5
print(f'La edad del aspirante es {edad}.') # N° 6


print('\n')


# Ejemplo N° 3

import math # N° 12.1

print('Programa de calculo de raíz cuadrada')

numero= int(input('Introduce un número: ')) # N° 1

intentos= 0 # N° 2

while numero < 0: # N° 3

  print('No se puede hallar la  raíz de un número negativo.') # N° 4

  if intentos == 2: # N°  5
    print('Has consumido demasiados intentos. El programa ha finalizado') # N° 6
    break; # N° 7 - La instrucción 'break' sale del bucle

  numero= int(input('Introduce un número: ')) # N° 8

  if numero < 0: # N° 9
    intentos += 1 # N° 10

if  intentos < 2: # N° 11
  solucion= math.sqrt(numero) # N° 12.0
  print(f'La raíz cuadrada de {numero} es {solucion}')


# Con 'cmath' podemos hallar raíz cuadrada de números negativos

"""
    Nota: Link a Documentación de while en Pyton
(https://www.geeksforgeeks.org/python-while-loop/?ref=lbp)
"""