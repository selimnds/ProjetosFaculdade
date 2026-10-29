# Luiz Henrique Selim Mendes
# Ordenação crescente

v = [45, -89, 32, -12, 33]

for i in range (0, 5, 1):
    for n in range(0, 4, 1):
        if v[n] > v[n+1]:
            v[n], v[n+1] = v[n+1], v[n]
print(v)

