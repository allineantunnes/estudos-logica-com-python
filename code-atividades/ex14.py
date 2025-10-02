while True:
    numero = int(input("Informe um número inteiro maior que zero: "))
    if numero > 1:
        break

divisores = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        divisores += 1

print(f"O número {numero} é primo" if divisores == 2 else f"O número {numero} tem {divisores} divisores, portanto não é primo")
