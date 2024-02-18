#VARIAVEL GLOBAL

variavel_local = "Estou fora da funcao"
def funcao():
    global variavel_local
    print(variavel_local)

funcao() #Vai imprimir: Estou fora da funcao