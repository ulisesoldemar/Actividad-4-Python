while True:
    try: 
        dia = int(input("Ingresa tu dia de nacimiento: "))
        mes = int(input("Ingresa tu mes de nacimiento: "))
    except ValueError:
        print("Algún dato no fue válido, reintenta.")
        continue
    if dia > 31 or dia < 1:
        print("No fue un día válido, reintenta.")
        continue
    elif mes > 12 or mes < 1:
        print("No fue un mes válido, reintenta.")
        continue
    else:
        break

if mes == 1:
    if dia <= 19:
        print("Capricornio")
    else:
        print("Acuario")
elif mes == 2:
    if dia <= 18:
        print("Acuario")
    while dia >= 28:
        try:
            dia = int(input("No fue un día válido para febrero, reintenta: "))
        except ValueError:
            print("Dato no válido, reintenta,")
            continue
    else:
        print("Piscis")
elif mes == 3:
    if dia <= 20:
        print("Piscis")
    else:
        print("Aries")
elif mes == 4:
    if dia <= 19:
        print("Aries")
    else:
        print("Tauro")
elif mes == 5:
    if dia <= 20:
        print("Tauro")
    else:
        print("Géminis")
elif mes == 6:
    if dia <= 20:
        print("Géminis")
    else:
        print("Cáncer")
elif mes == 7:
    if dia <= 22:
        print("Cáncer")
    else:
        print("Leo")
elif mes == 8:
    if dia <= 22:
        print("Leo")
    else:
        print("Virgo")
elif mes == 9:
    if dia <= 22:
        print("Virgo")
    else:
        print("Libra")
elif mes == 10:
    if dia <= 22:
        print("Libra")
    else:
        print("Escorpio")
elif mes == 11:
    if dia <= 21:
        print("Escorpio")
    else:
        print("Sagitario")
elif mes == 12:
    if dia <= 21:
        print("Sagitario")
    else:
        print("Capricornio")
else:
    print("Mes no válido")
