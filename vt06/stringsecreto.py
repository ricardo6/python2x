class StringSecreto:
	'''Un modo no totalmente seguro de almacenar un string secreto.'''
	
	def __init__(self, string_plano, frase_pass):
		self.__string_plano = string_plano
		self.__frase_pass = frase_pass

	def decrypt(self, frase_pass):
		'''Sólo muestra el string si la frase_pass es correcta.'''
		if frase_pass == self.__frase_pass:
			return self.__string_plano 
		else:
			return ''



