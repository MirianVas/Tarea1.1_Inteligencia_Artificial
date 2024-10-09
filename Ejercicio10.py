import random
import string


def GenerarContrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation

    if longitud < 8:
        print("La longitud mínima para la contraseña es 8 caracteres. Se generará una contraseña de 8 caracteres.")
        longitud = 8

    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    return contrasena

LongitudContrasena = int(input("Ingrese la longitud deseada para su contraseña (mínimo 8 caracteres): "))

ContrasenaGenerada = GenerarContrasena(LongitudContrasena)
print(f"Tu contraseña generada es: {ContrasenaGenerada}")