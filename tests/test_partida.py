from . import *
import pytest
from datetime import date


def test_criar_partida_valida():
    estadio = Estadio("Estadio Central", "Rua X")
    time1 = Time("Time A", estadio)
    time2 = Time("Time B", estadio)
    partida = Partida(time1, time2, estadio, date(2024, 10, 1))
    assert partida.mandante == time1
    assert partida.visitante == time2


def test_partida_estadio_nao_corresponde():
    estadio1 = Estadio("Estadio A", "Rua A")
    estadio2 = Estadio("Estadio B", "Rua B")
    time1 = Time("Time A", estadio1)
    time2 = Time("Time B", estadio2)
    estadio_invalido = Estadio("Estadio C", "Rua C")
    with pytest.raises(ValueError):
        Partida(time1, time2, estadio_invalido, date(2024, 10, 1))

def test_resultado_com_gols_negativos():
    estadio = Estadio("Estádio Teste", "Rua T")
    time1 = Time("T1", estadio)
    time2 = Time("T2", estadio)
    partida = Partida(time1, time2, estadio, date.today())
    with pytest.raises(ValueError):
        partida.definir_resultado(-1, 2)