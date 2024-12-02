# Neste algoritmo, crie uma variável que armazene uma string e uma lista que armazena várias strings.

# Variável que armazena uma string
minha_string = "Essa é uma string."

# Lista que armazena várias strings
minha_lista = ["Python", "é", "muito", "divertido"]

# Exibindo os valores
print("Minha String:", minha_string)
print("Minha Lista:", minha_lista)

# Acessar Elementos da Lista
print(minha_lista[0])  
print(minha_lista[-1])  

# Adicionar um Item à Lista
minha_lista.append("mesmo!")
print(minha_lista)  # ['Python', 'é', 'muito', 'divertido', 'mesmo!']

# Concatenar a String com um Item da Lista:
nova_frase = minha_string + " " + minha_lista[0]
print(nova_frase)  # Essa é uma string. Python


