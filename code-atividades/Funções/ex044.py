def pegaMes(m):

    if m < 1 or m > 12:
        raise ValueError("Mês inválido!")
    print(m)
pegaMes(int(input("Digite um mês:")))
