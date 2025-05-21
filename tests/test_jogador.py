from . import *
import pytest
from datetime import date, timedelta

def test_calcular_idade():
    jogador = Jogador("João", date(2000, 5, 10), 1.80)
    assert jogador.calcular_idade() == date.today().year - 2000 - (
        (date.today().month, date.today().day) < (5, 10)
    )

def test_altura_negativa_gera_erro():
    with pytest.raises(ValueError):
        Jogador("Pedro", date(1995, 1, 1), -1.70)

def test_data_nascimento_invalida():
    with pytest.raises(ValueError):
        futuro = date.today() + timedelta(days=1)
        Jogador("Futuro", futuro, 1.75)

def test_adicionar_remover_jogador():
    estadio = Estadio("Estádio X", "Rua X")
    time = Time("Time X", estadio)
    jogador = Jogador("João", date(2000, 1, 1), 1.80)
    time.adicionar_jogador(jogador)
    assert jogador in time.jogadores
    time.remover_jogador(jogador)
    assert jogador not in time.jogadores


