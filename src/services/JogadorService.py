from ..repositories.jogadorRepository import JogadorRepository, Jogador
from ..models.Estatisticas import Estatisticas


class JogadorService:
    def __init__(self, session):
        self.repo = JogadorRepository(session)

    def criar(self, jogador: Jogador) -> Jogador:
        if not jogador.nome.strip():
            raise ValueError("O nome do jogador não pode estar vazio.")
        return self.repo.adicionar(jogador)
    
    def buscar_por_id(self,jogador_id:int):
        return self.repo.buscar_por_id(jogador_id)

    def buscar(self, jogador_nome: str):
        return self.repo.buscar_por_nome(jogador_nome)
    
    def atualizar_estatisticas(self,jogador_id:int, estatisticas:Estatisticas):
        jogador = self.buscar_por_id(jogador_id)
        jogador.estatisticas = estatisticas
        self.repo.atualizar()
    
    def atualizar(self, novo_jogador: Jogador):
        jogador = self.buscar_por_id(novo_jogador.id)
        jogador.nome = novo_jogador.nome
        jogador.altura = novo_jogador.altura
        jogador.data_nascimento = novo_jogador.data_nascimento
        self.repo.atualizar()