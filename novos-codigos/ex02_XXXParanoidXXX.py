#Contribuição de XXXParanoidXXX em 20/06/2025 --> adorei o seu curso de GitHub no dio.me. Obrigado allineantunnes!

# Variável com uma string
mensagem_inicial = "Bem-vindo ao cadastro de nomes!"

# Lista com algumas strings iniciais
nomes = ["Ana", "Bruno", "Carlos"]

# Exibindo a mensagem
print(mensagem_inicial)

# Variável para controlar quantos nomes o usuário deseja adicionar
quantidade = int(input("Quantos nomes você quer adicionar à lista? "))

# Loop para adicionar novos nomes
for i in range(quantidade):
    novo_nome = input(f"Digite o nome {i + 1}: ")
    nomes.append(novo_nome)

# Exibindo todos os nomes cadastrados
print("\nLista de nomes atualizada:")
for nome in nomes:
    print(f"- {nome}")
