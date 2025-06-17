from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

from datetime import date
from datetime import date
from .time import Time
from .estadio import Estadio
from .resultado import Resultado

from . import *

class Partida(Base):
    __tablename__ = 'partidas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(Date, nullable=False)

    mandante_id = Column(Integer, ForeignKey('times.id'), nullable=False)
    visitante_id = Column(Integer, ForeignKey('times.id'), nullable=False)
    estadio_id = Column(Integer, ForeignKey('estadios.id'), nullable=False)

    resultado = relationship("Resultado", uselist=False, back_populates="partida", cascade="all, delete-orphan")

    mandante = relationship("Time", foreign_keys=[mandante_id])
    visitante = relationship("Time", foreign_keys=[visitante_id])
    estadio = relationship("Estadio")

    campeonato_id = Column(Integer, ForeignKey('campeonatos.id'))
    campeonato = relationship("Campeonato", back_populates="partidas")

    def __init__(self, mandante: Time, visitante: Time, estadio: Estadio, data: date):
        if not mandante or not visitante or not estadio or not data:
            raise ValueError("Dados inválidos para criar partida.")
        if estadio != mandante.estadio_sede and estadio != visitante.estadio_sede:
            raise ValueError("Estádio não corresponde ao estádio-sede de nenhum dos times.")
        self.mandante = mandante
        self.visitante = visitante
        self.estadio = estadio
        self.data = data

    def definir_resultado(self, gols_mandante: int, gols_visitante: int):
        if gols_mandante < 0 or gols_visitante < 0:
            raise ValueError("Gols não podem ser negativos.")
        self.resultado = Resultado(gols_mandante, gols_visitante)
