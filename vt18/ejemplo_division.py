def ejemplo_division(numero):
    try:
        return 100 / numero
    except ZeroDivisionError:
        return "¡Es imposible dividir por cero!"

#print(ejemplo_division(0))
#print(ejemplo_division(50.0))
#print(ejemplo_division("hola"))
