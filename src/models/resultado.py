class Resultado:
    def __init__(self, numGolsMandante: int, numGolsVisitante: int):
        self.numGolsMandante = numGolsMandante
        self.numGolsVisitante = numGolsVisitante

    def getPontuacaoMandante(self) -> int:
        if self.numGolsMandante > self.numGolsVisitante:
            return 3
        elif self.numGolsMandante == self.numGolsVisitante:
            return 1
        return 0

    def getPontuacaoVisitante(self) -> int:
        if self.numGolsVisitante > self.numGolsMandante:
            return 3
        elif self.numGolsVisitante == self.numGolsMandante:
            return 1
        return 0

    def jogoSaiuEmpatado(self) -> bool:
        return self.numGolsMandante == self.numGolsVisitante