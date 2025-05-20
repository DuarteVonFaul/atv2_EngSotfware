from datetime import date

class Jogador:
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