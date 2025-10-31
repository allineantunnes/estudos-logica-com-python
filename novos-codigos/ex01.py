# Neste algoritmo, crie uma variável que armazene uma string e uma lista que armazena várias strings.
print("Trabalhando com variáveis python")
variavel = input("Digite um texto para armazenar na variável: ")
print(f"A variável criada foi uma string de valor: {variavel}")
print("Agora vamos criar uma lista para armazenar várias strings.")
lista = []
while True:
    lista_item = input("Digite uma string para adicionar à lista (ou 'sair' para finalizar): ")
    if lista_item.lower() == 'sair':
        break
    lista.append(lista_item)

print("A lista criada contém as seguintes strings:")
for item in lista:
    print(f"- {item}")