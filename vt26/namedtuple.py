from collections import namedtuple
alumno = namedtuple ("Alumno", "nombre edad curso nota")
alumno = alumno("Alberto", 18, curso="Segundo", nota="Notable")

#credencial = ('pablo', 'identificador')

Credencial = namedtuple('Credencial', 'nombreusuario,contraseña')
credencial = Credencial(nombreusuario='pablo', contraseña='identificador')





