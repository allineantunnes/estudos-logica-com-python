# Aula de Estrutura de Dados
# Listas, Tulpas, Dicionarios

num2 = (2, 8, 6, 9, 10 ) #Tulpa
num = [2, 8, 6, 9, 10] #Lista
num[2] = 3 #Substituiu o 6 pelo 3
num.append(7) #Adicionou um elemento [7] a lista
num.sort() #Colocou em ordem sort e o reverse=True inverteu a ordem(crescente-> decrescente)
num.insert(2, 0) #Inserirr valores, valor 0 na posição 2 [ao aldo do 3]
#num.pop(2) #Apagou o elemento da posição 2 [o zero que havia adicionado]
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)

print(f'Essa lista tem {len(num)} elementos') #Imprime o total de elementos dentro da lista