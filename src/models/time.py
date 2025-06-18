from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .jogador import Jogador
from .estadio import Estadio

from . import *

class Time(Base):
    __tablename__ = 'times'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False,unique=True)
    estadio_id = Column(Integer, ForeignKey('estadios.id'), nullable=False)
    estadio_sede = relationship("Estadio")
    campeonatos = relationship("Campeonato", secondary=campeonato_time, back_populates="times")
    jogadores = relationship("Jogador", back_populates="time", cascade="all, delete-orphan")

    def __init__(self, nome: str, estadio_sede: Estadio):
        self.nome = nome
        self.estadio_sede = estadio_sede

    def adicionar_jogador(self, jogador: Jogador):
        if jogador in self.jogadores:
            raise ValueError("Jogador já está no time.")
        self.jogadores.append(jogador)

    def remover_jogador(self, jogador: Jogador):
        self.jogadores.remove(jogador)

    def altura_media(self) -> float:
        if not self.jogadores:
            return 0.0
        return sum(j.altura for j in self.jogadores) / len(self.jogadores)
