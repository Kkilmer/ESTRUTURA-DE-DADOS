class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        self.area = self.base * self.altura
        return self.area
    
    def mostrar_area(self):
        print(f'Area do retangulo: {self.area}')

retangulo = Retangulo(5,6)
print('Area calculada:', retangulo.calcular_area())
retangulo.mostrar_area()
