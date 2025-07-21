# Crie um programa que gerencie uma lista de tarefas (To-Do List).
# O programa deve apresentar um menu de opções ao usuário, onde seja possível:
# 1. Adicionar uma nova tarefa à lista.
# 2. Listar todas as tarefas cadastradas.
# 3. Remover uma tarefa da lista.
# 4. Sair do programa.
# O código utiliza a estrutura match case para o controle das opções do menu.
# A lista de tarefas é armazenada em uma lista e manipulada conforme a interação do usuário. 
#--------------------------------------------------------------------------------------------


# Importa o módulo 'os' para utilizar o comando de limpar a tela do terminal
import os

# Define uma função que exibe o menu de opções ao usuário
def mostra_menu():
    print("\nBem-vindo ao Gerenciador de Tarefas!")
    print("Menu de Opções:")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Remover Tarefa")
    print("4. Sair")

# Cria uma lista vazia que armazenará as tarefas adicionadas
tarefas = []

# Inicia um loop infinito para manter o programa rodando até o usuário escolher sair
while True:
    os.system('clear') # Limpa a tela do terminal (no Windows pode usar 'cls')
    mostra_menu() 

    opcao = input("Selecione uma opção (1-4): ") 

    # Estrutura match case para tratar a opção selecionada
    match opcao:
        # Opção 1: Adicionar uma nova tarefa
        case "1":
            tarefa = input("Digite a tarefa a ser adicionada: ") 
            tarefas.append(tarefa)
            print(f"Tarefa '{tarefa}' adicionada com sucesso!") 
        
        # Opção 2: Listar todas as tarefas
        case "2":
            if tarefas:
                os.system('clear')
                print("\nTarefas:")
                for idx, tarefa in enumerate(tarefas, start=1):
                    print(f"{idx}. {tarefa}")
            else:
                print("Nenhuma tarefa cadastrada.")

        # Opção 3: Remover uma tarefa
        case "3":
            if tarefas:
                os.system('clear')
                try:
                    print("\nTarefas:")
                    for idx, tarefa in enumerate(tarefas, start=1):
                        print(f"{idx}. {tarefa}")
                    indice = int(input("Digite o número da tarefa a ser removida: ")) - 1
                    if 0 <= indice < len(tarefas):
                        tarefa_removida = tarefas.pop(indice)
                        print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
                    else:
                        print("Número inválido. Tente novamente.")
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número.")
            else:
                print("Nenhuma tarefa para remover.")
        
        # Opção 4: Sair do programa
        case "4":
            print("Saindo do Gerenciador de Tarefas. Até logo!")
            break

        # Caso o usuário selecione uma opção inválida
        case _:
            print("Opção inválida. Por favor, selecione uma opção válida.")


