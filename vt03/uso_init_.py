Python 3.3.3 (v3.3.3:c3896275c0f6, Nov 18 2013, 21:18:40) [MSC v.1600 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> class Punto:
... 	def __init__(self, x, y):
... 		self.mover(x, y)
... 	def mover(self, x, y):
... 			self.x = x 
... 			self.y = y
... 
>>> punto = Punto(4, 6)
>>> print(punto.x, punto.y)
4 6
>>> 