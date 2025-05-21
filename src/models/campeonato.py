from .time import Time
from .partida import Partida

class Campeonato:
    def __init__(self, id:int,nome: str, ano:int):
        self.nome = nome
        self.ano = ano
        self.id = id
        self.times = []
        self.partidas = []

    def adicionar_time(self, time: Time):
        if time in self.times:
            raise ValueError("Time já está no campeonato.")
        self.times.append(time)

    def adicionar_partidas(self, partida: Partida):
        if partida in self.partidas:
            raise ValueError("Partidad já registrada")
        self.partidas.append(partida)

    def listar_partidas_por_dia(self, data):
        return [p for p in self.partidas if p.data == data]

