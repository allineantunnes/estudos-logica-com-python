print('=' * 40)
print('{:^40}'.format('Supermercado Tabajara'))
print('=' * 40)
info_produto = dict()
produtos = list()

while True:

    numero = len(produtos) + 1
    info_produto['numero'] = numero
    info_produto['nome'] = str(input(f'Produto {numero}: '))
    info_produto['valor'] = float(input('Valor: '))
    info_produto['qtd'] = int(input('Quantidade: '))
    info_produto['total'] = (info_produto['valor'] * info_produto['qtd'])
    produtos.append(info_produto.copy())
    continuar = input('Quer inserir outro produto?S/N ')

    if continuar.lower() == 'n':
        break
    elif continuar.lower() != 's':
        print('Digite novamente! ', end="")
        continuar = input('Quer inserir outro produto?S/N ')


print('=' * 40)
print('{:^40}'.format('Confirmação e Exclusão'))
print('=' * 40)

while True:

    retirar = input('Quer retirar algum produto?S/N ')

    if retirar.lower() == 'n':
        break
    elif retirar.lower() != 's':
        retirar = input('Quer retirar algum produto?S/N ')

    num_produto = int(input("Qual o número do produto? "))
    produto_encontrado = None

    for produto in produtos:
        if produto["numero"] == num_produto:
            produto_encontrado = produto
            produtos.remove(produto)
            print(f"Item {produto['nome']} excluído!")
            break

    if produto_encontrado is None:
        print("Item não encontrado")

print('=' * 50)
print('{:^50}'.format('Resumo das Compras'))
print('=' * 50)
total_compras = 0
print("{:<5} {:<15} {:<10} {:<10} {:<10}".format("Nº", "Produto", "Valor", "Qnt", "Total"))

for produto in produtos:
    numero, nome, valor, qtd, total = produto.values()
    total_compras += total
    print("{:<5} {:<15} {:<10.2f} {:<10} {:<10.2f}".format(numero, nome, valor, qtd, total))

print("\nTotal: {:>25.2f}".format(total_compras))