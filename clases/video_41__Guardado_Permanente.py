
"""
    Guardado Permanente

- Guardar datos de forma permanente en ficheros externos
"""

# N° 0.1
import pickle

# N° 0.2
class Persona():

  def __init__(self, nombre, genero, edad):

    self.nombre= nombre
    self.genero= genero
    self.edad= edad

    print(f'Se ha creado una persona nueva con el nombre de {self.nombre}.')

  # N° 0.3
  def __str__(self): # Método str: convierte en cadena de texto la info de un objeto para poder ver la info de las personas a guardar

    return '{} {} {}'.format(self.nombre, self.genero, self.edad)


# N° 0.5
# Guardar info para grabar y leer
class ListaPersonas():

  personas= []

  # N° 1
  # Guardar Lista en un Fichero Externo
  def __init__(self):

    listaDePersonas= open('video_41__ficheroExterno', 'ab+') # Agrega info binaria

    # N° 2
    # Mandar cursor al comienzo
    listaDePersonas.seek(0)

    try: # Agregamos exepciones para que no de error sí no se agrega nada
      # N° 3
      # Volcado de info para leerla
      self.personas= pickle.load(listaDePersonas)
      print('Se cargaron {} personas del fichero externo'.format(len(self.personas)))

    except:
      print('El fichero está vacio')

    finally:
      listaDePersonas.close()
      del (listaDePersonas)

  # Agregar Personas a la Lista
  def agregarPersonas(self, p):

    self.personas.append(p)

    # N° 5
    self.guardarPersonasEnFicheroExterno()

  # Muestra la info guardada en la Lista
  def mostrarPersona(self):

    for p in self.personas:
      print(p)

  # N° 4
  def guardarPersonasEnFicheroExterno(self):

    ListaPersonas= open('video_41__ficheroExterno', 'wb') # Modo Excritura binaria
    pickle.dump(self.personas, ListaPersonas)
    listaDePersonas.close()
    del(listaDePersonas)

  # N° 4
  def guardarPersonasEnFicheroExterno(self):

    listaDePersonas= open('video_41__ficheroExterno', 'wb') # Modo Excritura binaria
    pickle.dump(self.personas, listaDePersonas)
    listaDePersonas.close()
    del (listaDePersonas)

  # N° 8
  def mostrarInfoFicheroExterno(self):

    print('La informcación del fichero externo es la siguiente: ')

    for p in self.personas:
      print(p)


# N° 0.6
# Crear objeto de tipo Lista Persona para luego poder utilizar el método agregar personas y mostrar personas
miLista= ListaPersonas()

# N° 6
persona= Persona('Rodrigo', 'Masculino', 59)

# N° 7
miLista.agregarPersonas(persona)

# N° 9
miLista.mostrarInfoFicheroExterno()


"""# N° 0.4
p= Persona('Sandra', 'Femenino', 29)
miLista.agregarPersonas(p)

p= Persona('Antonio', 'Masculino', 39)
miLista.agregarPersonas(p)

p= Persona('Ana', 'Femenino', 19)
miLista.agregarPersonas(p)

# N° 0.7
miLista.mostrarPersona()"""