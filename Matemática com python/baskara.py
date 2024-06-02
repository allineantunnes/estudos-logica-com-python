"""Resolução de equações do segundo grau com a fórmula de Baskara e usar
a biblioteca matplotlip para tracar o gráfico da parábola. Além disso, usei 
um loop infinito para permitir que o usuário entre com novos valores para a, b e c e
etanbém para plotar o gráfico. Por ultimo usei try e except para tratar 
erros e incosistencias  das entrada de dados.""" 

# Importa a biblioteca math
import math


# Função para entrada de dados


def entrada_dados():
    # Solicita os valores de a, b e c
    while True:
        try:
            a = float(input("Entre com o valor de a: "))
        except ValueError:  # se algum caractere for digitado, será pedido novo valor
            print("Entre com valor em ponto flutuante diferente de zero")
        else:
            if a != 0:  # testa se a é dirente de zero
                break

    while True:
        try:
            b = float(input("Entre com o valor de b: "))
            break
        except ValueError:  # se algum caractere for digitado, será pedido novo valor
            print("Entre com valor em ponto flutuante")
            continue
    while True:
        try:
            c = float(input("Entre com o valor de c: "))
            break
        except ValueError:  # se algum caractere for digitado, será pedido novo valor
            print("Entre com valor em ponto flutuante")
            continue

    return a, b, c

# Função para cálculo do delta


def calculo_delta(a, b, c):
    # Calcula o valor do delta
    delta = b ** 2 - 4 * a * c

    return delta

# Função para cálculo de x1 e x2


def calculo_x1_x2(a, b, c):
    # Calcula os valores de x1 e x2
    delta = calculo_delta(a, b, c)

    if delta == 0:
        x1 = -b / (2 * a)
        X=[x1,x2]
        return X

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        X=[x1,x2]
        return X

# Função para impressão dos resultados

def impressao_resultados(a, b, c, x1, x2):
    # Imprime os valores de a, b, c, x1 e x2
    print("Equação do segundo grau:")
    print(f"ax^2 + bx + c = 0")
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = {c}")

    if x1 == x2:
        print(f"x = {x1}")
    else:
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")

# Função para plotagem do gráfico


def plot_grafico(a, b, c, x1, x2):
    import math
    import matplotlib
    import matplotlib.pyplot as plt
    import numpy as np
    
    #matplotlib.use('TkAgg')
     # Gera os pontos da parábola
    # Gera os pontos da parábola
    x = np.arange(-10, 10, 0.1)
    y = a * x ** 2 + b * x + c

    # Define o título do gráfico
    plt.title(f"Equação de Baskara\n {a}x^2 + {b}x + {c} = 0\n X1={x1} e X2={x2}", fontsize=10, fontweight="bold", color="green")
    plt.plot(x, y)
    plt.xlabel("Eixo x")
    plt.ylabel("Eixo y")
    # Desenha uma linha horizontal no eixo y
    plt.axhline(0, linewidth=0.5, linestyle='--', color='black')

    # Desenha uma linha vertical no eixo x
    plt.axvline(0, linewidth=0.5, linestyle='--', color='black')


    plt.show()
# Programa principal2

def main():
    # Loop para entrada de dados repetidas
    while True:
        # Recebe os valores de a, b e c
        a, b, c = entrada_dados()

        # Calcula os valores de x1 e x2
        X= calculo_x1_x2(a, b, c)
        x1=X[0]
        x2=X[1]


        # Imprime os resultados
        impressao_resultados(a, b, c, x1, x2)

        # plota o resultado
        plot_grafico(a, b, c, x1, x2)

        # Pergunta se o usuário deseja continuar
        continuar = input("Deseja continuar? (S/N): ")
        if continuar.upper() != "S":
            break


if __name__ == "__main__":
    main()

