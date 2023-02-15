
"""
    Paquetes Distribuidos

Para crear Paquetes Distribuidos debemos crear un archivo setup.py en la carpeta raíz y luego hacer lo siguiente...

from setuptools import setup

setup(
  name= 'paquetecalculos',
  version= '1.0',
  description= 'Paquete de Redondeo y Potencia',
  author= 'Cristian',
  packages= ['video_35__Paquetes', 'video_35__Paquetes.redondeo_potencia']
  )

Luego en la powershell llamamos a (python setup.py sdist) para crear el paquete distribuido
"""