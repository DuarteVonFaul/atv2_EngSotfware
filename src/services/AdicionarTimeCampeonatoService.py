from ..repositories.campeonatoRepository import CampeonatoRepository, Campeonato
from ..models.time                       import Time


class AdicionarTimeCampeonatoService:
    def __init__(self, session):
        self.repo = CampeonatoRepository(session)

    def adicionar_time(self, campeonato_id: int, time: Time):
        campeonato = self.repo.buscar_por_id(campeonato_id)
        if not campeonato:
            raise ValueError("Campeonato não encontrado.")
        if time in campeonato.times:
            raise ValueError("Time já está inscrito no Campeonato")
        campeonato.times.append(time)
        self.repo.atualizar()
