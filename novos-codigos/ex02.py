# Algoritimo para calcular o fatorial de um número
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
# Solicita ao usuário um número inteiro não negativo

num = int(input("Digite um número inteiro não negativo: "))
if num < 0:
    print("Número inválido! Por favor, digite um número não negativo.")
else:
    resultado = fatorial(num)
    print(f"O fatorial de {num} é {resultado}")
# e exibe o resultado
