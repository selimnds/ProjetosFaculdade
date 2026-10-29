while True:
    print(f''' 
    Consultar saldo
    Depositar
    Sacar
    Sair
    ''')
    saldo = int(input("Saldo inicial: "))
    op = input("Opção: ")
    val = int(input("Valor: "))

    match op:
        case i if op.lower() == 'consultar' or op.lower() == 'consultar saldo':
            print = saldo

        case i if op.lower() == 'depositar' and val > 0:
            saldo = saldo + val
        
        case i if op.lower() == 'sacar' and val < saldo:
            val = int(input("Valor: "))
            saldo = saldo - val
            if val > saldo:
                print("invalido")
                break
            
        case i if op.lower() == 'sair':
            break