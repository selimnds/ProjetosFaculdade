opc = 's'
qtd = 0 

while True:
    num = float(input("numero: "))
    dobro = num * 2
    print(dobro)

    opc = input("continuar? s/n ")
    qtd =+ 1

    while opc != 's' and opc != 'S' and opc != 'n' and opc != 'N':
        opc = input("Erro! S/N? ")
    else:
        if opc == 'n' or opc == 'n':
            break
        
else:
    print("bobg")
    print(qtd) 