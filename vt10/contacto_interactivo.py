Python 3.3.3 (v3.3.3:c3896275c0f6, Nov 18 2013, 21:18:40) [MSC v.1600 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from contacto import Contacto, Vendedor
>>> c = Contacto("Scarlett Johansson", "scarlett@suemail.com")
>>> v = Vendedor ("Bic Inc.", "bic@empresa.com")
>>> print (c.nombre, c.email, v.nombre, v.email)
Scarlett Johansson scarlett@suemail.com Bic Inc. bic@empresa.com
>>> c.todos_contactos
[<contacto.Contacto object at 0x02262B10>, <contacto.Vendedor object at 0x022ACB10>]
>>> c.pedido("Necesito 100 bic cristal")
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Contacto' object has no attribute 'pedido'
>>> v.pedido("Necesito 100 bic cristal")
En una aplicación completa enviaría el pedido Necesito 100 bic cristal pedido a Bic Inc.
>>> 