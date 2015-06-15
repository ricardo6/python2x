Python 3.3.3 (v3.3.3:c3896275c0f6, Nov 18 2013, 21:18:40) [MSC v.1600 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> import math
>>> class Punto:
... 	def mover(self, x, y):
... 		self.x = x
... 		self.y = y
... 	def reiniciar(self):
... 		self.mover(0, 0)
... 	def calcular_distancia(self, otro_punto):
... 		return math.sqrt(
... 			 (self.x - otro_punto.x)**2 +
... 			 (self.y - otro_punto.y)**2)
... 
>>> punto1 = Punto()
>>> punto2 = Punto()
>>> punto1.reiniciar()
>>> punto2.mover(5,0)
>>> print(punto2.calcular_distancia(punto1))
5.0
>>> 