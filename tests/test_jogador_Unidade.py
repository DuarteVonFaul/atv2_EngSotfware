from ..src.services.JogadorService import JogadorService
from . import Jogador
from datetime import date

from pprint import pprint


def test_jogador_database_insert(session):

    service = JogadorService(session)

    jogador = service.criar(Jogador('Guilherme',date(1999, 4, 27),1.69))


    
    assert jogador == service.buscar_por_id(1)

    ...

def test_jogador_database_search_by_name(session):

    service = JogadorService(session)

    jogador_criado = service.criar(Jogador('Guilherme',date(1999, 4, 27),1.69))
    jogador_busca = service.buscar('Guilherme')


    assert jogador_criado == jogador_busca

    ...


def test_jogador_database_update(session):

    service = JogadorService(session)

    service.criar(Jogador('Guilherme',date(1999, 4, 27),1.69))
    jogador = service.buscar_por_id(1)
    assert jogador.nome == 'Guilherme'

    jogador.nome = 'Matheus'
    service.atualizar(jogador)

    assert jogador.nome == 'Matheus'