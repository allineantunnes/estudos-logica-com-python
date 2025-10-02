#Passagem por referência

def adicionar_elemento(lista):
    lista.append(4)
    print("Lista dentro da função:", lista)

minha_lista = [1, 2, 3]
adicionar_elemento(minha_lista)
print("Lista fora da função:", minha_lista)