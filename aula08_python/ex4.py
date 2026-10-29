v = [45, -89, 32, -12, 33]
val = int(input('digite um valor: '))
if val not in v:
    print(f"o valor {val} não existe no vetor")
else: 
    print(f"o valor {val} existe no vetor")

n = 0
for i in range(0, 5):
    for j in range(0, 5 - 1 - i):
        if v[j] > v[j + 1]:
            v[j], v[j + 1] = v[j + 1], v[j]

print(v)