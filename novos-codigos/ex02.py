# Exercício: Soma de números pares e ímpares
# -------------------------------------------
# 1. O programa deve pedir ao usuário uma lista de números inteiros separados por vírgulas.
# 2. Ele deve calcular e exibir:
#    - A soma dos números pares.
#    - A soma dos números ímpares.

# Solução:
# -------------------------------------------

# Passo 1: Solicitar os números ao usuário
entrada = input("Digite uma lista de números inteiros separados por vírgulas: ")

# Passo 2: Converter a entrada em uma lista de inteiros
numeros = [int(num) for num in entrada.split(",")]

# Passo 3: Inicializar variáveis para armazenar as somas
soma_pares = 0
soma_impares = 0

# Passo 4: Percorrer a lista e classificar os números como pares ou ímpares
for numero in numeros:
    if numero % 2 == 0:  # Se o número for par
        soma_pares += numero
    else:  # Caso contrário, é ímpar
        soma_impares += numero

# Passo 5: Exibir os resultados
print(f"Soma dos números pares: {soma_pares}")
print(f"Soma dos números ímpares: {soma_impares}")

# Exemplo:
# Entrada: 1,2,3,4,5
# Saída:
# Soma dos números pares: 6
# Soma dos números ímpares: 9