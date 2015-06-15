class ArchivoWebM:
    def __init__(self, nombrearchivo):
        if not nombrearchivo.endswith(".webm"):
            raise Exception("formato de archivo inválido")

        self.nombrearchivo = nombrearchivo

    def play(self):
        print("ejecutándose {} como archivo webm".format(self.nombrearchivo))
