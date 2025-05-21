from . import *
import pytest
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
