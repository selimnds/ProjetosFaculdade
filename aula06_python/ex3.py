i = 0
notas = 0
soma = 0
while notas != -1:
  notas = float(input("Notas: "))
  if notas > 10 or notas < 0 and notas != -1:
      print("Nota invalida")
  else:
      i += 1
      soma = soma + notas
      media = soma / i

      if media >= 9:
        c = "Ótimo"
      elif media <= 7 and media >= 8:
        c = "Bom"
      elif media == 6:
        c = "Regular"
      else:
        c = "Ruim"

print(f'''
Quantidade: {i}
Média: {media}
Classificação: {c}
''')