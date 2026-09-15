import os

nome = "luiz selim"
idade = 18
altura = 1.65


# FORMATACOES
# forma 1 - classica | exibe qualquer tipo de dado | dá espaço entre informações
print("Nome: ", nome, "Idade: ", idade, "Altura: ", altura)
print("\nNome: ", nome, "\nIdade: ", idade, "\nAltura: ", altura)

# forma 2 - concatenacao (sinal de +) | exibe dados str | dá espaço entre informações
print("Nome: "+ nome+ "Idade: "+ str(idade) + "Altura: "+ str(altura))
print("\nNome: "+ nome+ "\nIdade: "+ str(idade) + "\nAltura: "+ str(altura))

# forma 3 - funcao format()
print("Nome: {0} \nIdade: {1} \nAltura: {2}".format(nome, idade, altura))
print("Nome: {n} \nIdade: {i} \nAltura: {a}".format(n=nome, i=idade, a=altura)) # alias

# forma 4 - f print
print(f"Nome: {nome}")
print(f"\nIdade: {idade}")
print(f"\nAltura: {altura}")

# triple quotes """ """
print(f"""
Nome: {nome}
Idade: {idade}
Altura: {altura}
"""
)

os.system("cls")

v1 = 14.521
v2 = 15319.5141
v3 = 1.5
print(f"""
v1 R$: {v1:8.2f}
v2 R$: {v2:8.2f}
v3 R$: {v3:8.2f}
""")

rcb = 21
print(f"recibo: {rcb:05d}")

qtd1 = 456
qtd2 = 3
p1 = "feijao"
p2 = "carne assada"
os.system("cls")
print(f"{p1} | {qtd1} | {v1} ")
print(f"{p2} | {qtd2} | {v2} ")