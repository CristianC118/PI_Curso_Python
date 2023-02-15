
"""
  Tipos, Operadores y Variables

Tipos:
    Numéricos: Enteros (int), Flotante (float), Complejos
    Textos
    Booleanos: True y False

Operadores:
    Aritméticos:
      Suma y Resta (+, -), Multiplicacación y División (*, /), Módulo(%), Exponente (**), División Entera (//)

    Comparación:
      Igual que (==), Diferente que(!=), Mayor que (>), Menor que (<), Mayor o igual (>=), Menor o igual (<=)

    Lógicos:
      and, or, not

    Asignación:
      Igual (=), Incremento (+=), Decremento (-=), (*=), (/=), (%=), (**=), (//=)

    Especiales:
      is, is not, in, not in
"""

# Módulo: Devuelve el resto de una división
print(10 % 3)

# Div. Entera: Devuelve valor sin decimales
print(9 // 2)

# El tipo de Variable lo establece el contenido no el contenedor
# en Python todo es un objeto

nombre0= 5
print(f'La variable nombre0 es de tipo: {type(nombre0)}')

nombre1= 'Cristian'
print(f'La variable nombre1 es de tipo: {type(nombre1)}')

nombre2= 5.2
print(f'La variable nombre2 es de tipo: {type(nombre2)}')

mensaje= """Ejemplo de salto
de línea
clase 4"""
print(mensaje)

# el condicional "if (sí)" permite evaluar dos o más condiciones para ver sí se cumplen o no
# condicional "else (y sí no)": y sí no es cierta la condición

number1= 5
number2= 7

if number1 > number2:
  print('El número 1 es mayor')

else:
  print('El número 2 es mayor')
