# Luiz Henrique Selim Mendes
# Ordenação decrescente

v = [41, 72, 39, 4, 35]

for i in range (0, 5, 1):
    for n in range(0, 4, 1):
        if v[n] < v[n+1]:
            v[n], v[n+1] = v[n+1], v[n]
print(v)

