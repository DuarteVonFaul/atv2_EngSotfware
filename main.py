from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models.resultado import *
from src.models.jogador import *
from src.models.time import *
from src.models.partida import *
from src.models.estadio import *
from src.models.campeonato import *


engine = create_engine('sqlite:///database.sqlite3', echo=True)

Base.metadata.create_all(engine)