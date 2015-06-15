class Inmueble:
    def __init__(self, metros_cuadrados='', habitaciones='', bans='', **kwargs):
        super().__init__(**kwargs)
        self.metros_cuadrados = metros_cuadrados
        self.num_habitaciones = habitaciones
        self.num_bans = bans

    def mostrar(self):
        print("DETALLES Inmueble")
        print("================")
        print("metros cuadrados: {}".format(self.metros_cuadrados))
        print("habitaciones: {}".format(self.num_habitaciones))
        print("baños: {}".format(self.num_bans))
        print()

    def prompt_init():
        return dict(metros_cuadrados=input("Escribe los metros cuadrados: "),
                habitaciones=input("Escribe el número de habitaciones: "),
                bans=input("Escribe el número de baños: "))
    prompt_init = staticmethod(prompt_init)

