from ..repositories.campeonatoRepository   import CampeonatoRepository, Campeonato
from ..repositories.partidaRepository       import PartidaRepository, Partida
from datetime import date, timedelta

class BuscarPartidaCampeonatoService:
    def __init__(self, session):
        self.campeonato_repo = CampeonatoRepository(session)
        self.partida_repo = PartidaRepository(session)

    def buscar_por_data(self, partida_data:date, campeonato_id:int) -> list[Partida]:
        return self.partida_repo.buscar_por_data(partida_data,campeonato_id)
    
    def buscar_por_estadio(self, estadio_id:int, campeonato_id:int) -> list[Partida]:
        return self.partida_repo.buscar_por_estadio(estadio_id,campeonato_id)