# Neste algoritmo, crie uma variável que armazene uma string e uma lista que armazena várias strings.

mensagem = input("Digite uma mensagem: ")

lista = []
variaveis = int(input("Quantas frutas você deseja adicionar à lista? "))

for _ in range(variaveis):
    info = input("Digite o nome da fruta: ")
    lista.append(info)

print("Mensagem:", mensagem)
print("Lista de strings:", lista)