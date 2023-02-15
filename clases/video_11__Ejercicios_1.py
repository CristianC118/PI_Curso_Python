'''
Ejercicio 1: 
• Crea un programa que pida dos números por teclado. El programa tendrá una función 
llamada “DevuelveMax” encargada de devolver el número más alto de los dos 
introducidos.'''


def DevuelveMax():

  numero1= int(input('Introduce cualquier número: '))
  numero2= int(input('Introduce cualquier número de vuelta: '))

  if numero1 > numero2:
    print('El Número 1 es mayor')

  else:
    print('El Número 2 es mayor')

DevuelveMax()

print(' ')


'''
Ejercicio 2:
• Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”. Esos tres datos 
deberán ser almacenados en una lista y mostrar en consola el mensaje: “Los datos
personales son: nombre apellido teléfono” (Se mostrarán los datos introducidos por
teclado).'''


nombre= input('Introduce tu nombre completo: ')
direccion= input('Introduce tu direccion: ')
tfno= int(input('Introduce tu número celular: '))

datos= [nombre, direccion, tfno]

print(f'Los Datos personales son: {datos}')

print(' ')

'''
Ejercicio 3:
• Crea un programa que pida tres números por teclado. El programa imprime en consola 
la media aritmética de los números introducidos.'''


num1= int(input('Introduce cualquier número: '))
num2= int(input('Introduce cualquier número: '))
num3= int(input('Introduce cualquier número: '))

numeros= (num1 + num2 + num3) / 3

print(f'La media aritmética de los números es: {numeros}')
