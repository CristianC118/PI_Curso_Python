
"""
    Documentación
    Incluir comentarios en clases, métodos, módulos, etc.
    Sirve para ayudar en el trabajo en equipo. Especialmente útil en aplicaciones complejas.
"""
class Areas:

    """Esta clase calcula las áreas de diferentes figuras geométricas."""

    def areaCuadrado(lado):

        """Calcula el Área de un cuadrado

        Elevando al cuadrado el lado pasado por parámetro
        """
        return (f'El área del cuadrado es: {lado*lado}')

    def areaTriangulo(base, altura):

        """Calcula el área de un triángulo utilizando los parámetros base y altura."""

        return (f'El área del triángulo es: {(base*altura)/2}')


help(Areas.areaCuadrado)

help(Areas)