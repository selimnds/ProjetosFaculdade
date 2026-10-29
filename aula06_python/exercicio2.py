while True:
    print(f''' 
    1. Somar
    2. Subtrair
    3. Multiplicar
    4. Dividir
    ''')

    opc = int(input("Opção: "))
   
    while opc not in [1, 2, 3, 4]:
        
        print("operacao invalida")
        break
    else:
        n1 = int(input("Primeiro número: "))
        n2 = int(input("Segundo número: "))
        match opc:
            case 1:
                print("Resultado: ", n1 + n2)
            case 2:
                print("Resultado: ", n1 - n2)
            case 3:
                print("Resultado: ", n1 * n2)
            case 4:
                if n1 == 0 or n2 == 0: 
                    print("Operação inválida (divisão por 0)")
                else:
                    print("Resultado: ", n1 / n2)
            case _:
                break