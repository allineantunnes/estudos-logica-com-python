# Neste algoritmo, crie uma variável que armazene uma string e uma lista que armazena várias strings.



# Lista de frutas
frutas = ["maçã", "banana", "laranja", "uva", "manga"]

# Dicionário com os valores comerciais das frutas
print("Lista de frutas e seus valores comerciais:")
valores_comerciais = {
    "maçã": 3.50,
    "banana": 2.00,
    "laranja": 2.50,
    "uva": 4.00,
    "manga": 3.00
}

# Enumerando as frutas com seus valores comerciais
for i, fruta in enumerate(frutas, start=1):
    valor = valores_comerciais.get(fruta, "Valor não disponível")
    print(f"{i}. {fruta.capitalize()} - R$ {valor:.2f}")
# Exibindo a lista de frutas e seus valores comerciais
# Exibindo a mensagem




