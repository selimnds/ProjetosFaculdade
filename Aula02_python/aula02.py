import os
os.system("cls")

def Aula2Variaveis():
    print("Aula 2 - Variáveis de memória")
    print("Como o nome sugere, variáveis de memória são um local alocado na memória do computador para armazenar um valor mutável durante a execução do programa")

    print("Regras para nomenclatura:\n" \
    "- Começar com letra \n" \
    "- Sem caracteres especiais \n" \
    "- Não pode ser palavra reservada da linguagem")

    print("Python é FRACAMENTE tipada. Por quê? Porque podemos mudar o tipo da variável durante a execução do programa")

def Aula2Algoritmo():
    print("ALGORITMOS - Sequencias logicas e bem definidas de passsos para realizarmos uma tarefa")
    print("Algoritmos não é a resposta do problema e sim o *COMO8 chegamos no resultado")

print("Módulos: 1. Variáveis, 2. Algoritmo")

modulo = input("Qual módulo deseja? \n")

if modulo == "1":
    Aula2Algoritmo()
elif modulo == "2":
    Aula2Algoritmo()
else:
    print("escolha um modulo valido")