def sin_retorno():
    print("Estoy a punto de lanzar una excepción")
    raise Exception("Esto será lanzado siempre")
    print("Esta línea nunca será ejecutada")
    return "No tiene retorno"

try:
    sin_retorno()
except:
    print("He cazado una excepción")
print("Ejecutado después de la excepción")








