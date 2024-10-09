class NumeroPrimo:
    def __init__(self, numero):
        self.numero = numero

    def es_primo(self):
        if self.numero < 2:
            return False
        for i in range(2, self.numero):
            if self.numero % i == 0:
                return False
        return True

numero = None
control = True

while control:
    try:
        if numero is None:
            numero = int(input("Ingrese un numero: "))
            control = False

    except ValueError:
        print("Ingrese un valor numerico")

if NumeroPrimo(numero).es_primo():
    print("El numero es primo")
else:
    print("El numero no es primo")

