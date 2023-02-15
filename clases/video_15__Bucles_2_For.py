
"""
    Bucle for:
  - Recorriendo strings
  - Tipo Range
  - Notaciones especiales con print
"""

# cuando se usan multiples valores es recomendable usar el parámetro 'sep='
print('09','12','2016', sep='-')


for i in ['Pildoras', 'Informáticas', 3]:

  # el parámetro 'end=' indíca como terminará la impresión
  print('Hola', end=' - ')


print('\n')


email= False

for i in 'juan@pildorasinformaticas.es':

  if (i== '@'):
    email= True

if email== True:
  print('Email Correcto')

else:
  print('Email Incorrecto')


print('\n')


email= False
miEmail= input('Introduce tu email: ')

for i in miEmail:

  if (i== '@'):
    email= True

if email== True:
  print('Email Correcto')

else:
  print('Email Incorrecto')


print('\n')


contador= 0
miEmail2= input('Introduce tu dirección de Email: ')

for i in miEmail2:

  if (i== '@' or i== '.'):
    contador += 1

if contador== 2:
  print('Email Correcto')

else:
  print('Email Incorrecto')


print('\n')


# Crea una seria de 5 elementos que van desde el 0 hasta el 4
for i in range(5):
  print(i)


print('\n')


for i in range(10):
  i += 1
  print(i)