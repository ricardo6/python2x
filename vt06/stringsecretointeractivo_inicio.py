Python 3.3.3 (v3.3.3:c3896275c0f6, Nov 18 2013, 21:18:40) [MSC v.1600 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> class StringSecreto:
... 	'''Un modo no totalmente seguro de almacenar un string secreto.'''
... 	def __init__(self, string_plano, frase_pass):
... 		self.__string_plano = string_plano
... 		self.__frase_pass = frase_pass
... 	def decrypt(self, frase_pass):
... 		'''Sólo muestra el string si la frase_pass es correcta.'''
... 		if frase_pass == self.__frase_pass:
... 			return self.__string_plano
... 		else:
... 			return ''
... 
>>> 