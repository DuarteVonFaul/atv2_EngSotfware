from ..src.services.BuscarPatidasCampeonatoService import BuscarPartidaCampeonatoService
from ..src.services.TimeService import TimeService
from ..src.services.CampeonatoService import CampeonatoService
from ..src.services.AdicionarTimeCampeonatoService import AdicionarTimeCampeonatoService

from . import Time, Campeonato, Estadio
from datetime import date



def test_partida_database_search_date(session):
    time_service = TimeService(session)
    campeonato_service = CampeonatoService(session)
    add_time_campeonato_service = AdicionarTimeCampeonatoService(session)
    buscar_partida_campeonato__service = BuscarPartidaCampeonatoService(session)

    time1 = time_service.criar(Time('Flamengo', Estadio('Maracana', 'Rio de Janeiro')))
    assert time1.id == 1
    time2 = time_service.criar(Time('Vasco', Estadio('Sao Januario', 'Rio de Janeiro')))
    assert time2.id == 2

    brasileirao = campeonato_service.criar(Campeonato('Brasileirao', '2025'))
    assert brasileirao.id == 1

    esperado = [
        (time1, time2, time1.estadio_sede, date(2025, 1, 1)),
    ]

    add_time_campeonato_service.adicionar_time(brasileirao.id, time1)
    add_time_campeonato_service.adicionar_time(brasileirao.id, time2)

    campeonato_service.gerar_partidas(brasileirao.id, date(2025, 1, 1))

    partidas = buscar_partida_campeonato__service.buscar_por_data(date(2025, 1, 1), brasileirao.id)

    resultado = [(p.mandante, p.visitante, p.estadio, p.data) for p in partidas]

    assert resultado == esperado



def test_partida_database_search_estadio(session):
    time_service = TimeService(session)
    campeonato_service = CampeonatoService(session)
    add_time_campeonato_service = AdicionarTimeCampeonatoService(session)
    buscar_partida_campeonato__service = BuscarPartidaCampeonatoService(session)

    time1 = time_service.criar(Time('Flamengo', Estadio('Maracana', 'Rio de Janeiro')))
    assert time1.id == 1
    time2 = time_service.criar(Time('Vasco', Estadio('Sao Januario', 'Rio de Janeiro')))
    assert time2.id == 2
    time3 = time_service.criar(Time('BotaFogo', Estadio('Nilton Santos', 'Rio de Janeiro')))
    assert time3.id == 3

    brasileirao = campeonato_service.criar(Campeonato('Brasileirao', '2025'))
    assert brasileirao.id == 1

    esperado = [
        (time1, time2, time1.estadio_sede),
        (time1, time3, time1.estadio_sede),
    ]

    add_time_campeonato_service.adicionar_time(brasileirao.id, time1)
    add_time_campeonato_service.adicionar_time(brasileirao.id, time2)
    add_time_campeonato_service.adicionar_time(brasileirao.id, time3)

    campeonato_service.gerar_partidas(brasileirao.id, date(2025, 1, 1))

    partidas = buscar_partida_campeonato__service.buscar_por_estadio(time1.estadio_id, brasileirao.id)

    resultado = [(p.mandante, p.visitante, p.estadio) for p in partidas]

    assert resultado == esperado

