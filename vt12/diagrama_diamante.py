class ClaseBase:
    num_llamadas_base = 0
    def llamame(self):
        print("LLamando método en Clase Base")
        self.num_llamadas_base += 1

class SubclaseIzq(ClaseBase):
    num_llamadas_izq = 0
    def llamame(self):
        ClaseBase.llamame(self)
        print("Llamando método en Subclase Izq")
        self.num_llamadas_izq += 1

class SubclaseDer(ClaseBase):
    num_llamadas_der = 0
    def llamame(self):
        ClaseBase.llamame(self)
        print("Llamando método en Subclase Der")
        self.num_llamadas_der += 1

class Subclase(SubclaseIzq, SubclaseDer):
    num_llamadas_sub = 0
    def llamame(self):
        SubclaseIzq.llamame(self)
        SubclaseDer.llamame(self)
        print("Llamando método en Subclase")
        self.num_llamadas_sub += 1
