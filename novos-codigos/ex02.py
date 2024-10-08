# crie uma calculadora simples que possa realizar operações básicas: adição, subtração, multiplicação e divisão.

def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro: Divisão por zero não é permitida."
    return x / y

def calculadora():
    while True:
        print("\nSelecione a operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        
        operacao = input("Digite a operação (1/2/3/4): ")
        
        if operacao in ['1', '2', '3', '4']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            
            if operacao == '1':
                resultado = adicionar(num1, num2)
                print(f"{num1} + {num2} = {resultado}")
            elif operacao == '2':
                resultado = subtrair(num1, num2)
                print(f"{num1} - {num2} = {resultado}")
            elif operacao == '3':
                resultado = multiplicar(num1, num2)
                print(f"{num1} * {num2} = {resultado}")
            elif operacao == '4':
                resultado = dividir(num1, num2)
                print(f"{num1} / {num2} = {resultado}")
        else:
            print("Operação inválida!")

        continuar = input("Deseja realizar outra operação? (s/n): ")
        if continuar.lower() != 's':
            print("Encerrando a calculadora.")
            break

if __name__ == "__main__":
    calculadora()
