# Solicita uma frase ao usuário
frase = input("Digite uma frase: ").lower()

# Define uma lista de vogais
vogais = "aeiou"

# Conta a quantidade de vogais na frase
quantidade_vogais = sum(1 for letra in frase if letra in vogais)

# Exibe o resultado
print(f"A frase contém {quantidade_vogais} vogais.")
