n = int(input("Introduce un número entero positivo: "))
if n > 0:
    suma = n * (n + 1) // 2
    print(f"La suma de los primeros {n} números enteros es: {suma}")
else:
    print("Por favor, introduce un número entero positivo.")
