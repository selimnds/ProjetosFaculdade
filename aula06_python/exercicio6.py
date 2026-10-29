r = 's'
while r in ['S', 's']:
  limite = int(input("Defina um limite: "))
  if limite >= 1 and limite <= 20:
    n = int(input("Digite um número: "))
    for i in range(1, limite+1):
      print(f"{n} x {i} = {n*i}")
    r = input("Deseja continuar? S/ N ")
  else:
    print("Limite invalido")
    break