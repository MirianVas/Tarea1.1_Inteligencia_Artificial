class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor
        return self.saldo

    def retirar(self, valor):
        if self.saldo < valor:
            print("Saldo insuficiente para realizar el retiro.")
        else: self.saldo -= valor
        return self.saldo

    def MostrarSaldo(self):
        print(f"Nombre del titular: {self.titular}")
        print(f"El saldo actual es: {self.saldo}")

cb1 = CuentaBancaria("Jose Luis Perales", 0)

cb1.depositar(1000.50)
cb1.depositar(800)
cb1.depositar(5000)
cb1.retirar(800)
cb1.retirar(1500)
cb1.MostrarSaldo()