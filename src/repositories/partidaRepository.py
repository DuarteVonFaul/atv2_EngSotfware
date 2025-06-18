from ..models.partida import Partida

class PartidaRepository:
    def __init__(self, session):
        self.session = session

    def adicionar(self, partida: Partida):
        self.session.add(partida)
        self.session.commit()

    def listar_todos(self):
        return self.session.query(Partida).all()
    
    def buscar_por_data(self,partida_data,campeonato:int):
        return self.session.query(Partida).filter_by(data = partida_data, campeonato_id = campeonato).all()
    
    def buscar_por_estadio(self,estadio:int,campeonato:int):
        return self.session.query(Partida).filter_by(estadio_id = estadio, campeonato_id = campeonato).all()

    def buscar_por_id(self, partida_id: int) -> Partida:
        return self.session.query(Partida).get(partida_id)

    def remover(self, partida: Partida):
        self.session.delete(partida)
        self.session.commit()

    def atualizar(self):
        self.session.commit()