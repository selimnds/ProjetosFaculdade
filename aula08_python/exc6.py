# Luiz Henrique Selim Mendes
# Determinação se existe/não existe

v = [45, -89, 32, -12, 33]
val = int(input('digite um valor: '))
if val not in v:
    print(f"o valor {val} não existe no vetor")
else: 
    print(f"o valor {val} existe no vetor")