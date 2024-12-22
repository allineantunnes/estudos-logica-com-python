# Solicita ao usuário para inserir uma string
minha_string = input("Digite uma string: ")

# Solicita ao usuário para inserir várias strings para a lista
minha_lista = []
while True:
    entrada = input("Digite uma string para adicionar à lista (ou 'sair' para terminar): ")
    if entrada.lower() == 'sair':
        break
    minha_lista.append(entrada)

# Exibe a string e a lista
print("String armazenada:", minha_string)
print("Lista armazenada:", minha_lista)# Neste algoritmo, crie uma variável que armazene uma string e uma lista que armazena várias strings.
