
from ..src.services.TimeService import TimeService
from ..src.services.CampeonatoService import CampeonatoService
from ..src.services.AdicionarTimeCampeonatoService import AdicionarTimeCampeonatoService
from ..src.services.AdicionarResultadoPartidaService import AdicionarResultadoPartidaService
from ..src.services.GerarTabelaClassificacaoService import GerarTabelaClassificacaoService

from . import Time, Campeonato, Estadio
from datetime import date
import random


def test_tabela_classificacao_result(session):
    time_service = TimeService(session)
    campeonato_service = CampeonatoService(session)
    add_time_campeonato_service = AdicionarTimeCampeonatoService(session)
    adicionar_resultado_partida_service = AdicionarResultadoPartidaService(session)
    gerar_tabela_service = GerarTabelaClassificacaoService(session)

    time1 = time_service.criar(Time('Flamengo', Estadio('Maracana', 'Rio de Janeiro')))
    time2 = time_service.criar(Time('Vasco', Estadio('Sao Januario', 'Rio de Janeiro')))
    time3 = time_service.criar(Time('BotaFogo', Estadio('Nilton Santos', 'Rio de Janeiro')))

    brasileirao = campeonato_service.criar(Campeonato('Brasileirao', '2025'))

    add_time_campeonato_service.adicionar_time(brasileirao.id, time1)
    add_time_campeonato_service.adicionar_time(brasileirao.id, time2)
    add_time_campeonato_service.adicionar_time(brasileirao.id, time3)

    partidas = campeonato_service.gerar_partidas(brasileirao.id, date(2025, 1, 1))

    for partida in partidas:
        gols_m = random.randint(0, 3)
        gols_v = random.randint(0, 3)
        adicionar_resultado_partida_service.adicionar_resultado_partida(partida.id, gols_m, gols_v)

    tabela = gerar_tabela_service.GerarTabela(brasileirao.id)

    assert len(tabela) == 3

    for i in range(len(tabela) - 1):
        t1 = tabela[i]
        t2 = tabela[i + 1]
        assert (
            (t1.pontos, t1.vitorias, t1.saldo_gols, t1.gols_pro)
            >=
            (t2.pontos, t2.vitorias, t2.saldo_gols, t2.gols_pro)
        )
