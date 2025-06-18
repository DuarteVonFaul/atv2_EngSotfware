from ..repositories.partidaRepository import PartidaRepository
from ..repositories.jogadorRepository import JogadorRepository

class AdicionarResultadoPartidaService:
    def __init__(self, session):
        self.repo = PartidaRepository(session)

    def adicionar_resultado_partida(self, partida_id: int, gols_mandantes:int, gols_visitantes:int):
        partida = self.repo.buscar_por_id(partida_id)
        partida.definir_resultado(gols_mandantes,gols_visitantes)
        self.repo.atualizar()
