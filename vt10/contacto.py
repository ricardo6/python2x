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

class Vendedor(Contacto):
    def pedido(self, pedido):
        print("En una aplicación completa enviaría el pedido "
                "{} pedido a {}".format(pedido, self.nombre))


