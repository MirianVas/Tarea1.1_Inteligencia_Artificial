import random

def AdivinaNumero():
    NumeroSecreto = random.randint(1,100)
    intentos = 0
    adivinado = False

    print("¡Adivina el número entre 1 y 100!")

    while not adivinado:
        try:
            Numero = int(input("Ingrese un numero del 1 al 100: "))
            intentos += 1

            if Numero < NumeroSecreto:
                print("El numero es mayor.")

            elif Numero > NumeroSecreto:
                print("El numero es menor.")

            else:
                adivinado = True
                print(f"¡Felicidades! Has adivinado el numero en {intentos} intentos ")

        except ValueError:
            print("Ingresa un valor numerico")

AdivinaNumero()

