# if condição:
#   Bloco True

import os
os.system("cls")
sexo = input("Qual é o seu sexo? M ou F ")

if sexo == "m":
    print("paga a entrada")

# if condição:
#   Bloco True
# else:
#   Bloco False

id = int(input("Idade: "))
if id >= 18:
    print("maior de idade")
else: 
    print("menor de idade")