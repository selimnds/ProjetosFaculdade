# Luiz Henrique Selim Mendes
# Maior 

v = [41, 72, 39, 4, 35]
maior = 0 

for i in range (0,4,1):
    if v[i] > v [i + 1] and v[i] > v[i - 1]:
        maior = v[i]
print(v)
print(maior)