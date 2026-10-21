c = 0
e = int(input("Eleitores: "))
p1 = p2 = p3 = b = n = 0
w = ''

while c < e:
    c += 1
    v = int(input('''
Escolha o seu voto.
1. Projeto 1
2. Projeto 2
3. Projeto 3
0. Voto em branco
Qualquer outra tecla: voto nulo
'''))
    match v:
      case 1:
        p1 += 1
      case 2:
        p2 += 1
      case 3:
        p3 += 1
      case 0:
        b += 1
      case _:
        n += 1

    if p1 > p2 and p1 > p3:
      w = 'Projeto 1 é o vencedor'
    elif p2 > p1 and p2 > p3:
      w = 'Projeto 2 é o vencedor'
    elif p3 > p1 and p3 > p2:
      w = 'Projeto 3 é o vencedor'
    else:
      w = 'Nenhum projeto é vencedor'

else:
  print(f'''
  Eleitores: {e}
  Projeto 1: {p1}
  Projeto 2: {p2}
  Projeto 3: {p3}
  Brancos: {b}
  Nulos: {n}
  {w}
  ''')