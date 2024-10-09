def ContadorVocales(frase):
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"

    contador = 0

    for letra in frase:
        if letra in vocales:
            contador += 1

    return contador

FraseIngresada = input("Ingrese la frase: ")

TotalVocales = ContadorVocales(FraseIngresada)
print(f"El total de vocales es: {TotalVocales}")