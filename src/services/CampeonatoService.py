from ..repositories.campeonatoRepository   import CampeonatoRepository, Campeonato
from ..repositories.partidaRepository       import PartidaRepository, Partida
from datetime import date, timedelta

class CampeonatoService:
    def __init__(self, session):
        self.campeonato_repo = CampeonatoRepository(session)
        self.partida_repo = PartidaRepository(session)
        self.session = session

    def criar(self, campeonato:Campeonato) -> Campeonato:
        return self.campeonato_repo.adicionar(campeonato)

    def gerar_partidas(self, campeonato_id: int, data_inicial: date = None):
        campeonato = self.campeonato_repo.buscar_por_id(campeonato_id)
        if not campeonato:
            raise ValueError("Campeonato não encontrado.")

        times = campeonato.times
        if not data_inicial:
            data_inicial = date.today()

        dias_entre_partidas = 1
        data_partida = data_inicial

        for i in range(len(times)):
            for j in range(i + 1, len(times)):
                mandante = times[i]
                visitante = times[j]
                estadio = mandante.estadio_sede or visitante.estadio_sede
                partida = Partida(
                    mandante=mandante,
                    visitante=visitante,
                    estadio=estadio,
                    data=data_partida
                )
                campeonato.partidas.append(partida)
                data_partida += timedelta(days=dias_entre_partidas)

        self.campeonato_repo.atualizar()
        self.session.refresh(campeonato)
        return campeonato.partidas

    def buscar(self, campeonato_id:int) -> Campeonato:
        return self.campeonato_repo.buscar_por_id(campeonato_id)