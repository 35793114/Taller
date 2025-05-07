class Rectangulo(FiguraGeometrica):
    def __init__(self, alto, ancho):
        super().__init__(alto, ancho)
    def area(self):
        return self._alto *  self._ancho
    def __str__(self):
        return f'Rectangulo de alto {self._alto}, área {self.area()}'