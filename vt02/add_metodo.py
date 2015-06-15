Python 3.3.3 (v3.3.3:c3896275c0f6, Nov 18 2013, 21:18:40) [MSC v.1600 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> class Punto:
... 	def reiniciar(self):
... 		self.x = 0
... 		self.y = 0
... 
>>> p = Punto()
>>> p.reiniciar()
>>> print(p.x, p.y)
0 0
>>> Punto.reiniciar(p)
>>> print(p.x, p.y)
0 0
>>> 