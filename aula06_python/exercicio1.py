senha = 1234
tentativas = 3
while tentativas > 0:
    tentativa = int(input("Senha: "))
    if tentativa != senha:
        print("Senha incorreta, tente novamente")
        tentativas = tentativas - 1
        print("Tentativas restantes", tentativas)
    else:
        print("Acesso permitido.")
else:
    print("Acesso bloqueado")