def no_devolver():
    print("Estoy a punto de lanzar una excepción")
    raise Exception("Esto siempre será lanzado")
    print("Esta línea nunca se ejecutará")
    return "Esto no será devuelto."

def llamar_excepcion():
    print("llamar_excepcion empieza aquí...")
    no_devolver()
    print("una exceción ha sido lanzada...")
    print("...por tanto esta línea no se ejecuta")