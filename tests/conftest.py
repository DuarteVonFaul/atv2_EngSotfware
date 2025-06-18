import pytest
from . import Database






@pytest.fixture()
def session():

    database = Database('sqlite:///:memory:')
    database.criar_tabelas()
    
    with database.get_sessao() as session:
        yield session

    database.drop()
    