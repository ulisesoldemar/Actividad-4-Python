from math import pi

def main():
    opt = ''
    print("Calcular el área de figuras")
    while True:
        print("1) Área de un cuadrado.")
        print("2) Área de un triángulo.")
        print("3) Área de un cítculo.")
        print("4) Salir.")
        opt = input("Selecciona una opción: ")
        if opt == '1':
            area_cuadrado()
            continue
        elif opt == '2':
            area_triangulo()
            continue
        elif opt == '3':
            area_circulo()
            continue
        elif opt == '4':
            print("Hasta luego.")
            break
        else:
             print("Opción no válida, reintenta.")

def area_cuadrado():
    print("Área de un cuadrado.")
    while True:
        try:
            lado = float(input("Ingresa el tamaño de lado del cuadrado en centímetros: "))
        except ValueError:
            print("Dato no válido, reintenta.")
            continue
        if lado > 0:
            break
    print("Area del cuadrado:", lado**2)

def area_triangulo():
    print("Área de un triángulo")
    while True:
        try:
            base = float(input("Ingresa el tamaño de la base en centímetros: "))
            altura = float(input("Ingresa el tamaño de la altura en centímetros: "))
        except ValueError:
            print("Algún dato no fue válido, reintenta.")
            continue
        if base > 0 and altura > 0:
            break
    print("Área del triángulo:", (base*altura) / 2)

def area_circulo():
    print("Área de un círculo")
    while True:
        try:
            radio = float(input("Ingresa el tamaño del radio en centímetros: "))
        except ValueError:
            print("Dato no válido, reintenta.")
            continue
        if radio > 0:
            break
    print("Área del círculo:", pi * (radio**2))

main()