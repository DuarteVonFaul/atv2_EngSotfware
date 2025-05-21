from . import *
from datetime import date
import pytest


def test_time_duplicado_no_campeonato():
    campeonato = Campeonato(1, "Brasileirão", 2024)
    estadio = Estadio("Estádio A", "Endereço A")
    time = Time("Time A", estadio)
    campeonato.adicionar_time(time)
    with pytest.raises(ValueError):
        campeonato.adicionar_time(time)


def test_filtrar_partidas_por_data():
    campeonato = Campeonato(2, "Copa", 2024)
    estadio = Estadio("Estádio B", "Rua B")
    time1 = Time("Time 1", estadio)
    time2 = Time("Time 2", estadio)
    partida = Partida(time1, time2, estadio, date(2024, 10, 10))
    campeonato.adicionar_partidas(partida)
    partidas = campeonato.listar_partidas_por_dia(date(2024, 10, 10))
    assert partida in partidas