from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship

from datetime import date
from .time import Time
from .partida import Partida

from . import *



class Campeonato(Base):
    __tablename__ = 'campeonatos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    ano = Column(Integer, nullable=False)

    times = relationship("Time", secondary=campeonato_time, back_populates="campeonatos")
    partidas = relationship("Partida", back_populates="campeonato", cascade="all, delete-orphan")

    def __init__(self, nome: str, ano: int):
        self.nome = nome
        self.ano = ano

    def adicionar_time(self, time: Time):
        if time in self.times:
            raise ValueError("Time já está no campeonato.")
        self.times.append(time)

    def adicionar_partida(self, partida: Partida):
        if partida in self.partidas:
            raise ValueError("Partida já registrada")
        self.partidas.append(partida)

    def listar_partidas_por_dia(self, data: date):
        return [p for p in self.partidas if p.data == data]
    



