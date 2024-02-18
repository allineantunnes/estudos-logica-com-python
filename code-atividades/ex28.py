while True:
    produtos = []

    print('=' * 40)
    print("Supermercado Tabajara".center(40))
    print('=' * 40)

    produto_numero = 1

    while True:
        info_produto = {}

        info_produto["nome"] = input(f"Produto {produto_numero}: ")
        info_produto["valor"] = float(input("Valor: "))
        info_produto["quantidade"] = int(input("Quantidade: "))
        info_produto["numero"] = produto_numero
        info_produto["total"] = info_produto["valor"] * info_produto["quantidade"]

        produtos.append(info_produto)

        resposta = input("Quer inserir outro produto? S/N: ")
        if resposta.lower() != "s":
            break

        produto_numero += 1

    print('=' * 40)
    print("Confirmação e Exclusão".center(40))
    print('=' * 40)

    while True:
        retirar = input("Quer retirar algum produto? S/N: ")
        if retirar.lower() == "n":
            break
        elif retirar.lower() != "s":
            continue

        numero_produto = int(input("Qual o número do produto? "))

        encontrado = False
        for produto in produtos:
            if produto["numero"] == numero_produto:
                produtos.remove(produto)
                encontrado = True
                print(f"Item {produto['nome']} excluído!")
                break

        if not encontrado:
            print("Item não encontrado")

    print('=' * 40)
    print("Resumo das Compras".center(40))
    print('=' * 40)

    total_compras = 0

    print(f"{'Nº':<5}{'Produto':<10}{'Valor':<10}{'Qnt':<10}{'Total':<10}")
    for produto in produtos:
        print(f"{produto['numero']:<5}{produto['nome']:<10}{produto['valor']:<10.2f}{produto['quantidade']:<10}{produto['total']:<10.2f}")
        total_compras += produto["total"]

    print(f"{'--> ':>35}{total_compras:.2f}")

    resposta_final = input("Deseja realizar outra compra? S/N: ")
    if resposta_final.lower() != "s":
        break