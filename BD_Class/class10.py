class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def aumentar_salario(self):
        self.aumento = float(self.salario) * 0.05
        return self.aumento

promocao = Funcionario("Kevin", 1420, "Supervisor")
print('Promocao de hoje vai para Kevin com o acrescimo de:', promocao.aumentar_salario())