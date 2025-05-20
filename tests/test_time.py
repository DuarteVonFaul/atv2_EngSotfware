import pytest
from src.models.jogador import Jogador
from src.models.time import Time
from src.models.estadio import Estadio
from datetime import date

def test_altura_media():
    estadio = Estadio("Arena", "Rua A")
    time = Time("Time A", estadio)
    time.adicionar_jogador(Jogador("A", date(2000, 1, 1), 1.75))
    time.adicionar_jogador(Jogador("B", date(1998, 1, 1), 1.85))
    assert round(time.altura_media(), 2) == 1.80

def test_adicionar_jogador_duplicado():
    estadio = Estadio("Arena", "Rua A")
    time = Time("Time B", estadio)
    jogador = Jogador("C", date(1997, 1, 1), 1.78)
    time.adicionar_jogador(jogador)
    with pytest.raises(ValueError):
        time.adicionar_jogador(jogador)

def test_remover_jogador():
    estadio = Estadio("Arena", "Rua A")
    time = Time("Time C", estadio)
    jogador = Jogador("D", date(1999, 1, 1), 1.80)
    time.adicionar_jogador(jogador)
    time.remover_jogador(jogador)
    assert jogador not in time.jogadores

def test_jogador_em_dois_times():
    estadio1 = Estadio("Estádio 1", "Rua 1")
    estadio2 = Estadio("Estádio 2", "Rua 2")
    jogador = Jogador("Duplicado", date(1999, 5, 5), 1.82)

    time1 = Time("Time 1", estadio1)
    time2 = Time("Time 2", estadio2)

    time1.adicionar_jogador(jogador)
    with pytest.raises(ValueError):
        time2.adicionar_jogador(jogador)
