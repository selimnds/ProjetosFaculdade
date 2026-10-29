# Luiz Henrique Selim Mendes
# Cópia invertida de v1 pra v2

v1 = [41, 72, 39, 4, 35]
v2 = [0] * 5
i = 0

for n in range (0,5,1):
  if v2[n] == 0:
    i += 1
    v2[n] = v1[(i * -1)]

print(v1, v2)