from sqlalchemy import Column, Integer, String

from . import *


class Estadio(Base):
    __tablename__ = 'estadios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    endereco = Column(String(200), nullable=False)

    def __init__(self, nome: str, endereco: str):
        self.nome = nome
        self.endereco = endereco
