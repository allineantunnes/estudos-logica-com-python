dicionario = {'a': 1, 'b': 2, 'c': 3}
soma = 0
for chave, valor in dicionario.items():
    if valor % 2 == 0:
        soma += valor
    else:
        soma -= valor
print(soma)