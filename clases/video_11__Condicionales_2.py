"""
    Condicional 'else' (y sí no) y condicional elif (else-if)

. No se pueden tener más de un 'else' sin su correspondiente 'if'
. En el caso de haber más de un 'if' el 'else' se acompaña del 'if' más cercano
"""

print('Verificación de Acceso')

edad_Usuario= int(input('Introduce tu edad: '))

if edad_Usuario < 18:
  print('No puedes pasar.')

elif edad_Usuario > 100:
  print('Edad Incorrecta')

else:
  print('Puedes pasar.')


print('--------------------------------')

nota_alumno= int(input('Introduce la nota: '))

if -1 < nota_alumno <= 5:
  print('Reprobado')

elif nota_alumno == 6:
  print('Suficiente')

elif nota_alumno == 7:
  print('Buen trabajo')

elif nota_alumno == 8:
  print('Notable')

elif nota_alumno == 9:
  print('Bien Hecho')

elif nota_alumno == 10:
  print('Excelente')

else:
  print('Error de Nota')


"""
  Nota: Link directo a la documentaciónde 'else' y 'elif' de Python (En Español)
(https://docs.python.org/es/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)
"""
