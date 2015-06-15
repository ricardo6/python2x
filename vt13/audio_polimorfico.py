class ArchivoAudio:
    def __init__(self, nombrearchivo):
        if not nombrearchivo.endswith(self.ext):
            raise Exception("formato archivo inválido")

        self.nombrearchivo = nombrearchivo

class ArchivoMP3(ArchivoAudio):
    ext = "mp3"
    def play(self):
        print("ejecutándose {} como mp3".format(self.nombrearchivo))

class ArchivoWav(ArchivoAudio):
    ext = "wav"
    def play(self):
        print("ejecutándose {} como wav".format(self.nombrearchivo))

class ArchivoOgg(ArchivoAudio):
    ext = "ogg"
    def play(self):
        print("ejecutándose {} como ogg".format(self.nombrearchivo))
