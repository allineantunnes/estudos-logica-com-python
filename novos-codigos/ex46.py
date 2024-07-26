import time
from datetime import datetime

# Variáveis globais
saldo = 1000  # Saldo inicial do caixa eletrônico
valor_sacado = 0  # Valor sacado no último saque
data_saque = None  # Data e hora do último saque

def calcular_combinacoes(valor):
    """
    Calcula as combinações possíveis de notas para um determinado valor.

    Args:
        valor (int): O valor a ser sacado.

    Returns:
        list: Lista de tuplas com as combinações de notas disponíveis.
    """
    notas_disponiveis = [50, 20, 10]
    combinacoes = []

    # Gera combinações de notas
    for quantidade_nota50 in range(0, valor // 50 + 1):
        for quantidade_nota20 in range(0, (valor - quantidade_nota50 * 50) // 20 + 1):
            quantidade_nota10 = (valor - (quantidade_nota50 * 50 + quantidade_nota20 * 20)) // 10
            
            # Verifica se a combinação é válida
            if (quantidade_nota50 * 50 + quantidade_nota20 * 20 + quantidade_nota10 * 10) == valor:
                combinacoes.append((quantidade_nota50, quantidade_nota20, quantidade_nota10))

    # Ordena as combinações pelo número total de notas
    combinacoes.sort(key=lambda x: x[0] + x[1] + x[2])

    # Seleciona as 3 combinações com a menor quantidade de notas
    return combinacoes[:3]

def saque_dinheiro():
    """
    Realiza o saque do valor especificado exibindo as combinações possíveis de notas.
    """
    global saldo, valor_sacado, data_saque
    print("Favor informar o valor a ser sacado:")
    valor_saque = input("Valor do saque: R$ ")
    if not valor_saque.replace(".", "").isdigit():
        print("Dados inválidos, encerrando a operação")
        return

    valor_saque = float(valor_saque)

    # Verifica se o valor está dentro do intervalo permitido
    if valor_saque < 10 or valor_saque > 600:
        print("Impossível sacar esse valor nesse caixa eletrônico com as notas disponíveis!")
        return

    # Verifica se o valor é múltiplo de 10
    if valor_saque % 10 != 0:
        print("Impossível sacar esse valor nesse caixa eletrônico com as notas disponíveis!")
        return

    # Verifica se há saldo suficiente
    if valor_saque > saldo:
        print("Saldo insuficiente para realizar o saque.")
        return

    # Calcula combinações de notas
    combinacoes = calcular_combinacoes(int(valor_saque))

    if not combinacoes:
        print("Não foi possível encontrar combinações de notas para o valor solicitado.")
        return

    # Exibe as combinações disponíveis
    print("Combinações de notas disponíveis:")
    for i, (q50, q20, q10) in enumerate(combinacoes):
        partes = []
        if q50 > 0:
            partes.append(f"{q50} nota(s) de R$ 50,00")
        if q20 > 0:
            partes.append(f"{q20} nota(s) de R$ 20,00")
        if q10 > 0:
            partes.append(f"{q10} nota(s) de R$ 10,00")

        print(f"Opção {i + 1}: {', '.join(partes)}")

    # Solicita ao usuário que escolha uma combinação
    try:
        escolha = int(input("Escolha a combinação de notas desejada: ")) - 1
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
        return

    if 0 <= escolha < len(combinacoes):
        print("Imprimindo, aguarde as notas serem contabilizadas e impressas...")
        time.sleep(1)
        q50, q20, q10 = combinacoes[escolha]
        if q50 > 0:
            print(f"{q50} nota(s) de R$ 50,00")
        if q20 > 0:
            print(f"{q20} nota(s) de R$ 20,00")
        if q10 > 0:
            print(f"{q10} nota(s) de R$ 10,00")
        print("Saque realizado com sucesso!")
        saldo -= valor_saque  # Atualiza o saldo
        valor_sacado = valor_saque  # Atualiza o valor sacado
        data_saque = datetime.now()  # Registra a data e hora do saque
    else:
        print("Opção inválida!")

def depositar_dinheiro():
    """
    Realiza o depósito de dinheiro em uma conta.
    """
    global saldo
    print("Favor informar o nome do banco:")
    banco = input("Nome do banco: ")
    if not isinstance(banco, str):
        print("Dados inválidos, encerrando a operação")
        return

    print("Favor informar o número da conta a ser favorecida:")
    conta = input("Número da conta: ")
    if not conta.isdigit():
        print("Dados inválidos, encerrando a operação")
        return

    print("Favor informar o número da agência:")
    agencia = input("Número da agência: ")
    if not agencia.isdigit():
        print("Dados inválidos, encerrando a operação")
        return

    print("Favor informar valor a ser depositado:")
    valor_depositado = input("Valor do depósito: R$ ")
    if not valor_depositado.isdigit():
        print("Dados inválidos, encerrando a operação")
        return

    valor_depositado = float(valor_depositado)
    saldo += valor_depositado  # Atualiza o saldo
    print(f"Depósito de R$ {valor_depositado:.2f} realizado com sucesso na conta {conta} da agência {agencia} do banco {banco}!")

def main():
    """
    Função principal para executar o programa de saque e depósito de dinheiro.
    """
    global valor_sacado, saldo, data_saque
    # Exibe as notas disponíveis antes de solicitar o valor do saque
    print("NOTAS DISPONÍVEIS: R$ 10,00, R$ 20,00, R$ 50,00")
    while True:
        print("MENU:")
        print("1 - Depósito")
        print("2 - Saque")
        print("3 - Extrato")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            depositar_dinheiro()
        elif opcao == "2":
            saque_dinheiro()
        elif opcao == "3":
            print("Extrato em preparação...")
            time.sleep(1)
            print(f"Saldo atual de R$ {saldo:.2f}")
            if data_saque:
                print(f"Saque realizado em {data_saque.strftime('%d/%m/%Y %H:%M')} no valor de R$ {valor_sacado:.2f}")
            else:
                print("Nenhum saque realizado ainda.")
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
