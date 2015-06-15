import math

class Punto:
    'Representa un punto en coordenadas geométricas bidimensionales'

    def __init__(self, x=0, y=0):
        '''Inicializa la posición de un nuevo punto. Las coordenadas x e y pueden ser especificadas. Si no lo son, 
        el punto por defecto será el de origen.'''
        self.mover(x, y)

    def mover(self, x, y):
        "Mueve el punto a una nueva localización en un espacio bidimensional."
        self.x = x
        self.y = y
    def reiniciar(self):
        'Reinicia el punto al origen geométrico: 0, 0'
        self.mover(0, 0)

    def calcular_distancia(self, otro_punto):
        """Calcula la distancia desde este punto a un segundo punto pasado como un parámetro. Esta función usa
        el Teorema de Pitágoras para calcular la distancia entre puntos. La distancia es devuelta como un float."""

        return math.sqrt(
                (self.x - otro_punto.x)**2 +
                (self.y - otro_punto.y)**2)
