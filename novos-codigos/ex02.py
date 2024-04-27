import random

numero_secreto = random.randint(1, 100)

while True:
    tentativa = int(input("Adivinhe o número (entre 1 e 100): "))
    if tentativa == numero_secreto:
        print("Parabéns! Você acertou!")
        break
    elif tentativa < numero_secreto:
        print("O número é maior. Tente novamente.")
    else:
        print("O número é menor. Tente novamente.")
