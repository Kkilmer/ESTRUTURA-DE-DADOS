class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calculo_valor_raio(self):
        return self.raio

    def mostrar_circulo(self):
        area = 3.14 * (self.raio ** 2)
        print(f'Área do círculo: {area}')

circulo = Circulo(5)

print("Raio do círculo:", circulo.calculo_valor_raio())

circulo.mostrar_circulo()
