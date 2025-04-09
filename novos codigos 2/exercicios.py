# Neste algoritimo crie uma variavel que armazene uma string e uma lista que armazena várias strings.

# problema da mochila

# Função para resolver o Knapsack Problem usando programação dinâmica
def knapsack(capacidade, pesos, valores, n):
    # Criando uma matriz para armazenar os resultados
    dp = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]

    # Preenchendo a matriz
    for i in range(1, n + 1):
        for w in range(1, capacidade + 1):
            if pesos[i - 1] <= w:
                dp[i][w] = max(valores[i - 1] + dp[i - 1][w - pesos[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacidade]

# Exemplo de uso
valores = [60, 100, 120]  # Valores dos itens
pesos = [10, 20, 30]      # Pesos dos itens
capacidade = 50           # Capacidade máxima da mochila
n = len(valores)          # Número de itens

resultado = knapsack(capacidade, pesos, valores, n)
print(f"O valor máximo que pode ser colocado na mochila é: {resultado}")

