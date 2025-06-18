import pytest
from unittest.mock import Mock
from ..src.services.JogadorService import JogadorService
from . import Jogador,Estatisticas
from datetime import date



def test_nao_salvar_jogador_sem_nome_mock():
    mock_service = Mock(spec=JogadorService)
    mock_service.criar.side_effect = ValueError("O nome do jogador não pode estar vazio.")

    jogador = Jogador(nome="", data_nascimento=date(1999, 4, 27),altura=1.80,)

    with pytest.raises(ValueError):
        mock_service.criar(jogador)



def test_atualizar_estatisticas_com_mock(session):
 
    mock_estatisticas_service = Mock()
    mock_repository = Mock()
    service = JogadorService(session)
    
    jogador = service.criar(Jogador(nome="Guilherme", data_nascimento=date(1999, 4, 27),altura=1.68))
    estatisticas_falsas = Estatisticas(gols=10, assistencias=5)
    
    mock_estatisticas_service.get_estatisticas.return_value = estatisticas_falsas

    assert jogador.estatisticas == None
    
    service.atualizar_estatisticas(jogador.id, mock_estatisticas_service.get_estatisticas())


    assert estatisticas_falsas == service.buscar_por_id(jogador.id).estatisticas