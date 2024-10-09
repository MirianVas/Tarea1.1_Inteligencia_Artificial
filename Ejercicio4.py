class Calculadora:

    a = None
    b = None
    control = True

    while control:
        try:
            if a == None:
                a = int(input("Ingrese el primer numero: "))

            b = int(input("Ingrese el segundo numero: "))

            control = False

        except ValueError:
            print("Ingrese un valor numerico")

    def suma(self):
        return self.a + self.b

    def resta(self):
        return self.a - self.b

    def multiplicacion(self):
        return self.a * self.b

    def division(self):
        if self.b == 0:
            return  "No se puede realizar"
        else:
            return self.a / self.b

cal1 = Calculadora()

print(f"La suma es: {cal1.suma()}")
print(f"La resta es: {cal1.resta()}")
print(f"La multiplicacion es: {cal1.multiplicacion()}")
print(f"La division es: {cal1.division()}")
