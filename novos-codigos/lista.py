def obter_item():
    nome = input("Digite o nome do item (ou pressione Enter para finalizar): ").strip()
    if not nome:
        return None
    while True:
        try:
            preco = float(input(f"Digite o preço de '{nome}': R$ "))
            break
        except ValueError:
            print("Preço inválido. Tente novamente.")
    return {"nome": nome, "preco": preco}

def categorizar_itens(itens):
    categorias = {
        "Barato": [],
        "Médio": [],
        "Caro": []
    }
    for item in itens:
        if item["preco"] < 10:
            categorias["Barato"].append(item)
        elif item["preco"] <= 50:
            categorias["Médio"].append(item)
        else:
            categorias["Caro"].append(item)
    return categorias

def exibir_categorias(categorias):
    for categoria, itens in categorias.items():
        print(f"\nCategoria: {categoria}")
        if itens:
            for item in itens:
                print(f"  - {item['nome']}: R$ {item['preco']:.2f}")
        else:
            print("  Nenhum item nesta categoria.")

def main():
    print("=== Lista de Compras ===")
    itens = []
    while True:
        item = obter_item()
        if item is None:
            break
        itens.append(item)
    categorias = categorizar_itens(itens)
    exibir_categorias(categorias)

if __name__ == "__main__":
    main()