from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from . import *

class Resultado(Base):
    __tablename__ = 'resultados'

    id = Column(Integer, primary_key=True, autoincrement=True)
    num_gols_mandante = Column(Integer, nullable=False)
    num_gols_visitante = Column(Integer, nullable=False)
    partida_id = Column(Integer, ForeignKey('partidas.id'), unique=True)
    partida = relationship("Partida", back_populates="resultado")

    def __init__(self, numGolsMandante: int, numGolsVisitante: int):
        self.num_gols_mandante = numGolsMandante
        self.num_gols_visitante = numGolsVisitante

    def get_pontuacao_mandante(self) -> int:
        if self.num_gols_mandante > self.num_gols_visitante:
            return 3
        elif self.num_gols_mandante == self.num_gols_visitante:
            return 1
        return 0

    def get_pontuacao_visitante(self) -> int:
        if self.num_gols_visitante > self.num_gols_mandante:
            return 3
        elif self.num_gols_visitante == self.num_gols_mandante:
            return 1
        return 0

    def jogo_saiu_empatado(self) -> bool:
        return self.num_gols_mandante == self.num_gols_visitante
