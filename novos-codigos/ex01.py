# Desafio Open Source DIO - Manipulacao de Strings e Listas

def main():
    nome = input("Digite seu nome: ").strip()
    tecnologias = []

    print(f"\nOla, {nome}! Vamos listar 3 tecnologias que voce esta estudando.")
    for i in range(1, 4):
        tech = input(f"Digite a {i}a tecnologia: ").strip()
        tecnologias.append(tech)

    print("\n--- Resumo do Perfil ---")
    print(f"Desenvolvedor(a): {nome.title()}")
    print(f"Tecnologias ({len(tecnologias)}): {', '.join(tecnologias)}")

if __name__ == "__main__":
    main()
