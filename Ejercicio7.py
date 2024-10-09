numero=None
control = True

while control:
    try:
        if numero is None:
            numero = int(input("Ingresa un numero: "))
            control = False

    except ValueError:
        print("Ingrese un valor numerico")

def TablaMultiplicar(numero):
    print(f"Tabla de multiplicar del {numero}")
    for i in range(1,11):
        multiplicacion = numero * i
        print(f"{numero} x {i} = {multiplicacion}")

TablaMultiplicar(numero)