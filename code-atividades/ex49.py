# Cria uma lista de compras simples e funcional para treinar elementos como:
# criação de um menu interativo
# utilização de listas
# utilização de controle de fluxo
# utilização de funções
# ultilização de while, if e else

def exibir_menu():
    print("\n--- LISTA DE COMPRAS ---")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Visualizar lista")
    print("4. Sair")
    return input("Escolha uma opção: ")

def lista_de_compras():
    lista = []
    
    while True:
        opcao = exibir_menu()

        if opcao == '1':
            item = input("Digite o nome do item para adicionar: ").strip()
            if item:
                lista.append(item)
                print(f"'{item}' foi adicionado com sucesso!")
            else:
                print("O nome do item não pode estar vazio.")

        elif opcao == '2':
            if not lista:
                print("A lista está vazia. Nada para remover.")
            else:
                print("\nItens atuais:", lista)
                item = input("Digite o nome do item exato que deseja remover: ").strip()
                if item in lista:
                    lista.remove(item)
                    print(f"'{item}' removido com sucesso!")
                else:
                    print("Item não encontrado na lista.")

        elif opcao == '3':
            if not lista:
                print("\nSua lista está vazia.")
            else:
                print("\n--- SUA LISTA ---")
                for i, item in enumerate(lista, 1):
                    print(f"{i}. {item}")

        elif opcao == '4':
            print("Saindo... Boas compras!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    lista_de_compras()