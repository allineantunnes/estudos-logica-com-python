def calcular_situacao(media: float) -> str:
    if media > 6.0:
        return "Aprovado"
    elif 4.0 <= media <= 6.0:
        return "Final"
    else:
        return "Reprovado"


def main():
    print("=== Sistema de Notas do Aluno ===\n")
    aluno = input("Digite o nome do aluno: ")
    
    medias_bimestres = []

    for bimestre in range(1, 5):
        print(f"\n--- {bimestre}º Bimestre ---")
        notas = []
        for i in range(1, 4):
            while True:
                try:
                    nota = float(input(f"Digite a {i}ª nota: "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("A nota deve estar entre 0 e 10.")
                except ValueError:
                    print("Entrada inválida! Digite um número.")
        
        media_bimestre = sum(notas) / len(notas)
        medias_bimestres.append(media_bimestre)
        situacao = calcular_situacao(media_bimestre)
        print(f"Média do {bimestre}º bimestre: {media_bimestre:.2f} - {situacao}")
    
    # Média anual
    media_anual = sum(medias_bimestres) / len(medias_bimestres)
    situacao_final = calcular_situacao(media_anual)
    
    print("\n=== Resultado Final ===")
    print(f"Aluno: {aluno}")
    print(f"Média anual: {media_anual:.2f} - {situacao_final}")


if __name__ == "__main__":
    main()
