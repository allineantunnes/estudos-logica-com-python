# Neste algoritmo, crie uma variável que armazene uma string e uma lista que armazena várias strings.
# Definindo uma lista de nomes
# Criando uma variável que armazena uma string
mensagem = "Bem-vindo ao nosso programa!"

# Criando uma lista que armazena várias strings (nomes)
nomes = ["Alice", "Beto", "Carla", "Diego", "Elaine"]

# Imprimindo a mensagem de boas-vindas
print(mensagem)

# Saudando cada nome na lista
for nome in nomes:
    print(f"Olá, {nome}!")

# Adicionando um novo nome à lista de nomes
novo_nome = "Fernando"
nomes.append(novo_nome)

# Saudando o novo nome
print(f"Olá, {novo_nome}!")


