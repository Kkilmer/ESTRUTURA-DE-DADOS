class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

detalhes = Carro("VW", "Polo", "2024")
print(detalhes.marca)
print(detalhes.modelo)
print(detalhes.ano)