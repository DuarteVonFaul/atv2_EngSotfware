from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from datetime import date

from . import *

class Jogador(Base):
    __tablename__ = 'jogadores'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    data_nascimento = Column(Date, nullable=False)
    altura = Column(Float, nullable=False)

    time_id = Column(Integer, ForeignKey('times.id'))
    time = relationship("Time", back_populates="jogadores")

    def __init__(self, nome: str, data_nascimento: date, altura: float):
        if altura < 0:
            raise ValueError("Altura não pode ser negativa.")
        if data_nascimento > date.today():
            raise ValueError("Data de nascimento inválida.")
        
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.altura = altura

    def calcular_idade(self) -> int:
        hoje = date.today()
        idade = hoje.year - self.data_nascimento.year - (
            (hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day)
        )
        return idade
