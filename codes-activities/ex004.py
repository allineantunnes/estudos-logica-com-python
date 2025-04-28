nomeAluno = str(input("Digite o nome do Aluno:"))
nota1 = int(input("Nota do 1º Bimestre (0 a 100):"))
nota2 = int(input("Nota do 2º Bimestre (0 a 100):"))
nota3 = int(input("Nota do 3º Bimestre (0 a 100):"))
nota4 = int(input("Nota do 4º Bimestre (0 a 100):"))

peso_bimestal1 = 2
peso_bimestral2 = 3

calc_media_ponderada = (nota1 * peso_bimestal1 + nota2 * peso_bimestal1 + nota3 * peso_bimestral2 + nota4 * peso_bimestral2) / (peso_bimestal1 * 2 + peso_bimestral2 * 2)

media_ponderada_inteira = round(calc_media_ponderada)

if media_ponderada_inteira >= 60:
    print(f'\033[1;40;42mO Aluno {nomeAluno} obteve a média de {media_ponderada_inteira} e está aprovado.')
elif 20 <= media_ponderada_inteira <= 59:
    print(f'\033[1;30;43mO Aluno {nomeAluno} obteve a média de {media_ponderada_inteira} e está em recuperação.')
elif media_ponderada_inteira < 20:
    print(f'\033[30;41mO Aluno {nomeAluno} obteve a média de {media_ponderada_inteira} e está reprovado.')
