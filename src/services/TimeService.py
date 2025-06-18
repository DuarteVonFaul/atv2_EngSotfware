from ..repositories.timeRepository import Time, TimeRepository


class TimeService:
    def __init__(self, session):
        self.repo = TimeRepository(session)

    def criar(self, time:Time) -> Time:
        return self.repo.adicionar(time)

    def buscar(self, time_id:int):
        return self.repo.buscar_por_id(time_id)