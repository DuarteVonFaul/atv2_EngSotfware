from ..models.time import Time
from sqlalchemy.exc import IntegrityError

class TimeRepository:
    def __init__(self, session):
        self.session = session

    def adicionar(self, time: Time) -> Time:
        try:
            self.session.add(time)
            self.session.commit()
            self.session.refresh(time)
            return time
        except IntegrityError as e:
            self.session.rollback()
            raise ValueError(f"Já existe um time com o nome '{time.nome}' ou com o mesmo estádio.")

    def listar_todos(self) -> list[Time]:
        return self.session.query(Time).all()

    def buscar_por_id(self, time_id: int) -> Time:
        return self.session.query(Time).get(time_id)

    def remover(self, time: Time):
        self.session.delete(time)
        self.session.commit()

    def atualizar(self):
        self.session.commit()