# Exercício: Caixa Eletrônico Básico
# ---------------------------------------------------------
# Este programa simula um saque em um caixa eletrônico.
# O usuário informa um valor para sacar e o programa calcula
# quantas notas de R$50 e R$10 serão entregues.
#
# Objetivo:
# - Praticar entrada de dados com input()
# - Usar divisão inteira (//) e módulo (%) para calcular notas
# - Entender a lógica de distribuição de valores
# ---------------------------------------------------------

def sacar(valor):
    notas50 = valor // 50
    valor = valor % 50

    notas10 = valor // 10

    print("Você receberá:")
    print(f"{notas50} nota(s) de R$50")
    print(f"{notas10} nota(s) de R$10")

valor_saque = int(input("Digite o valor do saque (apenas múltiplos de 10): R$ "))
sacar(valor_saque)
