# ATENÇÃO: O código abaixo é um exemplo de exercícios de tratamento de exceções em Python.
# Exercício 1: Divisão com tratamento de exceções
# Enunciado: Escreva um programa que peça dois números ao usuário e realize a divisão entre eles. 
# Trate a exceção de divisão por zero e exiba uma mensagem apropriada.



# Exercício 2: Abertura de arquivo com tratamento de exceções
# Enunciado: Escreva um programa que tente abrir um arquivo chamado "dados.txt". 
# Caso o arquivo não exista, capture a exceção e exiba uma mensagem apropriada.


# Exercício 3: Conversão de string para inteiro
# Enunciado: Escreva um programa que peça ao usuário para digitar um número inteiro. 
# Caso o usuário insira um valor inválido, trate a exceção e exiba uma mensagem apropriada.


#ATENÇÃO: TENTE FAZER O EXERCICIO ANTES DE VISUALIZAR AS RESPOSTAS! 
#RESPOSTAS DOS EXERCÍCIOS DE TRATAMENTO DE EXCEÇÕES:
#resposta do Exercício 1: Divisão com tratamento de exceções

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 / num2
    print(f"O resultado da divisão é: {resultado}")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
except ValueError:
    print("Erro: Por favor, insira apenas números.")
finally:
    print("Operação finalizada.")


#Resposta do exercício 2: Abertura de arquivo com tratamento de exceções

try:
    with open("dados.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print("Conteúdo do arquivo:")
        print(conteudo)
except FileNotFoundError:
    print("Erro: O arquivo 'dados.txt' não foi encontrado.")
finally:
    print("Tentativa de leitura do arquivo concluída.")

#Resposta do exercício 3: Conversão de string para inteiro

try:
    numero = int(input("Digite um número inteiro: "))
    print(f"Você digitou o número: {numero}")
except ValueError:
    print("Erro: O valor digitado não é um número inteiro válido.")
finally:
    print("Programa encerrado.")


