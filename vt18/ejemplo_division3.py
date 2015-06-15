def ejemplo_division3(numero):
    try:
        if numero == 25:
            raise ValueError("25 no es un número válido")
        return 100 / numero
    except ZeroDivisionError:
        return "Escribe un número que no sea cero"
    except TypeError:
        return "Escribe un valor numérico"
    except ValueError:
        print("El número 25 no vale")
        raise


