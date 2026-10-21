plc = plcIn = ''
s = i = prc = h = 0
while True:
    plcIn = input("Placa: ")
    if plcIn.upper() == 'FIM':
        break
    h = int(input("Horas: "))
    if h <= 0:
        print("Horas inválidas")
        continue
    prc = 5*(h-1) + 8
    if h > 8:
        prc = (5*(h-1) + 8) + 20
    plc = plc + f"{plcIn.upper()}: R$ {prc:.2f}\n"
    i += 1
    s += prc
print(plc, end="")
print(f'''Veículos atendidos: {i}
Total arrecadado: R$ {s:.2f}''')