# Crie uma lista numériaca aleatória depois busque a média de valores, menor valor e o maior valor.

import random

# Gerar uma lista numérica aleatória
numeros = [random.randint(1, 100) for _ in range(10)]

print(f"Lista de números: {numeros}")

# Calcular a média
media = sum(numeros) / len(numeros)

# Encontrar o menor valor
menor = min(numeros)

# Encontrar o maior valor
maior = max(numeros)

# Exibir os resultados
print(f"Média: {media:.2f}")
print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}") 