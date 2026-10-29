# Luiz Henrique Selim Mendes
# Cópia de v1 para v2

v1 = [41, 72, 39, 4, 35]
v2 = [0] * 5

for n in range(0,5,1):
    if v2[n] == 0:
        v2[n] = v1[n]
print(v1, v2)   