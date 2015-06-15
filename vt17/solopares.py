class SoloPares(list):
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError("Sólo pueden añadirse enteros")
        if integer % 2:
            raise ValueError("Sólo pueden añadirse números pares")
        super().append(integer)

