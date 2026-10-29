n = 51
tentativas = 0
while True:
    chute = int(input(": "))
    tentativas += 1
    if chute > n:
        print("Tente um número menor")
    elif chute < n:
        print("Tente um número maior")
    else:
        print(f"Acertou em {tentativas} tentativas!")

    if tentativas > 7:
        print("Tentativas esgotadas")
        break