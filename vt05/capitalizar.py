def formato_string(string,formatter=None):
	''' Formatea un string usando el objeto formatter, del que se espera que tenga un método format()
	que acepta un string.'''
	class DefaultFormatter:
		'Formatea un string en case title'
		def format(self, string):
			return str(string).title()
	if not formatter:
		formatter = DefaultFormatter()
	return formatter.format(string)
