brasil = (('Alisson', 1), ('Dini Alves', 2), ('Miranda', 3), ('Rodrigo Caio', 4), ('Casemiro', 5), ('Felipe Luis', 6), ('Taison', 7), ('R. Augusto', 8), ('Gabriel Jesus', 9), ('Neymar', 10), ('P. Coutinho', 11), ('Marcelo', 12), ('Marquinhos', 13), ('T. Silva', 14), ('Paulinho', 15))
while True:
    numero = int(input("Digite um número entre 1 e 15: "))
    if 1 <= numero <= 15:
        jogador, brasil = brasil[numero - 1]
        print(f"O jogador {jogador} vestiu a camisa {brasil} nesta convocação.")
        break
    else:
        print("Número fora do intervalo.", end=' ')
