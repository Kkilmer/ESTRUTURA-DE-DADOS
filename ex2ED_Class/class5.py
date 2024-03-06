class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

falar = Pessoa('Kevin', 22)
print(falar.nome)