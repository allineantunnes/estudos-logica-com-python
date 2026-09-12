# Exemplo de Dicionário

produto = {
    "nome": "Teclado",
    "preco": 120.00,
    "quantidade": 5
}

print("\nDados do produto:")

for chave, valor in produto.items():
    print(f"{chave}: {valor}")