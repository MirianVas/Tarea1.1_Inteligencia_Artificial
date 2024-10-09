class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return self.base + self.altura

r1 = Rectangulo(5, 3)

print(f"El area es: {r1.area()}")
print(f"El perimetro es: {r1.perimetro()}")