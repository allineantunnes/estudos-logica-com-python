# Programa que demonstra conceitos de variáveis e listas em Python
## Neste algoritmo, crie uma variavel que armazene uma string e uma lista que armazene números.

# Criando uma lista vazia para armazenar números
numeros = []

# Variáveis para controle
quantidade = 5  # Quantidade de números a serem inseridos
soma = 0.0      # Variável para armazenar a soma
media = 0.0     # Variável para armazenar a média

# Loop para adicionar números à lista
for i in range(quantidade):
    numero = float(input(f"Digite o {i+1}º número: "))  # Variável temporária
    numeros.append(numero)  # Adicionando à lista
    soma += numero  # Atualizando a soma

# Calculando a média
media = soma / quantidade

# Imprimindo os resultados
print("Números inseridos:", numeros)
print("Soma total:", soma)
print("Média:", media)
