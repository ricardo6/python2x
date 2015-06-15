class ListaContactos(list):
    def buscar(self, nombre):
        '''Devuelve todos los contactos que contienen el valor de
        búsqueda en su nombre.'''
        contactos_coincidentes = []
        for contacto in self:
            if nombre in contacto.nombre:
                contactos_coincidentes.append(contacto)
        return contactos_coincidentes

class Contacto:
    todos_contactos = ListaContactos()
    
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        Contacto.todos_contactos.append(self)

class ContenedorDireccion:
    def __init__(self, calle, ciudad, provincia, codigo):
        self.calle = calle
        self.ciudad = ciudad
        self.provincia = provincia
        self.codigo = codigo

'''class Vendedor(Contacto):
	def __init__(self, nombre, email, telefono):
		super().__init__(nombre, email)
		self.telefono = telefono

	def pedido(self, pedido):
		print("En una aplicación completa enviaría el pedido "
                "{} pedido a {}".format(pedido, self.nombre))'''

class Vendedor(Contacto, ContenedorDireccion):
    def __init__(self, nombre, email, telefono, calle, ciudad, estado, codigo):
        Contacto.__init__(self, nombre, email)
        ContenedorDireccion.__init__( self, calle, ciudad, estado, codigo)
        self.telefono = telefono

        





class NombreLargoDict(dict):
	def clave_maslarga(self):
		maslarga = None
		for key in self:
			if not maslarga or len(key) > len(maslarga):
				maslarga = key
		return maslarga

class EnviarEmail:
    def enviar_mail(self,mensaje):
        print("enviando mensaje a " + self.email)
        # Añadir la lógica del email aquí

class EnvioEmailContactos(Contacto, EnviarEmail):
    pass


