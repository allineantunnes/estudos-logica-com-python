# Neste algoritmo, crie uma variável que armazene uma string e uma lista que armazena várias strings.

class Heroi:
    def __init__(self, nome, tipo, xp):
        self.nome = nome
        self.tipo = tipo
        self.xp = xp
    
    def __str__(self):
        return f"Name: {self.nome} \nTipo: {self.tipo} \nXp {self.xp} "
    
def criar_heroi():
    nome = input("Digite o nome do seu herói: ")
    while True:
        try:
            tipo = int(input("Escolhar a classe: \n1 - Mago\n2 - Guerreiro\n3 - Arqueiro\n4 - Paladino\n"))
            if 1 <= tipo <=4:
                break
            else:
                print("Opção Invalida.Digite um número entre 1 e 4.")
        except ValueError:
            print("Erro , digite um número inteiro")

    tipos = ["Mago", "Guerreiro", "Arqueiro", "Paladino"]
    xp = int(input("Digite xp do seu herói: "))
    return Heroi(nome, tipos[tipo-1], xp)

heroi = criar_heroi()
print(heroi)