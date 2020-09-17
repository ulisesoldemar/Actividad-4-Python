def factorial(n:int):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return ValueError
    else:
        return n * factorial(n - 1)

while True:
    try:
        n = 0
        e = 0
        limite = int(input("Ingresa el límite de iteraciones para el cálculo de e: "))
        if limite <= 0 :
            print("El límite debe ser mayor a 0.") 
            continue
        while n < limite:
            e += 1/factorial(n)
            n += 1
        break
    except ValueError:
        print("Dato no válido, reintenta.")
        continue
    except RecursionError:
        print("Límite muy grande, ingresa un valor más pequeño.")
        continue
print("Valor de e con", limite, "de precisión:", e)
