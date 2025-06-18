from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Estatisticas(Base):
    __tablename__ = 'estatisticas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    gols = Column(Integer, nullable=False)
    assistencias = Column(Integer, nullable=False)

    jogador_id = Column(Integer, ForeignKey('jogadores.id'), unique=True)
    jogador = relationship("Jogador", back_populates="estatisticas")

    def __init__(self, gols: int, assistencias: int):
        self.gols = gols
        self.assistencias = assistencias