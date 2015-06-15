Python 3.3.3 (v3.3.3:c3896275c0f6, Nov 18 2013, 21:18:40) [MSC v.1600 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> class Punto:
... 	def reiniciar():
... 		pass
... 
>>> p = Punto()
>>> p.reiniciar()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
TypeError: reiniciar() takes 0 positional arguments but 1 was given
>>> 