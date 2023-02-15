

"""
    Métodos de Cadena

upper() convierte en mayúsculas todas las letras de un string
lower() convierte en minúscula todas las letras de un string
capitalize() coloca la primera letra en mayúscula
count() contar una y cuantas aparecen dentro de una cadena
find() representa el índice/posición donde aparece un carácter dentro de un texto
isdigit() devuelve un booleano si es un valor numérico o no
isalum() comprueba si es alfanuméricos
isalpha si es alpha comprueba si son solo letras
split()  separa por palabras utilizando espacios
strip() borra los espacios sobrante al principio y al final
replace() cambia una palabra o una letra por otra
rfind() representa el índice de un carácter contando desde atrás
"""

# convierte en mayúsculas todas las letras de un string
nombreUsuario= input('Introduce tu usuario: ')
print(f'El nombre es {nombreUsuario.upper()}')

# convierte en minúscula todas las letras de un string
nombreUsuario= input('Introduce tu usuario: ')
print(f'El nombre es {nombreUsuario.lower()}')

# coloca la primera letra en mayúscula
nombreUsuario= input('Introduce tu usuario: ')
print(f'El nombre es {nombreUsuario.capitalize()}')

# devuelve un booleano si es un valor numérico o no
edad= input('Introduce la edad: ')

while (edad.isdigit()== False):
	print('Por favor Introduce un valor númerico.')
edad= input('Introduce la edad: ')

if int(edad) < 18:
    print('No puede pasar')

else:
    print('Puede pasar')


"""
    Nota: Link a Documentación oficial de los Métodos de Cadena en Python (En Español)
(https://docs.python.org/es/3/library/stdtypes.html#text-sequence-type-str)
(https://pyspanishdoc.sourceforge.net/lib/string-methods.html)
"""
