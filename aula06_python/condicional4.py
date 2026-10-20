while True:
    n1 = float(input("n1: "))
    if n1 < 0 and n1 > 10:
        print("erro")
        continue
    n2 = float(input("n2: "))
    if n2 < 0 and n2 > 10:
        print("erro")
        continue

    media = (n1+n2) / 2
    print(media)

    opc = input("continuar? s/n")

    # while opc not in ['S', 's', 'n', 'N']
    while opc != 's' and opc != 'S' and opc != 'n' and opc != 'N':
            opc = input("Erro! S/N? ")
    else:
        if opc == 'n' or opc == 'n':
                break



