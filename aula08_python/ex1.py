v = []
for n in range (0,5,1):
    i = int(input("digite um valor "))
    v.append(i)
    n += 1
print(v)

# ex2, continuação deste ^

soma = 0
for s in v:
    soma += v[s]
print(soma)