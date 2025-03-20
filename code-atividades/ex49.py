# Solicita a palavra ao usuário
palavra = input("Digite uma palavra: ").strip().lower()

# Inverte a palavra e compara com a original
if palavra == palavra[::-1]:
    print(f"A palavra '{palavra}' é um palíndromo!")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")
