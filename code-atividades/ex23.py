lista = [1, 2, 3, 4, 5]
soma = 0
for i in lista:
    if i % 2 == 0:
        soma += i
    else:
        soma -= i
print(soma)