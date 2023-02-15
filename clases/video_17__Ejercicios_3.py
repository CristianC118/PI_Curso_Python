
"""Ejercicio 1:
• Crea un programa que pida números infinitamente. Los números introducidos deben
ser cada vez mayores El programa finalizará cuando se introduce un número menor que
el anterior."""


def infinito():

  numero1= int(input('Introduce el primer número: '))
  numero2= int(input('Introduce el segundo número: '))

  while numero1 < numero2:
    print('Sigue así...')

    numero1= int(input('Introduce otro número: '))
    numero2= int(input('Introduce números cada vez mayor: '))

    if numero2 < numero1:
      print('Haz introducido un número igual o menor que el anterior. \nFinalizando...')
      break

infinito()


"""Ejercicio 2:
• Crea un programa que pida números positivos indefinidamente. El programa termina
cuando se introduce un número negativo. Finalmente el programa muestras la suma de
todos los números introducidos"""


def positivo():

  numero= int(input('Introduce solo números positivos: '))
  suma= 0

  while numero >= 0:
    print('Sigue así...')

    suma= suma + numero
    numero= int(input('Introduce solo números positivos: '))

    if numero < 0:
      print('Haz introducido un número negativo. \nFinalizando...')
      print(f'La suma total de los número introducidos es de: {suma}')
      break

positivo()