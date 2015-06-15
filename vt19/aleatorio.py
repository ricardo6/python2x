import random
algunas_excepciones = [ValueError, TypeError, IndexError, None]

try:
    choice = random.choice(algunas_excepciones)
    print("lanzando {}".format(choice))
    if choice:
        raise choice("Un error")
except ValueError:
    print("Cazado un ValueError")
except TypeError:
    print("Cazado un TypeError")
except Exception as e:
    print("Cazado algún otro error: %s" %
        ( e.__class__.__name__))
else:
    print("Este código es llamado si no hay ninguna excepción")
finally:
    print("Este código es siempre llamado")
