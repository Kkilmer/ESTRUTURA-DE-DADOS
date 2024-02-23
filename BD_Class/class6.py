class Produto:
    def __init__(self, nome, preco, quant):
        self.nome = nome
        self.preco = preco
        self.quant = quant

    def calcular_total(self):
        self.total = float(self.preco * self.quant)
        return self.total

compra = Produto("BomPreco", 150, 2)
print('Valor para pagar é:', compra.calcular_total())