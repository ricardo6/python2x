Python 3.3.3 (v3.3.3:c3896275c0f6, Nov 18 2013, 21:18:40) [MSC v.1600 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> def formato_string(string,formatter=None):
	''' Formatea un string usando el objeto formatter, del que se espera que tenga un método format()
	que acepta un string.'''
	class DefaultFormatter:
		'Formatea un string en case title'
		def format(self, string):
			return str(string).title()
	if not formatter:
		formatter = DefaultFormatter()
	return formatter.format(string)
... ... ... ... ... ... ... ... ... ... 
>>> string_hola ="hola mundo, ¿Cómo estás hoy?"
>>> print(" entrada:" + string_hola)
 input:hola mundo, ¿Cómo estás hoy?
>>> print("output: " + formato_string(string_hola))
output: Hola Mundo, ¿Cómo Estás Hoy?
>>> 