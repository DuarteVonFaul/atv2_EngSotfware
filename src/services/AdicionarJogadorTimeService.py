from ..models.campeonato import Campeonato
from ..models.time import Time
from ..models.jogador import Jogador

class AdicionarJogadorTimeService:
    @staticmethod
    def adicionar_jogador(campeonato: Campeonato, time: Time, jogador: Jogador):
        for outro_time in campeonato.times:
            if jogador in outro_time.jogadores and outro_time != time:
                raise ValueError("Jogador já pertence a outro time do campeonato.")
        time.adicionar_jogador(jogador)