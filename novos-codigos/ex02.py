# Programa para coletar nomes até o usuário decidir sair
# Inicializa a lista para armazenar os nomes
nomes = []

print("Digite os nomes para adicionar à lista. Para encerrar, digite 'SAIR'.")

while True:
    # Recebe o nome do usuário
    nome = input("Informe um nome: ").strip()
    
    # Verifica se o usuário deseja sair
    if nome.upper() == "SAIR":
        break
    
    # Adiciona o nome à lista
    nomes.append(nome)

# Exibe o tamanho da lista e os nomes informados
print(f"\nQuantidade de nomes informados: {len(nomes)}")
print("Nomes informados:")
for nome in nomes:
    print(f"- {nome}")