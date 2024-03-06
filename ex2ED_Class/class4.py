class ContaBancaria:
    def __init__(self, saldo, titular):
        self.saldo = saldo
        self.titular = titular

    def calculo_entrada(self):
        self.entrada = self.saldo
        return self.entrada
    
    def calculo_saida(self):
        self.saida = self.saldo - self.entrada
        return self.saida
    
    def mostrar_resultado(self):
        print(f'Valor em conta: {self.entrada}')
        print(f'Extrato de saidas: {self.saida}')

saldo = ContaBancaria(5000, "Kevin")
print('Saldo em conta correte:', saldo.calculo_entrada())
saldo.calculo_saida()



