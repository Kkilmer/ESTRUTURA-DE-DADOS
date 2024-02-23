class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        self.media = self.notas / 3
        return self.media
    
aluno = Aluno("Kevin", 90)
print("Resultado da sua media:", aluno.calcular_media())