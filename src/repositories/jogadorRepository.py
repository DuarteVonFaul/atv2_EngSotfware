from ..models.jogador import Jogador

class JogadorRepository:
    def __init__(self, session):
        self.session = session

    def adicionar(self, jogador: Jogador) -> Jogador:
        self.session.add(jogador)
        self.session.commit()
        self.session.refresh(jogador)
        return jogador

    def listar_todos(self) -> list[Jogador]:
        return self.session.query(Jogador).all()

    def buscar_por_id(self, jogador_id: int) -> Jogador:
        return self.session.query(Jogador).get(jogador_id)
    
    def buscar_por_nome(self, jogador_nome: str) -> Jogador:
        return self.session.query(Jogador).filter_by(nome = jogador_nome).one()

    def remover(self, jogador: Jogador):
        self.session.delete(jogador)
        self.session.commit()

    def atualizar(self):
        self.session.commit()
