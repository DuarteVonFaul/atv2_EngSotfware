class TabelaTime:
    def __init__(self, time):
        self.time = time
        self.pontos = 0
        self.vitorias = 0
        self.empates = 0
        self.derrotas = 0
        self.gols_pro = 0
        self.gols_contra = 0

    @property
    def saldo_gols(self):
        return self.gols_pro - self.gols_contra