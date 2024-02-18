import calcArea

def main():
    print("Cálculo das áreas de figuras geométricas:")
    print("1. Círculo")
    print("2. Triângulo")
    print("3. Retângulo")

    try:
        opcao = int(input("Qual figura deseja calcular a área? "))

        if opcao < 1 or opcao > 3:
            print("ERRO! Essa não é uma opção válida!")
        else:
            if opcao == 1:
                raio = float(input("Digite o raio do círculo: "))
                area = calcArea.calcular_area_circulo(raio)
                print(f"A área do círculo é: {area:.2f}")
            elif opcao == 2:
                base = float(input("Digite a base do triângulo: "))
                altura = float(input("Digite a altura do triângulo: "))
                area = calcArea.calcular_area_triangulo(base, altura)
                print(f"A área do triângulo é: {area:.2f}")
            elif opcao == 3:
                largura = float(input("Digite a largura do retângulo: "))
                altura = float(input("Digite a altura do retângulo: "))
                area = calcArea.calcular_area_retangulo(largura, altura)
                print(f"A área do retângulo é: {area:.2f}")
    except ValueError:
        print("ERRO! Essa não é uma opção válida!")


if __name__ == "__main__":
    main()
