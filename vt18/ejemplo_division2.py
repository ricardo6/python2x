def ejemplo_division2(numero):
    try:
        if numero == 25:
            raise ValueError("el número 25 no es válido")
        return 100 / numero
    except (ZeroDivisionError, TypeError):
        return "Escribe un número que no sea cero"


