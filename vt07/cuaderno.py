import datetime

# Almacena todas las ids disponibles para las nuevas notas
ultima_id = 0

class Nota:
    '''Representa una nota en el cuaderno. Se compara con un String
    en las búsquedas y las etiquetas para cada nota'''
    def __init__(self, memo, tags=''):
        '''inicializa una nota con memo y opcional tags
        separado por comas. Automáticamente configura la fecha
        de creación de la nota y una única id'''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global ultima_id
        ultima_id += 1
        self.id = ultima_id
    def match(self, filter):
        '''Determina si esta nota concuerda con el filtro
        de texto. Devuelve True si concuerda, en otro caso False.
        Búsqueda es case sensitive y compara tanto con text como
        con tags.'''
        return filter in self.memo or filter in self.tags

    