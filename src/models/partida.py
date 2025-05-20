from datetime import date
from src.models.time import Time
from src.models.estadio import Estadio
from src.models.resultado import Resultado

class Partida:
    def __init__(self, mandante: Time, visitante: Time, estadio: Estadio, data: date):
        if not mandante or not visitante or not estadio or not data:
            raise ValueError("Dados inválidos para criar partida.")
        if estadio != mandante.estadio_sede and estadio != visitante.estadio_sede:
            raise ValueError("Estádio não corresponde ao estádio-sede de nenhum dos times.")
        self.mandante = mandante
        self.visitante = visitante
        self.estadio = estadio
        self.data = data
        self.resultado = None

    def definir_resultado(self, gols_mandante: int, gols_visitante: int):
        if gols_mandante < 0 or gols_visitante < 0:
            raise ValueError("Gols não podem ser negativos.")
        self.resultado = Resultado(gols_mandante, gols_visitante)