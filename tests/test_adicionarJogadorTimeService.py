from . import *
import pytest
from datetime import date
from ..src.services.AdicionarJogadorTimeService import AdicionarJogadorTimeService


def test_adicionar_jogador_com_sucesso():
    campeonato = Campeonato(1, "Campeonato Teste", 2024)
    estadio = Estadio("Estádio A", "Rua A")
    time = Time("Time A", estadio)
    jogador = Jogador("João", date(2000, 1, 1), 1.80)

    campeonato.adicionar_time(time)
    
    AdicionarJogadorTimeService.adicionar_jogador(campeonato, time, jogador)

    assert jogador in time.jogadores

def test_jogador_ja_em_outro_time_do_campeonato():
    campeonato = Campeonato(2, "Campeonato Teste", 2024)
    estadio1 = Estadio("Estádio 1", "Endereço 1")
    estadio2 = Estadio("Estádio 2", "Endereço 2")
    
    time1 = Time("Time 1", estadio1)
    time2 = Time("Time 2", estadio2)
    
    jogador = Jogador("Carlos", date(1999, 5, 5), 1.82)

    campeonato.adicionar_time(time1)
    campeonato.adicionar_time(time2)

    AdicionarJogadorTimeService.adicionar_jogador(campeonato, time1, jogador)

    with pytest.raises(ValueError, match="Jogador já pertence a outro time do campeonato."):
        AdicionarJogadorTimeService.adicionar_jogador(campeonato, time2, jogador)

def test_jogador_ja_no_mesmo_time():
    campeonato = Campeonato(3, "Campeonato Teste", 2024)
    estadio = Estadio("Estádio Repetido", "Rua Repetida")
    time = Time("Time Único", estadio)
    jogador = Jogador("Repetido", date(2001, 3, 15), 1.78)

    campeonato.adicionar_time(time)
    AdicionarJogadorTimeService.adicionar_jogador(campeonato, time, jogador)

    with pytest.raises(ValueError, match="Jogador já está no time."):
        AdicionarJogadorTimeService.adicionar_jogador(campeonato, time, jogador)