def fibonacci(n):

    a, b = 0, 1

    for i in range(n):
        print(a, end=", " if i < n-1 else "\n")
        a, b = b, a + b

n = None
control = True

while control:
    try:
        if n is None:
            n = int(input("Ingrese el número de términos: "))
            control = False

    except ValueError:
        print("Ingrese un valor numerico")

if n <= 0:
    print("Por favor ingrese un número entero positivo.")
else:
    print("Secuencia de Fibonacci:")
    fibonacci(n)


