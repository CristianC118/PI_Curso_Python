
"""
    Bucle for
- Tipo Range
- Notaciones especiales con print
"""

for i in range(5):

  i += 1
  print(f'Valor de la variable i: {i}')

print('*****************')

# Comienza desde el 5 y va hasta el 49 de 3 en 3
for i in range(5, 50, 3):

  print(i, end=' ')


print('\n')


valido= False

email= input('Introduce tu email')

for i in range(len(email)):

  if email[i]== '@':
    valido= True

if valido== True:
  print('Email Correcto')

else:
  print('Email Incorrecto')