from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Table, ForeignKey

Base = declarative_base()

# Tabela associativa para relação muitos-para-muitos entre Campeonato e Time
campeonato_time = Table(
    'campeonato_time',
    Base.metadata,
    Column('campeonato_id', Integer, ForeignKey('campeonatos.id'), primary_key=True),
    Column('time_id', Integer, ForeignKey('times.id'), primary_key=True)
)