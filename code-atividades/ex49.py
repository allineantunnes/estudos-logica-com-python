# Este codigo foi criado por I.A. Gemini


#  Crie um personagem épico com nome, classe (mago, guerreiro, etc.) e nível de poder.
# Atribua valores iniciais para seus atributos de ataque, defesa e vida.
# Mostre na tela o nome, a classe e o nível de poder do seu personagem, além de seus atributos iniciais.


# Definindo seu personagem épico!
nome_personagem = "Arcano, o Mago Lendário"
classe_personagem = "Mago"
nivel_poder = 100

# Atribuindo atributos poderosos!
ataque_personagem = 80
defesa_personagem = 60
vida_personagem = 150

# Revelando a lenda!
print(f"Nome: {nome_personagem}")
print(f"Classe: {classe_personagem}")
print(f"Nível de Poder: {nivel_poder}")
print(f"Ataque: {ataque_personagem}")
print(f"Defesa: {defesa_personagem}")
print(f"Vida: {vida_personagem}")

# Seu personagem enfrenta um monstro feroz com seus próprios atributos de ataque, defesa e vida.
# Crie um algoritmo para calcular o dano causado pelo seu personagem no monstro e vice-versa.
# Mostre na tela o dano causado por cada um a cada rodada, até que um deles chegue a zero de vida.
# Declare o vencedor e mostre a vida restante do personagem e do monstro.


# Definindo os combatentes!
nome_personagem = "Arcano, o Mago Lendário"
ataque_personagem = 80
defesa_personagem = 60
vida_personagem = 150

nome_monstro = "Goblim Terrível"
ataque_monstro = 50
defesa_monstro = 30
vida_monstro = 100

# Batalha épica!
while True:
    # Ataque do personagem
    dano_personagem = ataque_personagem - defesa_monstro
    if dano_personagem < 0:
        dano_personagem = 0
    vida_monstro -= dano_personagem

    # Ataque do monstro
    dano_monstro = ataque_monstro - defesa_personagem
    if dano_monstro < 0:
        dano_monstro = 0
    vida_personagem -= dano_monstro

    # Mostrando o status da batalha
    print(f"{nome_personagem} ataca {nome_monstro} causando {dano_personagem} de dano!")
    print(f"{nome_monstro} ataca {nome_personagem} causando {dano_monstro} de dano!")
    print(f"Vida do {nome_personagem}: {vida_personagem}")
    print(f"Vida do {nome_monstro}: {vida_monstro}")

    # Verificando o vencedor
    if vida_personagem <= 0:
        print(f"{nome_monstro} é o vencedor!")
        print(f"Vida restante do {nome_monstro}: {vida_monstro}")
        break
    elif vida_monstro <= 0:
        print(f"{nome_personagem} é o vencedor!")
        print(f"Vida restante do {nome_personagem}: {vida_personagem}")
        break
