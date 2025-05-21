from .jogador import Jogador

class Time:
    def __init__(self, nome: str, estadio_sede):
        self.nome = nome
        self.estadio_sede = estadio_sede
        self.jogadores = []

    def adicionar_jogador(self, jogador: Jogador):
        if jogador in self.jogadores:
            raise ValueError("Jogador já está no time.")
        self.jogadores.append(jogador)

    def remover_jogador(self, jogador: Jogador):
        self.jogadores.remove(jogador)

    def altura_media(self) -> float:
        if not self.jogadores:
            return 0.0
        return sum(j.altura for j in self.jogadores) / len(self.jogadores)
