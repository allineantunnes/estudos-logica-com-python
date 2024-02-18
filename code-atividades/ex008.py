#Estruturas de Repetições
#Atividades de fixação
#Desenvolva um programa que faça uma contagem regressiva para o estouro de fogos de artifício

soma = 0
quantidade = 1
while quantidade <= 8:
    nota = float(input('Nota Aluno  {}:'.format(quantidade)))
    soma = soma + nota
    quantidade = quantidade + 1
media = soma/8
print('A média da turma foi {}'.format(round(media)))