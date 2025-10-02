#Passagem por valor
def modificar(x):
    x = 5
    print("Valor dentro da função:", x)

num  = 10
modificar(num)
print("valor fora da função", num)