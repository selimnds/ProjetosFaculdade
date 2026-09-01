qntd = int(input("Digite uma quantia (inteira): "))
cem = qntd // 100
resto = qntd % 100
cnqt = resto // 50
resto = resto % 50
vnt = resto // 20
resto = resto % 20
dez = resto // 10

print(f"{cem} cédulas de 100 \n {cnqt} cédula de 50 \n {vnt} cédula de 20 \n {dez} cédula de 10")