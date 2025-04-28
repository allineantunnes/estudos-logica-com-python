#Estruturas de Repetições
#Atividades de fixação
#Desenvolva um programa que faça uma contagem regressiva para o estouro de fogos de artifício

#ATENÇÃO: definimos que o parâmetro start seja igual a 9, stop igual a -1, e step igual -1.

#FOR II

soma = 0
for i in range(1, 9):
    nota = float(input('Nota Aluno {} :'.format(i)))
    soma = soma + nota
media = soma/8
print('A media da turma foi {}'.format(round(media)))