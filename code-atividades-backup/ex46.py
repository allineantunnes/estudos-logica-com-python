import time
def saqueDinheiro(valor):
    notas_disponiveis = [50, 20, 10]

    if valor < 10 or valor > 600:
        print("Valor inválido. O valor deve estar entre R$ 10,00 e R$ 600,00.")
        return

    if valor % 10 != 0:
        print("Impossível sacar esse valor nesse caixa eletrônico com as notas disponíveis!")
        return

    print("IMPRIMINDO...")
    time.sleep(1)
    for nota in notas_disponiveis:
        quantidade_notas = valor // nota
        valor %= nota
        time.sleep(1)  # Simulando o processo de contagem e distribuição de notas
        print(f"{quantidade_notas} nota(s) de R$ {nota},00")

valor_saque = int(input("Nesse caixa você pode sacar até R$600,00 -Notas disponíveis: R$ 10,00, R$20, R$20 e R$50- "))
print('Valor do saque R$', valor_saque)
saqueDinheiro(valor_saque)
