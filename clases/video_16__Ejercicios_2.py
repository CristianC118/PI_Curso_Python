
"""Ejercicio 1:
• Crea un programa que muestre los números impares del 1 al 100. Los números deberán
aparecer una al lado del otro sin salto de línea."""


for i in range(1, 100, 2):

  print(i, end=' ')

"""Ejercicio 2:
• Crea  un  programa  que  pida  por  teclado  introducir  una  contraseña.  La  contraseña  no
podrá tener menos de 8 caracteres ni espacios en blanco. Si la contraseña es correcta,
el programa imprime “Contraseña OK”. En caso contrario imprime “Contraseña
errónea”."""


contador= 0
passs= input('\nIntroduce tu contraseña: ')

for i in range(len(passs)):

  if passs[i]== ' ':
    contador += 1


if len(passs) >= 8 or contador < 0:
  print('\nContraseña OK')

else:
  print('\nContraseña Errónea')

"""Ejercicio 3:
• Crea un programa que  evalúe si una dirección de correo electrónico es válida o no en
función  de  si  tiene  “@”  o  “.”  Hay  que  tener  en  cuenta  que  la  dirección  se  considera
correcta si solo tiene una “@” y si tiene uno o más “.” """


arroba= 0
punto= 0

correo= input('Introduce tu correo: ')

for i in range(len(correo)):

  if correo[i] == '@':
    arroba += 1

  if correo[i] == '.':
    punto = 1

if punto == 0 or arroba != 1:
  print('Email Incorrecto')

else:
  print('Email Correcto')