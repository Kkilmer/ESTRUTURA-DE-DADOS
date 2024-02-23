class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_perimetro(self):
            self.perimetro = self.lado1 + self.lado2 + self.lado3
            return self.perimetro
        
    def calcular_altura(self):
            self.altura = (self.lado2 * 7) / 2
            return self.altura
        
perimetro = Triangulo(15, 13, 10)
print('Valor do perimetro é:', perimetro.calcular_perimetro(), 
      "Se quiser saber a altura: ", perimetro.calcular_altura())
