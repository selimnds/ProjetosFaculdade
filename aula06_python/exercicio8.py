p = n = s = par = impar = maior = menor = 0

while True:
  i = int(input("Número(s): "))

  if i > 0:
    p += 1
  elif i < 0:
    n += 1
  elif i == 0 and p != 0 and n != 0:
    break

  if i % 2 == 0:
    par += 1
  else:
    impar += 1

  s += i

  if i > maior:
    maior = i
  elif i < maior and i < menor:
    menor = i


print(f'''
{p}, {n}
{par}, {impar}
{s}
{maior}, {menor}
''')
