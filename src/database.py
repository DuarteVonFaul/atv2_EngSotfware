from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker




class Database:
    def __init__(self, DATABASE_URL):
        self.engine = create_engine(DATABASE_URL, echo=True)
        self.SessionLocal = sessionmaker(bind=self.engine)

    def criar_tabelas(self):
        from .models import jogador, time, estadio, partida, campeonato, Base, campeonato_time
        Base.metadata.create_all(bind=self.engine)

    def get_sessao(self):
        return self.SessionLocal()
    
    def drop(self):
        from .models import Base
        Base.metadata.drop_all(self.engine)
    

