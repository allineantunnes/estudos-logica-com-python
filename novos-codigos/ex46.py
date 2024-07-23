import time

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

def saque_dinheiro(valor):
    """
    Realiza o saque do valor especificado exibindo as combinações possíveis de notas.

    Args:
        valor (int): O valor a ser sacado.
    """
    # Verifica se o valor está dentro do intervalo permitido
    if valor < 10 or valor > 600:
        print("Impossível sacar esse valor nesse caixa eletrônico com as notas disponíveis!")
        return

    # Verifica se o valor é múltiplo de 10
    if valor % 10 != 0:
        print("Impossível sacar esse valor nesse caixa eletrônico com as notas disponíveis!")
        return

    # Calcula combinações de notas
    combinacoes = calcular_combinacoes(valor)

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
        print("Entrada inválida! Por favor, insira um número.")
        return

    if 0 <= escolha < len(combinacoes):
        print("IMPRIMINDO...")
        time.sleep(1)
        q50, q20, q10 = combinacoes[escolha]
        if q50 > 0:
            print(f"{q50} nota(s) de R$ 50,00")
        if q20 > 0:
            print(f"{q20} nota(s) de R$ 20,00")
        if q10 > 0:
            print(f"{q10} nota(s) de R$ 10,00")
    else:
        print("Opção inválida!")

def main():
    """
    Função principal para executar o programa de saque de dinheiro.
    """
    # Exibe as notas disponíveis antes de solicitar o valor do saque
    print("NOTAS DISPONÍVEIS: R$ 10,00, R$ 20,00, R$ 50,00")
    try:
        valor_saque = int(input("Nesse caixa você pode sacar até R$600,00. Informe o valor que deseja sacar: R$ "))
        print(f'Valor do saque: R$ {valor_saque}')
        saque_dinheiro(valor_saque)
    except ValueError:
        print("Entrada inválida! Por favor, insira um número.")

if __name__ == "__main__":
    main()
