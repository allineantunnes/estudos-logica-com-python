# Entrada e saída
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
print(f"{nome} tem {idade} anos")

# Conversão de tipos
valor = "10"
print(int(valor) + 5)

# Listas
numeros = [1, 2, 3]
numeros.append(4)
numeros.remove(2)
print(len(numeros))

# Laço com enumerate
nomes = ["Ana", "João", "Maria"]
for i, nome in enumerate(nomes):
    print(i, nome)

# Tratamento de erros
try:
    n = int(input("Digite um número: "))
    print(10 / n)
except ZeroDivisionError:
    print("Divisão por zero não permitida")
except ValueError:
    print("Entrada inválida")

