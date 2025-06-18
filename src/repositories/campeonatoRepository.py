from ..models.campeonato import Campeonato

class CampeonatoRepository:
    def __init__(self, session):
        self.session = session

    def adicionar(self, campeonato: Campeonato) -> Campeonato:
        self.session.add(campeonato)
        self.session.commit()
        self.session.refresh(campeonato)
        return campeonato

    def listar_todos(self) -> list[Campeonato]:
        return self.session.query(Campeonato).all()

    def buscar_por_id(self, campeonato_id: int) -> Campeonato:
        return self.session.query(Campeonato).get(campeonato_id)

    def remover(self, campeonato: Campeonato):
        self.session.delete(campeonato)
        self.session.commit()

    def atualizar(self):
        self.session.commit()