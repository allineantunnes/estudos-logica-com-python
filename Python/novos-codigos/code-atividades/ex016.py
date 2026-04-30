#Utilizando a linguagem Python, simule um caixa eletrônico que pergunte o valor a ser sacado e qual a cédula
# de maior valor que o cliente deseja receber, em seguida retorne o valor retirado
# e o número de todas as cédulas utilizadas na composição do saque.
#Para os critérios de avaliação, o programa deverá:
    #Solicitar o valor (inteiro) a ser sacado;
    #Garantir que esse valor seja maior ou igual a 1 real;
    #Solicitar o valor máximo de cédula que o cliente deseja receber no saque (100, 50, 20, 10, 5, 2 e 1);
    #Garantir que valor de cédula informado seja válido, além de ser igual ou superior ao valor do saque;
    #Calcular a quantidade de cédulas (de cada tipo) utilizadas para a composição do valor a ser sacado;
    #O cálculo dever seguir a seguinte lógica: Utilizar a cédula (de maior valor informada pelo cliente) até que não seja mais possível, e então buscar a cédula imediatamente inferior e repetir o processo até que a composição do valor total seja satisfeita.
    #Informar o valor sacado e a quantidade de cédulas (de cada tipo) utlizadas.

#ALGORITMO DE SOLUÇÃO:
saque = int(input("Qual o valor que deseja sacar? "))
while saque < 1:
    print("O valor informado deve ser maior ou igual a 1 Real!")
    saque = int(input("Qual o valor que deseja sacar? "))

cedulas_aceitaveis = [1, 2, 5, 10, 20, 50, 100]

cedula = int(input("Valor máximo das cédulas (1 - 2 - 5 - 10 - 20 - 50 - 100)? "))
while cedula not in cedulas_aceitaveis:
    print("A cédula informada é inválida, informe um novo valor de cédula.")
    cedula = int(input("Valor máximo das cédulas (1 - 2 - 5 - 10 - 20 - 50 - 100)? "))

total = saque
cedulas_utilizadas = []

print(f"O valor sacado foi de R$ {saque}")
print("Cédulas:")

while total > 0:
    if total >= cedula:
        quantidade_cedulas = total // cedula
        total -= quantidade_cedulas * cedula
        cedulas_utilizadas.append((cedula, quantidade_cedulas))

    if cedula == 100:
        cedula = 50
    elif cedula == 50:
        cedula = 20
    elif cedula == 20:
        cedula = 10
    elif cedula == 10:
        cedula = 5
    elif cedula == 5:
        cedula = 2
    elif cedula == 2:
        cedula = 1

for cedula, quantidade in cedulas_utilizadas:
    print(f"{quantidade} de R$ {cedula}")
