from ..models.estadio import Estadio

class EstadioRepository:
    def __init__(self, session):
        self.session = session

    def adicionar(self, estadio: Estadio):
        self.session.add(estadio)
        self.session.commit()

    def listar_todos(self):
        return self.session.query(Estadio).all()

    def buscar_por_id(self, estadio_id: int):
        return self.session.query(Estadio).get(estadio_id)

    def remover(self, estadio: Estadio):
        self.session.delete(estadio)
        self.session.commit()

    def atualizar(self):
        self.session.commit()