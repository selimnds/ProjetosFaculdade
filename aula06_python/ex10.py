prod = input("Produto: ")
pr = float(input("Preço: R$ "))
e = int(input("Estoque inicial: "))
t = 0

while True:
    op = input("Menu (Consultar, Repor, Vender, Sair): ").lower()
    match op:
        case "consultar":
            print(f"{prod}: {e} unidades")
        case "repor":
            q = int(input("Reposição: "))
            if q <= 0:
                print("Quantidade inválida")
                continue
            e += q
        case "vender":
            q = int(input("Venda: "))
            if q <= 0:
                print("Quantidade inválida")
                continue
            if q > e:
                print("Estoque insuficiente")
                continue
            e -= q
            t += q * pr
        case "sair":
            break
        case _:
            print("Opção inválida")

print(f'''Estoque restante: {e} unidades
Valor total vendido: R$ {t:.2f}''')