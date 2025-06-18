from ..repositories.timeRepository import TimeRepository
from ..repositories.jogadorRepository import JogadorRepository

class AdicionarJogadorTimeService:
    def __init__(self, session):
        self.time_repo = TimeRepository(session)
        self.jogador_repo = JogadorRepository(session)

    def adicionar_jogador(self, time_id: int, jogador_id: int):
        time = self.time_repo.buscar_por_id(time_id)
        jogador= self.jogador_repo.buscar_por_id(jogador_id)

        if not time or not jogador:
            raise ValueError("Time ou jogador não encontrado.")

        if jogador in time.jogadores:
            raise ValueError("Jogador já está no time.")
        
        if jogador.time:
            raise ValueError("Jogador já está em um time.")

        time.jogadores.append(jogador)
        self.time_repo.atualizar()
