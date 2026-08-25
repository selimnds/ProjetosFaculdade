import os
os.system("cls")
print("exc pelo vscode")

num1 = int(input("digite num1: "))
num2 = int(input("digite num2: "))

soma = num1 + num2
subtracao = num1 - num2
divisao = num1 / num2
divisaoInteira = num1 // num2
modulo = num1 % num2 
exponenciacao = num1 ** num2

operacao = int(input("escolha uma operação:\n" \
"\n 1.soma" \
"\n 2.subtracao" \
"\n 3.divisao" \
"\n 4.divisao inteira" \
"\n 5.modulo" \
"\n 6.exponenciacao \n " \
))

if operacao == 1:
     print(soma)
elif operacao == 2:
    print(subtracao)
elif operacao == 3:
     print(divisao)
elif operacao == 4:
     print(divisaoInteira)
elif operacao == 5:
     print(modulo)
elif operacao == 6:
     print(exponenciacao)