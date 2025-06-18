from ..src.services.TimeService import TimeService
from . import Jogador, Time, Estadio
from datetime import date

from datetime import date
import pytest


def test_time_database_insert(session):

    service = TimeService(session)

    flamengo = Time('Flamengo', Estadio('Maracana', 'Rio de Janeiro'))

    flamengo.adicionar_jogador(Jogador('Jorginho',date(1999, 4, 27),1.69 ))
    flamengo.adicionar_jogador(Jogador('Arrascaeta',date(1999, 4, 27),1.69 ))
    flamengo.adicionar_jogador(Jogador('Predo',date(1999, 4, 27),1.69 ))
    flamengo.adicionar_jogador(Jogador('Gerson',date(1999, 4, 27),1.69 ))
    flamengo.adicionar_jogador(Jogador('Plata',date(1999, 4, 27),1.69 ))
    

    flamengo = service.criar(flamengo)


    
    assert flamengo == service.buscar(1)

    ...

def test_time_database_insert_same_name(session):

    service = TimeService(session)

    service.criar(Time('Flamengo', Estadio('Maracana', 'Rio de Janeiro')))



    with pytest.raises(ValueError, match="Já existe um time com o nome 'Flamengo' ou com o mesmo estádio"):
        service.criar(Time('Flamengo', Estadio('Maracana', 'Rio de Janeiro')))
    ...